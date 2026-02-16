<div align="center">

<img alt="simplemem_logo" src="https://github.com/user-attachments/assets/6ea54ad1-e007-442c-99d7-1174b10d1fec" width="450">

<div align="center">

## Memoria a Vita Efficiente per Agenti LLM

<small>Archivia, comprimi e recupera memorie a lungo termine con compressione semantica senza perdita. Compatibile con Claude, Cursor, LM Studio e altro.</small>

</div>

<p><b>Funziona con qualsiasi piattaforma AI che supporta MCP o integrazione Python</b></p>

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
  <sub><a href="https://pypi.org/project/simplemem/"><b>Pacchetto PyPI</b></a></sub>
</td>
<td align="center" width="100">
  <sub><b>+ Qualsiasi<br/>Client MCP</b></sub>
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
[🇧🇷 Português](./README.pt-br.md)<br/>
[🇷🇺 Русский](./README.ru.md) •
[🇸🇦 العربية](./README.ar.md) •
[🇮🇹 **Italiano**](./README.it.md) •
[🇻🇳 Tiếng Việt](./README.vi.md) •
[🇹🇷 Türkçe](./README.tr.md)

<br/>

[![Project Page](https://img.shields.io/badge/🎬_DEMO_INTERATTIVO-Visita_il_Sito-FF6B6B?style=for-the-badge&labelColor=FF6B6B&color=4ECDC4&logoColor=white)](https://aiming-lab.github.io/SimpleMem-Page)

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
  <a href="https://discord.gg/KA2zC32M"><img src="https://img.shields.io/badge/Discord-Unisciti-5865F2?style=flat&labelColor=555&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="../../fig/wechat_logo3.JPG"><img src="https://img.shields.io/badge/WeChat-Gruppo-07C160?style=flat&labelColor=555&logo=wechat&logoColor=white" alt="WeChat"></a>
</p>

<br/>

[Panoramica](#-panoramica) • [Avvio Rapido](#-avvio-rapido) • [Server MCP](#-server-mcp) • [Valutazione](#-valutazione) • [Citazione](#-citazione)

</div>

</div>

<br/>

## 🔥 Novità

- **[02/09/2026]** 🚀 **Memoria Cross-Session disponibile - 64% più performante di Claude-Mem!** SimpleMem ora supporta **memoria persistente tra le conversazioni**. Nel benchmark LoCoMo, SimpleMem ottiene un **miglioramento del 64%** rispetto a Claude-Mem. I tuoi agenti ora possono ricordare automaticamente contesto, decisioni e apprendimenti dalle sessioni precedenti. [Documentazione Cross-Session →](../../cross/README.md)
- **[01/20/2026]** **SimpleMem è ora disponibile su PyPI!** 📦 Installa direttamente con `pip install simplemem`. [Guida all'uso del pacchetto →](../PACKAGE_USAGE.md)
- **[01/18/2026]** **SimpleMem ora supporta Claude Skills!** 🚀
- **[01/14/2026]** **Il server MCP di SimpleMem è LIVE e Open Source!** 🎉 Servizio di memoria cloud su [mcp.simplemem.cloud](https://mcp.simplemem.cloud). [Documentazione MCP →](../../MCP/README.md)
- **[01/05/2026]** L'articolo SimpleMem è stato pubblicato su [arXiv](https://arxiv.org/abs/2601.02553)!

---

## 🌟 Panoramica

<div align="center">
<img src="../../fig/Fig_tradeoff.png" alt="Compromesso Prestazioni vs Efficienza" width="900"/>

*SimpleMem raggiunge un punteggio F1 superiore (43.24%) con un costo minimo di token (~550).*
</div>

**SimpleMem** è un framework di memoria efficiente basato sulla **compressione semantica senza perdita** che affronta la sfida fondamentale della **memoria a lungo termine efficiente per agenti LLM**. SimpleMem massimizza la **densità informativa** e l'**utilizzo dei token** attraverso una pipeline a tre stadi:

<table>
<tr>
<td width="33%" align="center">

### 🔍 Stadio 1
**Compressione Strutturata Semantica**

Distilla interazioni non strutturate in unità di memoria compatte con indicizzazione multi-vista

</td>
<td width="33%" align="center">

### 🗂️ Stadio 2
**Sintesi Semantica Online**

Integra istantaneamente il contesto correlato in rappresentazioni astratte unificate per eliminare la ridondanza

</td>
<td width="33%" align="center">

### 🎯 Stadio 3
**Pianificazione del Recupero Consapevole dell'Intento**

Deduce l'intento di ricerca per determinare dinamicamente l'ambito di recupero

</td>
</tr>
</table>

<div align="center">
<img src="../../fig/Fig_framework.png" alt="Framework SimpleMem" width="900"/>
</div>

---

### 🏆 Confronto Prestazioni

<div align="center">

| Modello | ⏱️ Costruzione | 🔎 Recupero | ⚡ Totale | 🎯 F1 Medio |
|:------|:--------------------:|:-----------------:|:-------------:|:-------------:|
| A-Mem | 5140.5s | 796.7s | 5937.2s | 32.58% |
| LightMem | 97.8s | 577.1s | 675.9s | 24.63% |
| Mem0 | 1350.9s | 583.4s | 1934.3s | 34.20% |
| **SimpleMem** ⭐ | **92.6s** | **388.3s** | **480.9s** | **43.24%** |

</div>

---

## 📦 Installazione

```bash
git clone https://github.com/aiming-lab/SimpleMem.git
cd SimpleMem
pip install -r requirements.txt
cp config.py.example config.py
```

---

## ⚡ Avvio Rapido

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

## 🔌 Server MCP

**🌐 Servizio Cloud**: [mcp.simplemem.cloud](https://mcp.simplemem.cloud)

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

> 📖 [Documentazione MCP](../../MCP/README.md)

---

## 📊 Valutazione

```bash
python test_locomo10.py
python test_locomo10.py --num-samples 5
```

---

## 📝 Citazione

```bibtex
@article{simplemem2025,
  title={SimpleMem: Efficient Lifelong Memory for LLM Agents},
  author={Liu, Jiaqi and Su, Yaofeng and Xia, Peng and Zhou, Yiyang and Han, Siwei and  Zheng, Zeyu and Xie, Cihang and Ding, Mingyu and Yao, Huaxiu},
  journal={arXiv preprint arXiv:2601.02553},
  year={2025},
  url={https://github.com/aiming-lab/SimpleMem}
}
```

## 📄 Licenza

Questo progetto è sotto **Licenza MIT** - vedi [LICENSE](../../LICENSE).

## 🙏 Ringraziamenti

- 🔍 **Modello di Embedding**: [Qwen3-Embedding](https://github.com/QwenLM/Qwen)
- 🗄️ **Database Vettoriale**: [LanceDB](https://lancedb.com/)
- 📊 **Benchmark**: [LoCoMo](https://github.com/snap-research/locomo)
