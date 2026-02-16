<div align="center">

<img alt="simplemem_logo" src="https://github.com/user-attachments/assets/6ea54ad1-e007-442c-99d7-1174b10d1fec" width="450">

<div align="center">

## Memória Vitalícia Eficiente para Agentes LLM

<small>Armazene, comprima e recupere memórias de longo prazo com compressão semântica sem perdas. Compatível com Claude, Cursor, LM Studio e mais.</small>

</div>

<p><b>Funciona com qualquer plataforma de IA que suporte MCP ou integração com Python</b></p>

<table>
<tr>
<td align="center" width="100">
  <a href="https://www.anthropic.com/claude">
    <img src="https://cdn.simpleicons.org/claude/D97757" width="48" height="48" alt="Claude Desktop" />
  </a><br/>
  <sub><a href="https://www.anthropic.com/claude"><b>Claude Desktop</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://cursor.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/cursor/FFFFFF">
      <img src="https://cdn.simpleicons.org/cursor/000000" width="48" height="48" alt="Cursor" />
    </picture>
  </a><br/>
  <sub><a href="https://cursor.com"><b>Cursor</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://lmstudio.ai">
    <img src="https://github.com/lmstudio-ai.png?size=200" width="48" height="48" alt="LM Studio" />
  </a><br/>
  <sub><a href="https://lmstudio.ai"><b>LM Studio</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://cherry-ai.com">
    <img src="https://github.com/CherryHQ.png?size=200" width="48" height="48" alt="Cherry Studio" />
  </a><br/>
  <sub><a href="https://cherry-ai.com"><b>Cherry Studio</b></a></sub>
</td>
<td align="center" width="100">
  <a href="https://pypi.org/project/simplemem/">
    <img src="https://cdn.simpleicons.org/pypi/3775A9" width="48" height="48" alt="PyPI" />
  </a><br/>
  <sub><a href="https://pypi.org/project/simplemem/"><b>Pacote PyPI</b></a></sub>
</td>
<td align="center" width="100">
  <sub><b>+ Qualquer<br/>Cliente MCP</b></sub>
</td>
</tr>
</table>

<div align="center">

<br/>

[🇨🇳 中文](./README.zh-CN.md) •
[🇯🇵 日本語](./README.ja.md) •
[🇰🇷 한국어](./README.ko.md) •
[🇪🇸 Español](./README.es.md) •
[🇫🇷 Français](./README.fr.md) •
[🇩🇪 Deutsch](./README.de.md) •
[🇧🇷 **Português**](./README.pt-br.md)<br/>
[🇷🇺 Русский](./README.ru.md) •
[🇸🇦 العربية](./README.ar.md) •
[🇮🇹 Italiano](./README.it.md) •
[🇻🇳 Tiếng Việt](./README.vi.md) •
[🇹🇷 Türkçe](./README.tr.md)

<br/>

