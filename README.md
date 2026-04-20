# HIPE-OCRepair-2026 Data Repository

[HIPE-OCRepair-2026](https://hipe-eval.github.io/HIPE-OCRepair-2026/) is an [ICDAR 2026 Competition](https://icdar2026.org/index.php/competitions/) focused on **LLM-assisted OCR post-correction of historical documents**, with a particular emphasis on historical newspapers.

With renewed interest driven by large language models (LLMs), OCR post-correction has (re)gained momentum, resulting in a growing number of models and experimental approaches. However, these efforts often rely on heterogeneous legacy datasets that come with important limitations, making systematic evaluation and meaningful comparison across approaches difficult.

A central question motivating this competition is:

> **To what extent can modern large language models address the OCR debt accumulated in large-scale digitized historical collections?**

The competition addresses this by providing **HIPE-OCRepair-Bench**, a unified multilingual benchmark for OCR post-correction, comprising curated datasets, an evaluation protocol, baseline systems, and an open leaderboard.

## 📋 Participation Guidelines

All information about the task, datasets, evaluation protocol, and submission instructions is available in the **[Participation Guidelines](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/blob/main/README-Participation-Guidelines.md)**.

## 🔗 Important Links

|                                              |                                                                                                        |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------|
| 🌐 Competition website                       | https://hipe-eval.github.io/HIPE-OCRepair-2026/                                                        |
| 📋 Participation Guidelines                  | [README-Participation-Guidelines.md](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/blob/main/README-Participation-Guidelines.md)                               |
| 📈 Scorer                                    | [https://github.com/hipe-eval/HIPE-OCRepair-scorer](https://github.com/hipe-eval/HIPE-OCRepair-scorer) |
| 📊 Evaluation repository (after competition) | https://github.com/hipe-eval/HIPE-OCRepair-2026-eval                                                   |
| 🏆 Leaderboard (to come)                     | https://huggingface.co/spaces/hipe-ocrepair-2026-eval                                                  |
| 📝 Registration & contact                    | see competition website                                                                                |

## 📦 Data

Data is available:
- in the [data/](data/) folder of this repository and in the git [releases](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/releases)
- later: also on Zenodo

### Release History

- **20.04.2026**: Final competition release with **unmasked test files** with post-submission ground truth corrections | **Release tag** [v0.9.5](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/releases/tag/v0.9.5)
- **06.04.2026**: Release of **masked test files** for the competition | **Release tag** [v0.9.3](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/releases/tag/v0.9.3)
- **20.03.2026**: Release of train and dev sets for `dta19` dataset | **Release tag** [v0.9.2](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/releases/tag/v0.9.2)
- **11.03.2026**: Hot fix for `impresso-snippets` dataset | **Release tag** [v0.9.1](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/releases/tag/v0.9.1)
- **02.03.2026**: First data release with `overproof`, `icdar17`, `impresso-nzz` and `impresso-snippets` | **Release tag** [v0.9](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/releases/tag/v0.9)

## 🎓 Citation

### Competition Report

The HIPE-OCRepair-2026 shared task will be described in a competition report paper currently under review for the proceedings of ICDAR 2026.

**Citation:** *(BibTeX entry will be provided upon publication)*

### Participant Publications

Participating teams may publish their own system description papers. We will maintain a list of these publications here:

- **Team Name** - *Paper Title* - [Venue/Preprint] - [Link] *(coming soon)*


## 🤝 Acknowledgments

The HIPE-OCRepair-2026 organising team expresses its sincere appreciation to the ICDAR-2026 Competition Committee for the overall coordination and support.

### 👥 Participating Teams

We thank all teams who participated in the HIPE-OCRepair-2026 shared task:

#### BnF-Mistral
- **Mistral AI:** Maxime Kunsch, Jacques Sun, Yassine El Ouahidi
- **Bibliothèque nationale de France (BnF):** Sébastien Crétin, Marcel Bautista, Jean-Philippe Moreux

#### BLOCR
- **British Library:** Valentina Vavassori, Harry Lloyds
- **Code:** [github.com/harrylloyd-bl/hipe-ocrepair](https://github.com/harrylloyd-bl/hipe-ocrepair)

#### L3i
- **L3i Laboratory, La Rochelle Université:** Tien Nam Nguyen, Wenjun Sun, Ahmed Hamdi, Carlos-Emiliano Gonzalez-Gallardo, Mickaël Coustaty, Antoine Doucet

#### zakaria-ENSIAS
- **ENSIAS, Rabat, Morocco:** Zakaria Bouaouda


### 📚 HIPE-eval Series

HIPE-OCRepair-2026 is part of the [HIPE-eval](https://github.com/hipe-eval) series of shared tasks on historical document and information processing and evaluation.

HIPE-eval editions are organised within the framework of the [Impresso – Media Monitoring of the Past](https://impresso-project.ch) project, funded by the Swiss National Science Foundation under grant No. CRSII5_213585 and by the Luxembourg National Research Fund under grant No. 17498891.
