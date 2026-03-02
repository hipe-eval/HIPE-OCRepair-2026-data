# HIPE-OCRepair-2026 Data Repository

[HIPE-OCRepair-2026](https://hipe-eval.github.io/HIPE-OCRepair-2026/) is an [ICDAR 2026 Competition](https://icdar2026.org/index.php/competitions/) focused on **LLM-assisted OCR post-correction of historical documents**, with a particular emphasis on historical newspapers.

With renewed interest driven by large language models (LLMs), OCR post-correction has (re)gained momentum, resulting in a growing number of models and experimental approaches. However, these efforts often rely on heterogeneous legacy datasets that come with important limitations, making systematic evaluation and meaningful comparison across approaches difficult.

A central question motivating this competition is:

> **To what extent can modern large language models address the OCR debt accumulated in large-scale digitized historical collections?**

The competition addresses this by providing **HIPE-OCRepair-Bench**, a unified multilingual benchmark for OCR post-correction, comprising curated datasets, an evaluation protocol, baseline systems, and an open leaderboard.


## 📋 Participation Guidelines

All information about the task, datasets, evaluation protocol, and submission instructions is available in the **[Participation Guidelines](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/blob/data-guidelines-release/README-Participation-Guidelines.md)**.

## 🔗 Key Links

|                                              | |
|----------------------------------------------|---|
| 🌐 Competition website                       | https://hipe-eval.github.io/HIPE-OCRepair-2026/ |
| 📋 Participation Guidelines                  | [documentation/participation-guidelines.md](documentation/participation-guidelines.md) |
| 📈 Scorer                                    | [https://github.com/hipe-eval/HIPE-OCRepair-scorer](https://github.com/hipe-eval/HIPE-OCRepair-scorer)|
| 📊 Evaluation repository (after competition) | https://github.com/hipe-eval/HIPE-OCRepair-2026-eval |
| 🏆 Leaderboard (to come)                     | https://huggingface.co/spaces/hipe-ocrepair-2026-eval |
| 📝 Registration & contact                    | see competition website |

## 📦 Data

Data is available:
- in the [data/](data/) folder of this repository
    - in git [releases](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/releases)
- later: also on Zenodo

### Release History

| Date       | Release                                          |
|------------|--------------------------------------------------|
| 10.12.2025 | [Sample data](data/sample/)                      |
| 12.01.2026 | JSON schema for input data and predictions       |
| 02.03.2026 | Training and development data + Scorer           |
| 06.04.2026 | Masked test data — start of evaluation phase     |
| 08.04.2026 | Submission of system results                     |
| 10.04.2026 | Results publication + unmasked test data release |


## Acknowledgements

The HIPE-OCRepair-2026 organising team expresses its sincere appreciation to the ICDAR-2026 Competition Committee for the overall coordination and support. 

HIPE-OCRepair-2026 is part of the [HIPE-eval](https://github.com/hipe-eval) series of shared tasks on historical
document and information processing and evaluation.

HIPE-eval editions are organised within the framework of the [Impresso – Media Monitoring of the Past](https://impresso-project.ch) project, funded by the Swiss National Science Foundation under grant No. CRSII5_213585 and by the Luxembourg National Research Fund under grant No. 17498891.