[![Project Page](https://img.shields.io/badge/🎬_DEMO_INTERATIVO-Visitar_Site-FF6B6B?style=for-the-badge&labelColor=FF6B6B&color=4ECDC4&logoColor=white)](https://aiming-lab.github.io/SimpleMem-Page)

<p align="center">
  <a href="https://arxiv.org/abs/2601.02553"><img src="https://img.shields.io/badge/arXiv-2601.02553-b31b1b?style=flat&labelColor=555" alt="arXiv"></a>
  <a href="https://github.com/aiming-lab/SimpleMem"><img src="https://img.shields.io/badge/github-SimpleMem-181717?style=flat&labelColor=555&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="../../LICENSE"><img src="https://img.shields.io/github/license/aiming-lab/SimpleMem?style=flat&label=license&labelColor=555&color=2EA44F" alt="License"></a>
  <a href="https://github.com/aiming-lab/SimpleMem/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat&labelColor=555" alt="PRs Welcome"></a>
  <br/>
  <a href="https://pypi.org/project/simplemem/"><img src="https://img.shields.io/pypi/v/simplemem?style=flat&label=pypi&labelColor=555&color=3775A9&logo=pypi&logoColor=white" alt="PyPI"></a>
  <a href="https://pypi.org/project/simplemem/"><img src="https://img.shields.io/pypi/pyversions/simplemem?style=flat&label=python&labelColor=555&color=3775A9&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://mcp.simplemem.cloud"><img src="https://img.shields.io/badge/MCP-mcp.simplemem.cloud-14B8A6?style=flat&labelColor=555" alt="MCP Server"></a>
  <br/>
  <a href="https://discord.gg/KA2zC32M"><img src="https://img.shields.io/badge/Discord-Participar-5865F2?style=flat&labelColor=555&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="../../fig/wechat_logo3.JPG"><img src="https://img.shields.io/badge/WeChat-Grupo-07C160?style=flat&labelColor=555&logo=wechat&logoColor=white" alt="WeChat"></a>
</p>

<br/>

[Visão Geral](#-visão-geral) • [Início Rápido](#-início-rápido) • [Servidor MCP](#-servidor-mcp) • [Avaliação](#-avaliação) • [Citação](#-citação)

</div>

</div>

<br/>

## 🔥 Novidades

- **[02/09/2026]** 🚀 **Memória Cross-Session disponível - Superando Claude-Mem em 64%!** SimpleMem agora suporta **memória persistente entre conversas**. No benchmark LoCoMo, SimpleMem alcança uma **melhoria de 64%** sobre Claude-Mem. Seus agentes agora podem lembrar automaticamente o contexto, decisões e aprendizados de sessões anteriores. [Ver Documentação Cross-Session →](../../cross/README.md)
- **[01/20/2026]** **SimpleMem agora está disponível no PyPI!** 📦 Instale diretamente com `pip install simplemem`. [Ver Guia de Uso →](../PACKAGE_USAGE.md)
- **[01/18/2026]** **SimpleMem agora suporta Claude Skills!** 🚀
- **[01/14/2026]** **Servidor MCP do SimpleMem está NO AR e Open Source!** 🎉 Serviço de memória na nuvem em [mcp.simplemem.cloud](https://mcp.simplemem.cloud). [Documentação MCP →](../../MCP/README.md)
- **[01/05/2026]** Artigo do SimpleMem publicado no [arXiv](https://arxiv.org/abs/2601.02553)!

---

## 🌟 Visão Geral

<div align="center">
<img src="../../fig/Fig_tradeoff.png" alt="Compromisso Desempenho vs Eficiência" width="900"/>

*SimpleMem atinge um score F1 superior (43.24%) com custo mínimo de tokens (~550).*
</div>

**SimpleMem** é um framework de memória eficiente baseado em **compressão semântica sem perdas** que aborda o desafio fundamental da **memória eficiente de longo prazo para agentes LLM**. SimpleMem maximiza a **densidade de informação** e a **utilização de tokens** através de um pipeline de três estágios:

<table>
<tr>
<td width="33%" align="center">

### 🔍 Estágio 1
**Compressão Estruturada Semântica**

Destila interações não estruturadas em unidades de memória compactas com indexação multi-vista

</td>
<td width="33%" align="center">

### 🗂️ Estágio 2
**Síntese Semântica Online**

Integra instantaneamente contexto relacionado em representações abstratas unificadas para eliminar redundância

</td>
<td width="33%" align="center">

### 🎯 Estágio 3
**Planejamento de Recuperação Consciente da Intenção**

Infere a intenção de busca para determinar dinamicamente o escopo de recuperação

</td>
</tr>
</table>

<div align="center">
<img src="../../fig/Fig_framework.png" alt="Framework SimpleMem" width="900"/>
</div>

---

### 🏆 Comparação de Desempenho

<div align="center">

| Modelo | ⏱️ Construção | 🔎 Recuperação | ⚡ Total | 🎯 F1 Médio |
|:------|:--------------------:|:-----------------:|:-------------:|:-------------:|
| A-Mem | 5140.5s | 796.7s | 5937.2s | 32.58% |
| LightMem | 97.8s | 577.1s | 675.9s | 24.63% |
| Mem0 | 1350.9s | 583.4s | 1934.3s | 34.20% |
| **SimpleMem** ⭐ | **92.6s** | **388.3s** | **480.9s** | **43.24%** |

</div>

---

## 📦 Instalação

```bash
git clone https://github.com/aiming-lab/SimpleMem.git
cd SimpleMem
pip install -r requirements.txt
cp config.py.example config.py
```

---

## ⚡ Início Rápido

```python
from main import SimpleMemSystem

system = SimpleMemSystem(clear_db=True)
system.add_dialogue("Alice", "Bob, let's meet at Starbucks tomorrow at 2pm", "2025-11-15T14:30:00")
system.add_dialogue("Bob", "Sure, I'll bring the market analysis report", "2025-11-15T14:31:00")
system.finalize()

answer = system.ask("When and where will Alice and Bob meet?")
print(answer)
```

---

## 🔌 Servidor MCP

**🌐 Serviço na Nuvem**: [mcp.simplemem.cloud](https://mcp.simplemem.cloud)

```json
{
  "mcpServers": {
    "simplemem": {
      "url": "https://mcp.simplemem.cloud/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN"
      }
    }
  }
}
```

> 📖 [Documentação MCP](../../MCP/README.md)

---

## 📊 Avaliação

```bash
python test_locomo10.py
python test_locomo10.py --num-samples 5
```

---

## 📝 Citação

```bibtex
@article{simplemem2025,
  title={SimpleMem: Efficient Lifelong Memory for LLM Agents},
  author={Liu, Jiaqi and Su, Yaofeng and Xia, Peng and Zhou, Yiyang and Han, Siwei and  Zheng, Zeyu and Xie, Cihang and Ding, Mingyu and Yao, Huaxiu},
  journal={arXiv preprint arXiv:2601.02553},
  year={2025},
  url={https://github.com/aiming-lab/SimpleMem}
}
```

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja [LICENSE](../../LICENSE).

## 🙏 Agradecimentos

- 🔍 **Modelo de Embeddings**: [Qwen3-Embedding](https://github.com/QwenLM/Qwen)
- 🗄️ **Banco de Dados Vetorial**: [LanceDB](https://lancedb.com/)
- 📊 **Benchmark**: [LoCoMo](https://github.com/snap-research/locomo)
