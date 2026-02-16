<div align="center">

<img alt="simplemem_logo" src="https://github.com/user-attachments/assets/6ea54ad1-e007-442c-99d7-1174b10d1fec" width="450">

<div align="center">

## Effizientes Lebenslang-Gedächtnis für LLM-Agenten

<small>Speichern, komprimieren und abrufen von Langzeitgedächtnis durch semantische verlustfreie Kompression. Kompatibel mit Claude, Cursor, LM Studio und mehr.</small>

</div>

<p><b>Funktioniert mit jeder KI-Plattform, die MCP oder Python-Integration unterstützt</b></p>

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
  <sub><a href="https://pypi.org/project/simplemem/"><b>PyPI-Paket</b></a></sub>
</td>
<td align="center" width="100">
  <sub><b>+ Jeder MCP-<br/>Client</b></sub>
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
[🇩🇪 **Deutsch**](./README.de.md) •
[🇧🇷 Português](./README.pt-br.md)<br/>
[🇷🇺 Русский](./README.ru.md) •
[🇸🇦 العربية](./README.ar.md) •
[🇮🇹 Italiano](./README.it.md) •
[🇻🇳 Tiếng Việt](./README.vi.md) •
[🇹🇷 Türkçe](./README.tr.md)

<br/>

[![Project Page](https://img.shields.io/badge/🎬_INTERAKTIVE_DEMO-Website_Besuchen-FF6B6B?style=for-the-badge&labelColor=FF6B6B&color=4ECDC4&logoColor=white)](https://aiming-lab.github.io/SimpleMem-Page)

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
  <a href="https://discord.gg/KA2zC32M"><img src="https://img.shields.io/badge/Discord-Beitreten-5865F2?style=flat&labelColor=555&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="../../fig/wechat_logo3.JPG"><img src="https://img.shields.io/badge/WeChat-Gruppe-07C160?style=flat&labelColor=555&logo=wechat&logoColor=white" alt="WeChat"></a>
</p>

<br/>

[Überblick](#-überblick) • [Schnellstart](#-schnellstart) • [MCP-Server](#-mcp-server) • [Bewertung](#-bewertung) • [Zitation](#-zitation)

</div>

</div>

<br/>

## 🔥 Neuigkeiten

- **[02/09/2026]** 🚀 **Cross-Session Memory ist da - 64% besser als Claude-Mem!** SimpleMem unterstützt jetzt **persistenten Speicher über Gespräche hinweg**. Im LoCoMo-Benchmark erreicht SimpleMem eine **64% Leistungssteigerung** gegenüber Claude-Mem. Ihre Agenten können nun automatisch Kontext, Entscheidungen und Erkenntnisse aus vorherigen Sitzungen abrufen. [Cross-Session Dokumentation →](../../cross/README.md)
- **[01/20/2026]** **SimpleMem ist jetzt auf PyPI verfügbar!** 📦 Installieren Sie direkt mit `pip install simplemem`. [Paket-Nutzungsanleitung →](../PACKAGE_USAGE.md)
- **[01/18/2026]** **SimpleMem unterstützt jetzt Claude Skills!** 🚀
- **[01/14/2026]** **SimpleMem MCP-Server ist LIVE und Open Source!** 🎉 Cloud-Gedächtnisdienst unter [mcp.simplemem.cloud](https://mcp.simplemem.cloud). [MCP-Dokumentation →](../../MCP/README.md)
- **[01/05/2026]** SimpleMem-Paper wurde auf [arXiv](https://arxiv.org/abs/2601.02553) veröffentlicht!

---

## 🌟 Überblick

<div align="center">
<img src="../../fig/Fig_tradeoff.png" alt="Leistung vs. Effizienz" width="900"/>

*SimpleMem erreicht einen überlegenen F1-Score (43.24%) bei minimalen Token-Kosten (~550).*
</div>

**SimpleMem** ist ein effizientes Gedächtnis-Framework basierend auf **semantischer verlustfreier Kompression**, das die grundlegende Herausforderung des **effizienten Langzeitgedächtnisses für LLM-Agenten** angeht. SimpleMem maximiert **Informationsdichte** und **Token-Nutzung** durch eine dreistufige Pipeline:

<table>
<tr>
<td width="33%" align="center">

### 🔍 Stufe 1
**Semantische Strukturierte Kompression**

Destilliert unstrukturierte Interaktionen in kompakte, multi-view-indexierte Gedächtniseinheiten

</td>
<td width="33%" align="center">

### 🗂️ Stufe 2
**Online Semantische Synthese**

Integriert verwandten Kontext sofort in einheitliche abstrakte Darstellungen zur Eliminierung von Redundanz

</td>
<td width="33%" align="center">

### 🎯 Stufe 3
**Intentionsbewusste Abrufplanung**

Leitet Suchintention ab, um den Abrufumfang dynamisch zu bestimmen und präzisen Kontext effizient zu konstruieren

</td>
</tr>
</table>

<div align="center">
<img src="../../fig/Fig_framework.png" alt="SimpleMem Framework" width="900"/>
</div>

---

### 🏆 Leistungsvergleich

<div align="center">

| Modell | ⏱️ Aufbauzeit | 🔎 Abrufzeit | ⚡ Gesamtzeit | 🎯 Durchschn. F1 |
|:------|:--------------------:|:-----------------:|:-------------:|:-------------:|
| A-Mem | 5140.5s | 796.7s | 5937.2s | 32.58% |
| LightMem | 97.8s | 577.1s | 675.9s | 24.63% |
| Mem0 | 1350.9s | 583.4s | 1934.3s | 34.20% |
| **SimpleMem** ⭐ | **92.6s** | **388.3s** | **480.9s** | **43.24%** |

</div>

---

## 📦 Installation

```bash
git clone https://github.com/aiming-lab/SimpleMem.git
cd SimpleMem
pip install -r requirements.txt
cp config.py.example config.py
```

---

## ⚡ Schnellstart

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

## 🔌 MCP-Server

**🌐 Cloud-Dienst**: [mcp.simplemem.cloud](https://mcp.simplemem.cloud)

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

> 📖 [MCP-Dokumentation](../../MCP/README.md)

---

## 📊 Bewertung

```bash
python test_locomo10.py
python test_locomo10.py --num-samples 5
```

---

## 📝 Zitation

```bibtex
@article{simplemem2025,
  title={SimpleMem: Efficient Lifelong Memory for LLM Agents},
  author={Liu, Jiaqi and Su, Yaofeng and Xia, Peng and Zhou, Yiyang and Han, Siwei and  Zheng, Zeyu and Xie, Cihang and Ding, Mingyu and Yao, Huaxiu},
  journal={arXiv preprint arXiv:2601.02553},
  year={2025},
  url={https://github.com/aiming-lab/SimpleMem}
}
```

## 📄 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz** - siehe [LICENSE](../../LICENSE).

## 🙏 Danksagungen

- 🔍 **Embedding-Modell**: [Qwen3-Embedding](https://github.com/QwenLM/Qwen)
- 🗄️ **Vektordatenbank**: [LanceDB](https://lancedb.com/)
- 📊 **Benchmark**: [LoCoMo](https://github.com/snap-research/locomo)
