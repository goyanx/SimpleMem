<div align="center">

<img alt="simplemem_logo" src="https://github.com/user-attachments/assets/6ea54ad1-e007-442c-99d7-1174b10d1fec" width="450">

<div align="center">

## Эффективная Пожизненная Память для LLM-Агентов

<small>Хранение, сжатие и извлечение долгосрочных воспоминаний с помощью семантического сжатия без потерь. Работает с Claude, Cursor, LM Studio и другими.</small>

</div>

<p><b>Работает с любой AI-платформой, поддерживающей MCP или интеграцию с Python</b></p>

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
  <sub><a href="https://pypi.org/project/simplemem/"><b>Пакет PyPI</b></a></sub>
</td>
<td align="center" width="100">
  <sub><b>+ Любой MCP-<br/>клиент</b></sub>
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
[🇷🇺 **Русский**](./README.ru.md) •
[🇸🇦 العربية](./README.ar.md) •
[🇮🇹 Italiano](./README.it.md) •
[🇻🇳 Tiếng Việt](./README.vi.md) •
[🇹🇷 Türkçe](./README.tr.md)

<br/>

[![Project Page](https://img.shields.io/badge/🎬_ИНТЕРАКТИВНОЕ_ДЕМО-Посетить_Сайт-FF6B6B?style=for-the-badge&labelColor=FF6B6B&color=4ECDC4&logoColor=white)](https://aiming-lab.github.io/SimpleMem-Page)

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
  <a href="https://discord.gg/KA2zC32M"><img src="https://img.shields.io/badge/Discord-Присоединиться-5865F2?style=flat&labelColor=555&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="../../fig/wechat_logo3.JPG"><img src="https://img.shields.io/badge/WeChat-Группа-07C160?style=flat&labelColor=555&logo=wechat&logoColor=white" alt="WeChat"></a>
</p>

<br/>

[Обзор](#-обзор) • [Быстрый Старт](#-быстрый-старт) • [MCP Сервер](#-mcp-сервер) • [Оценка](#-оценка) • [Цитирование](#-цитирование)

</div>

</div>

<br/>

## 🔥 Новости

- **[02/09/2026]** 🚀 **Кросс-сессионная память доступна - на 64% лучше Claude-Mem!** SimpleMem теперь поддерживает **постоянную память между разговорами**. В бенчмарке LoCoMo SimpleMem достигает **улучшения на 64%** по сравнению с Claude-Mem. Ваши агенты теперь могут автоматически вспоминать контекст, решения и знания из предыдущих сессий. [Документация Cross-Session →](../../cross/README.md)
- **[01/20/2026]** **SimpleMem теперь доступен на PyPI!** 📦 Установите через `pip install simplemem`. [Руководство по использованию пакета →](../PACKAGE_USAGE.md)
- **[01/18/2026]** **SimpleMem теперь поддерживает Claude Skills!** 🚀
- **[01/14/2026]** **MCP-сервер SimpleMem запущен и является Open Source!** 🎉 Облачный сервис памяти на [mcp.simplemem.cloud](https://mcp.simplemem.cloud). [Документация MCP →](../../MCP/README.md)
- **[01/05/2026]** Статья SimpleMem опубликована на [arXiv](https://arxiv.org/abs/2601.02553)!

---

## 🌟 Обзор

<div align="center">
<img src="../../fig/Fig_tradeoff.png" alt="Компромисс производительности и эффективности" width="900"/>

*SimpleMem достигает лучшего показателя F1 (43.24%) при минимальных затратах токенов (~550).*
</div>

**SimpleMem** — это эффективный фреймворк памяти на основе **семантического сжатия без потерь**, решающий фундаментальную задачу **эффективной долгосрочной памяти для LLM-агентов**. SimpleMem максимизирует **плотность информации** и **утилизацию токенов** через трёхэтапный конвейер:

<table>
<tr>
<td width="33%" align="center">

### 🔍 Этап 1
**Семантическое Структурированное Сжатие**

Дистиллирует неструктурированные взаимодействия в компактные единицы памяти с мультиракурсной индексацией

</td>
<td width="33%" align="center">

### 🗂️ Этап 2
**Онлайн Семантический Синтез**

Мгновенно интегрирует связанный контекст в унифицированные абстрактные представления для устранения избыточности

</td>
<td width="33%" align="center">

### 🎯 Этап 3
**Планирование Извлечения с Учётом Намерений**

Определяет поисковое намерение для динамического определения области извлечения

</td>
</tr>
</table>

<div align="center">
<img src="../../fig/Fig_framework.png" alt="Архитектура SimpleMem" width="900"/>
</div>

---

### 🏆 Сравнение Производительности

<div align="center">

| Модель | ⏱️ Построение | 🔎 Извлечение | ⚡ Итого | 🎯 Средний F1 |
|:------|:--------------------:|:-----------------:|:-------------:|:-------------:|
| A-Mem | 5140.5s | 796.7s | 5937.2s | 32.58% |
| LightMem | 97.8s | 577.1s | 675.9s | 24.63% |
| Mem0 | 1350.9s | 583.4s | 1934.3s | 34.20% |
| **SimpleMem** ⭐ | **92.6s** | **388.3s** | **480.9s** | **43.24%** |

</div>

---

## 📦 Установка

```bash
git clone https://github.com/aiming-lab/SimpleMem.git
cd SimpleMem
pip install -r requirements.txt
cp config.py.example config.py
```

---

## ⚡ Быстрый Старт

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

## 🔌 MCP Сервер

**🌐 Облачный сервис**: [mcp.simplemem.cloud](https://mcp.simplemem.cloud)

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

> 📖 [Документация MCP](../../MCP/README.md)

---

## 📊 Оценка

```bash
python test_locomo10.py
python test_locomo10.py --num-samples 5
```

---

## 📝 Цитирование

```bibtex
@article{simplemem2025,
  title={SimpleMem: Efficient Lifelong Memory for LLM Agents},
  author={Liu, Jiaqi and Su, Yaofeng and Xia, Peng and Zhou, Yiyang and Han, Siwei and  Zheng, Zeyu and Xie, Cihang and Ding, Mingyu and Yao, Huaxiu},
  journal={arXiv preprint arXiv:2601.02553},
  year={2025},
  url={https://github.com/aiming-lab/SimpleMem}
}
```

## 📄 Лицензия

Проект распространяется под **лицензией MIT** — см. файл [LICENSE](../../LICENSE).

## 🙏 Благодарности

- 🔍 **Модель эмбеддингов**: [Qwen3-Embedding](https://github.com/QwenLM/Qwen)
- 🗄️ **Векторная БД**: [LanceDB](https://lancedb.com/)
- 📊 **Бенчмарк**: [LoCoMo](https://github.com/snap-research/locomo)
