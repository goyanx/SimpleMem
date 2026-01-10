"""
Embedding utilities - Generate vector embeddings using SentenceTransformers
Supports Qwen3 Embedding models through SentenceTransformers interface
"""
from typing import List, Optional, Dict, Any
import numpy as np
import config
import os


class EmbeddingModel:
    """
    Embedding model using SentenceTransformers (supports Qwen3 and other models)
    """
    def __init__(self, model_name: str = None, use_optimization: bool = True):
        self.model_name = model_name or config.EMBEDDING_MODEL
        self.use_optimization = use_optimization
        
        print(f"Loading embedding model: {self.model_name}")
        
        name = self.model_name or ""
        name_lc = name.lower()

        # If user points to an Ollama-tagged model like "qwen3-embedding:0.6b",
        # prefer calling the OpenAI-compatible embeddings endpoint (e.g. http://localhost:11434/v1).
        # This avoids requiring Hugging Face / SentenceTransformer SBERT layout files.
        is_ollama_style = (":" in name) and ("/" not in name)
        if is_ollama_style:
            self._init_openai_compatible_embeddings()
            return

        # Otherwise, use SentenceTransformers (supports HF repo ids like "Qwen/Qwen3-Embedding-0.6B")
        is_qwen3_hf = name_lc.startswith("qwen3") or ("qwen3-embedding" in name_lc)
        if is_qwen3_hf:
            self._init_qwen3_sentence_transformer()
        else:
            self._init_standard_sentence_transformer()

    def _init_openai_compatible_embeddings(self):
        """Initialize embeddings via OpenAI-compatible API (e.g., Ollama /v1/embeddings)."""
        try:
            from openai import OpenAI

            # Reuse the same base URL as the LLM client; for Ollama this should be http://localhost:11434/v1
            base_url = getattr(config, "OPENAI_BASE_URL", None)
            api_key = getattr(config, "OPENAI_API_KEY", "") or "ollama"
            client_kwargs = {"api_key": api_key}
            if base_url:
                client_kwargs["base_url"] = base_url

            self.client = OpenAI(**client_kwargs)
            self.model_type = "openai_compatible_embeddings"
            self.supports_query_prompt = False
            self.dimension = getattr(config, "EMBEDDING_DIMENSION", None)
            if not self.dimension:
                # Best-effort default; will be inferred on first encode if needed
                self.dimension = 0

            print(f"Using OpenAI-compatible embeddings endpoint for model: {self.model_name}")
        except Exception as e:
            print(f"Failed to initialize OpenAI-compatible embeddings client: {e}")
            raise

    def _init_qwen3_sentence_transformer(self):
        """Initialize Qwen3 model using SentenceTransformers"""
        try:
            from sentence_transformers import SentenceTransformer
            
            # Map model names to actual model paths
            qwen3_models = {
                "qwen3-0.6b": "Qwen/Qwen3-Embedding-0.6B",
                "qwen3-4b": "Qwen/Qwen3-Embedding-4B", 
                "qwen3-8b": "Qwen/Qwen3-Embedding-8B"
            }
            
            model_path = qwen3_models.get(self.model_name, self.model_name)
            print(f"Loading Qwen3 model via SentenceTransformers: {model_path}")
            
            # Initialize with optimization settings
            if self.use_optimization:
                try:
                    # Try to use flash_attention_2 and left padding for better performance
                    self.model = SentenceTransformer(
                        model_path,
                        model_kwargs={
                            "attn_implementation": "flash_attention_2", 
                            "device_map": "auto"
                        },
                        tokenizer_kwargs={"padding_side": "left"},
                        trust_remote_code=True
                    )
                    print("Qwen3 loaded with flash_attention_2 optimization")
                except Exception as e:
                    print(f"Flash attention failed ({e}), using standard loading...")
                    self.model = SentenceTransformer(model_path, trust_remote_code=True)
            else:
                self.model = SentenceTransformer(model_path, trust_remote_code=True)
            
            self.dimension = self.model.get_sentence_embedding_dimension()
            self.model_type = "qwen3_sentence_transformer"
            
            # Check if Qwen3 supports query prompts
            self.supports_query_prompt = hasattr(self.model, 'prompts') and 'query' in getattr(self.model, 'prompts', {})
            
            print(f"Qwen3 model loaded successfully with dimension: {self.dimension}")
            if self.supports_query_prompt:
                print("Query prompt support detected")
                
        except Exception as e:
            print(f"Failed to load Qwen3 model: {e}")
            print("Falling back to default SentenceTransformers model...")
            self._fallback_to_sentence_transformer()

    def _init_standard_sentence_transformer(self):
        """Initialize standard SentenceTransformer model"""
        try:
            from sentence_transformers import SentenceTransformer
            try:
                self.model = SentenceTransformer(self.model_name)
            except FileNotFoundError as e:
                # Some HF transformer repos (e.g. Qwen3 embedding) require trust_remote_code=True
                # and are not laid out like an SBERT-exported model.
                missing = str(e).lower()
                if "sentence_xlnet_config.json" in missing or "sentence_bert_config.json" in missing:
                    print(
                        "SentenceTransformer SBERT config missing; retrying with trust_remote_code=True..."
                    )
                    self.model = SentenceTransformer(self.model_name, trust_remote_code=True)
                else:
                    raise
            self.dimension = self.model.get_sentence_embedding_dimension()
            self.model_type = "sentence_transformer"
            self.supports_query_prompt = False
            print(f"SentenceTransformer model loaded with dimension: {self.dimension}")
        except Exception as e:
            print(f"Failed to load SentenceTransformer model: {e}")
            raise

    def _fallback_to_sentence_transformer(self):
        """Fallback to default SentenceTransformer model"""
        fallback_model = "sentence-transformers/all-MiniLM-L6-v2"
        print(f"Using fallback model: {fallback_model}")
        self.model_name = fallback_model
        self._init_standard_sentence_transformer()

    def encode(self, texts: List[str], is_query: bool = False) -> np.ndarray:
        """
        Encode list of texts to vectors
        
        Args:
        - texts: List of texts to encode
        - is_query: Whether these are query texts (for Qwen3 prompt optimization)
        """
        if isinstance(texts, str):
            texts = [texts]
        
        if self.model_type == "openai_compatible_embeddings":
            return self._encode_openai_compatible(texts)

        # Use query prompt for Qwen3 models when encoding queries
        if self.model_type == "qwen3_sentence_transformer" and self.supports_query_prompt and is_query:
            return self._encode_with_query_prompt(texts)
        return self._encode_standard(texts)

    def encode_single(self, text: str, is_query: bool = False) -> np.ndarray:
        """
        Encode single text
        
        Args:
        - text: Text to encode
        - is_query: Whether this is a query text (for Qwen3 prompt optimization)
        """
        return self.encode([text], is_query=is_query)[0]
    
    def encode_query(self, queries: List[str]) -> np.ndarray:
        """
        Encode queries with optimal settings for Qwen3
        """
        return self.encode(queries, is_query=True)
    
    def encode_documents(self, documents: List[str]) -> np.ndarray:
        """
        Encode documents (no query prompt)
        """
        return self.encode(documents, is_query=False)
    
    def _encode_with_query_prompt(self, texts: List[str]) -> np.ndarray:
        """Encode texts using Qwen3 query prompt"""
        try:
            embeddings = self.model.encode(
                texts, 
                prompt_name="query",  # Use Qwen3's query prompt
                show_progress_bar=False,
                normalize_embeddings=True
            )
            return embeddings
        except Exception as e:
            print(f"Query prompt encoding failed: {e}, falling back to standard encoding")
            return self._encode_standard(texts)
    
    def _encode_standard(self, texts: List[str]) -> np.ndarray:
        """Encode texts using standard method"""
        embeddings = self.model.encode(
            texts, 
            show_progress_bar=False,
            normalize_embeddings=True
        )
        return embeddings

    def _encode_openai_compatible(self, texts: List[str]) -> np.ndarray:
        """Encode texts using an OpenAI-compatible embeddings API (e.g., Ollama)."""
        # OpenAI API expects `input` to be a string or list of strings.
        response = self.client.embeddings.create(
            model=self.model_name,
            input=texts,
        )

        vectors = [item.embedding for item in response.data]
        arr = np.asarray(vectors, dtype=np.float32)

        # Infer dimension if not set
        if not getattr(self, "dimension", None) or self.dimension == 0:
            self.dimension = int(arr.shape[1]) if arr.ndim == 2 else 0

        # Match previous behavior: normalize embeddings
        norms = np.linalg.norm(arr, axis=1, keepdims=True)
        norms = np.where(norms == 0, 1.0, norms)
        return arr / norms
