# ICDAR HIPE-OCRepair-2026: Participation Guidelines

**Competition on LLM-Assisted OCR Post-Correction for Historical Documents**  
_v.2026-03-01 — HIPE-OCRepair-2026 Team_

## Useful Links

|                                     |                                                       |
| ----------------------------------- | ----------------------------------------------------- |
| 🌐 Competition website              | https://hipe-eval.github.io/HIPE-OCRepair-2026/       |
| 📦 Data repository                  | https://github.com/hipe-eval/HIPE-OCRepair-2026-data  |
| 📈 HIPE-OCRepair-scorer repository  | https://github.com/hipe-eval/HIPE-OCRepair-scorer/)   |
| 📊 Evaluation repository            | https://github.com/hipe-eval/HIPE-OCRepair-2026-eval  |
| 🏆 Leaderboard (to come)            | https://huggingface.co/spaces/hipe-ocrepair-2026-eval |
| 📝 Registration, timeline & contact | see competition website                               |

## Contents

1. [Introduction](#1-introduction)
2. [Task Definition](#2-task-definition)
3. [Data](#3-data)
4. [Input/Output Format](#4-inputoutput-format)
5. [Evaluation Campaign and System Responses](#5-evaluation-campaign-and-system-responses)
6. [Competition Report](#6-competition-report)

## 1. Introduction

HIPE-OCRepair-2026 is an [ICDAR 2026 Competition](https://icdar2026.org/index.php/competitions/) focused on **LLM-assisted OCR post-correction of historical documents**.

Despite advances in OCR technology, historical documents remain difficult to digitize accurately. Many institutions lack the resources to re-OCR millions of legacy pages, making **post-correction the primary path to improving OCR quality**. The rise of LLMs has opened new possibilities, but results across languages and error types remain inconsistent and hard to compare.

A central question motivating this competition is:

> _To what extent can modern large language models address the OCR debt accumulated in large-scale digitized historical collections?_

The competition aims to address this by providing **HIPE-OCRepair-Bench**, a unified multilingual benchmark for OCR post-correction, comprising curated datasets, an evaluation protocol, baseline systems, and an open leaderboard.

## 2. Task Definition

Participant teams correct **noisy OCR transcripts from historical documents** without
access to source images. For each text chunk (typically a paragraph or article), the input includes:

- the OCR hypothesis (erroneous transcription)
- document metadata (language, date, publication title, origin)
- indicative quality metrics pre-computed on training/dev data: CER, WER, and a [lexicon-based OCR quality score](https://huggingface.co/impresso-project/ocr-quality-assessor-unigram-light)

Systems return a corrected version of the text. The ground truth for evaluation is the corresponding manually verified transcription. The benchmark covers English, French, and German, with documents spanning the 17th to the 20th century.

The benchmark adopts a **semi-diplomatic transcription** approach: historical spelling and archaic forms are preserved in the ground truth, and the focus is on linguistic accuracy rather than layout reproduction. Systems are not required to reproduce line breaks or soft hyphens in their output (see [Section 3.4](#34-layout-encoding) and [Section 5.3](#53-pre-processing-before-scoring)).

## 3. Data

### 3.1 Overview

**HIPE-OCRepair-Bench** consolidates and harmonises multiple existing datasets alongside newly curated materials, covering historical newspapers and printed works in English, French, and German (17th–20th century).

| Dataset                                                          | Doc. Type  | Origin        | Period  | Version | License                                                               |
| :--------------------------------------------------------------- | :--------- | :------------ | :------ | :------ | :-------------------------------------------------------------------- |
| [`icdar2017`](documentation/README-icdar-2017.md)                | newspapers | existing      | 17C–20C | v1.1    | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| [`overproof`](documentation/README-overproof.md)                 | newspapers | existing      | 19C–20C | v1.0    | Research use only                                                     |
| [`impresso-nzz`](documentation/README-impresso-nzz.md)           | newspapers | existing      | 18C–20C | v1.1    | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)       |
| [`dta19`](documentation/README-dta19.md)                         | books      | existing      | 19C     | v0.1    | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)       |
| [`impresso-snippets`](documentation/README-impresso-snippets.md) | newspapers | newly created | 19C–20C | v1.0    | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) |

These constituent datasets originate from diverse sources and consequently vary in their original transcription policies, file formats, and degree of layout awareness (i.e. how much layout information — line breaks, hyphenation — is retained in the encoding).

In preparation for HIPE-OCRepair-2026, all datasets went through a unified curation pipeline:

- **Format standardisation**: all datasets are in JSON and follow the same [JSON schema](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/blob/main/schema/hipe-ocrepair.schema.json);
- **Quality filtering**: where necessary, excessively noisy (>10-15 CER) or very short documents were dismissed;
- **Transcription unit harmonisation**: OCR text units should neither be too short (individual lines are avoided) nor excessively long aggregations of unrelated text. Where article- and paragraph-like units exist they are preserved; elsewhere, semantic chunks are computationally derived;
- **Manual correction/verification** of GT for dev and test sets. Training sets retain original transcriptions (segmentation and formatting harmonisation only).

The benchmark reflects the diversity and complexity of real historical OCR data. Where original error rates were too low for meaningful evaluation (`dta19`), OCR conditions were artificially degraded by introducing noise at increasing intensity levels.

### 3.2 Dataset Descriptions

**`icdar2017`** — Historical newspapers from the BnF (French) and British Library (English). Monographs excluded. Original documents were very long concatenations of articles; semantic chunking (Chonkie, max 1024 tokens, min 5 sentences) was applied. Chunks with CER > 0.15 filtered out. No line information. Dev and test sets manually corrected.

**`overproof`** — Newspaper articles from the Sydney Morning Herald (Trove / NLA) and Chronicling America (Library of Congress). Dataset 1 excluded due to poor GT quality. Line-level alignment; original GT from crowdsourced Trove corrections plus manual verification. New splits created for this benchmark. All GT additionally verified for this benchmark.

**`impresso-nzz`** — Neue Zürcher Zeitung in Black Letter (Fraktur) font, digitised with ABBYY FineReader Server 11. Semantic chunk and sentence segmentation provided.

**`dta19`** — Pages from 39 DTA corpus books (30 samples per book). Original error rates were very low; images artificially corrupted at two noise levels to produce more challenging conditions.

**`impresso-snippets`** — Short newspaper paragraphs sampled from the multilingual Impresso corpus, with a newly transcribed ground truth. Line information is exactly preserved. No sentence or chunk segmentation. This data is newly created for this benchmark and has not been published before.

### 3.3 Text Structural Information

Each original dataset has a given document granularity that was either preserved or transformed into a new transcription unit, and optionally complemented with additional segmentation levels — sentences and semantic chunks — computed automatically. If present, these are provided as character offsets relative to the `transcription_unit` text. Line-level segmentation, where available in the original data, is likewise provided as character offsets.

| Dataset             | Lang       | Original Granularity            | Benchmark Transcription Unit | Line Offsets | Sentence Offsets | Chunk Offsets |
| :------------------ | :--------- | :------------------------------ | :--------------------------- | :----------: | :--------------: | :-----------: |
| `icdar2017`         | en, fr     | very long concatenated document | **semantic chunk**           |      —       |        ✓         |       ✓       |
| `overproof`         | en         | newspaper article               | **article**                  |      —       |        ✓         |       —       |
| `impresso-nzz`      | de         | newspaper page                  | **page**                     |      ✓       |        ✓         |       ✓       |
| `dta19`             | de         | book page                       | **page**                     |      ✓       |        —         |       —       |
| `impresso-snippets` | fr, de, en | newspaper paragraph             | **newspaper paragraph**      |      ✓       |        —         |       —       |

**Important:** Systems must correct the text in the `transcription_unit` field only. Sub-segmentation information (lines, sentences, chunks) is provided for reference and may optionally be used as context, but is not the target of evaluation.

### 3.4 Layout Encoding

Each original dataset either retains or discards layout information such as line breaks and soft hyphens. The benchmark preserves this information where it exists:

- **line breaks** (`\n`): only present where the original data had line-level segmentation;
- **paragraph breaks** (`\n\n`): only present where the transcription unit itself spans multiple paragraphs;
- **soft hyphens** (`¬\n`): only present where the original data had line-break hyphenation information, or where newly introduced during curation of the ground truth.

| Dataset             | Line breaks in OCR | Line breaks in GT | Para breaks in OCR | Para breaks in GT | Soft hyphens in OCR | Soft hyphens in GT |
| :------------------ | :----------------: | :---------------: | :----------------: | :---------------: | :-----------------: | :----------------: |
| `icdar2017`         |         —          |         —         |         —          |         —         |          —          |         —          |
| `overproof`         |         ✓          |         ✓         |         —          |         —         |          —          |         ✓          |
| `impresso-nzz`      |         ✓          |         ✓         |         ✓          |         ✓         |          ✓          |         ✓          |
| `dta19`             |        TBD         |        TBD        |         —          |         —         |         TBD         |        TBD         |
| `impresso-snippets` |         ✓          |         ✓         |         —          |         —         |          -          |         ✓          |

> **Note on `overproof`:** soft hyphens are present in the GT but not in the OCR. This reflects the fact that the original OCR output did not encode hyphenation, while the ground truth was reconstructed with explicit soft hyphen markers during curation.

> **Note on `icdar2017`:** the original data had no line-break information; residual layout artefacts may remain in some documents despite curation efforts.

**Important**: Layout information is preserved to support future layout-aware work, but systems are not required to reproduce it. The evaluation script normalises both output and ground truth before scoring, so systems are not penalised for layout encoding differences (see [Section 5.3](#53-pre-processing-before-scoring)). Concretely, the following transformations are applied:

- `¬\n` → `""` (soft hyphen + line break removed; word parts joined)
- `-\n` → `"-"` (hard hyphen preserved; layout break removed)
- `\n` → `" "` (remaining line breaks converted to spaces)

These transformations can be applied to training data without affecting evaluation scores. See the [normalise_layout() function](https://github.com/hipe-eval/HIPE-OCRepair-scorer/blob/main/hipe_ocrepair_scorer/utils/normalisation.py) in the evaluation repository.

### 3.5 OCR Source, GT Quality and Filtering

**Note on `dta19`**: There was no OCR hypothesis in the original data (only images
and GT). The OCR hypothesis was generated by artificially introducing noise into the original images at two intensity levels, starting from a clean manual GT.

| Dataset             | Lang     | OCR Engine                      | Avg CER (train) | Avg CER (dev) | Avg CER (test) | CER Filter     | GT Source                     | GT Correction Status                 |
| :------------------ | :------- | :------------------------------ | :-------------: | :-----------: | :------------: | :------------- | :---------------------------- | :----------------------------------- |
| `icdar2017`         | en       | various                         |      0.038      |     0.042     |      TBD       | > 0.15 removed | IMPACT project (manual)       | train: original; dev/test: corrected |
| `icdar2017`         | fr       | various                         |      0.038      |      TBD      |     0.028      | > 0.15 removed | IMPACT project (manual)       | train: original; dev/test: corrected |
| `overproof`         | en       | ABBYY                           |      0.083      |      TBD      |      TBD       | > 0.15 removed | crowdsourced (Trove) + manual | train: original; dev/test: corrected |
| `impresso-nzz`      | de       | ABBYY FineReader Server 11      |       TBD       |       —       |      TBD       | none           | manual                        | train: original; test: corrected     |
| `dta19` (noise 1)   | de       | artificially degraded (level 1) |       TBD       |      TBD      |      TBD       | none           | manual (DTA)                  | train: original; dev/test: corrected |
| `dta19` (noise 2)   | de       | artificially degraded (level 2) |       TBD       |      TBD      |      TBD       | none           | manual (DTA)                  | train: original; dev/test: corrected |
| `impresso-snippets` | fr,de,en | various                         |       TBD       |      TBD      |      TBD       | > 0.15 removed | manual (Impresso)             | newly created                        |

### 3.6 Splits

| Dataset             | Lang | Train | Dev | Test | Competition Test\* | Split Origin                                 |
| :------------------ | :--- |:-----:|:---:|:----:| :----------------: | :------------------------------------------- |
| `icdar2017`         | en   |  455  | 188 | TBD  |         ✓          | original train→train+dev; original test→test |
| `icdar2017`         | fr   |  391  |  —  | 230  |         ✓          | original train→train; original test→test     |
| `overproof`         | en   |  145  | 30  |  32  |         —          | no original split; new splits over SMH+CA    |
| `impresso-nzz`      | de   |  150  |  —  |  17  |         —          | original splits                              |
| `dta19` (noise 1)   | de   |  TBD  | TBD | TBD  |         ✓          | new splits (available around 5.03.2026)      |
| `dta19` (noise 2)   | de   |  TBD  | TBD | TBD  |         ✓          | new splits (available around 5.03.2026)      |
| `impresso-snippets` | fr   |  50   | 10  | 100  |         ✓          | new splits                                   |
| `impresso-snippets` | de   |  50   | 10  | 100  |         ✓          | new splits                                   |
| `impresso-snippets` | en   |  50   | 10  | 100  |         ✓          | new splits                                   |

(\*) ✓ = used as official competition test set; — = available for training/evaluation but not part of the official competition ranking.
(\*\*) numbers will be completed soon.

## 4. Input/Output Format

Each document in the benchmark follows a common JSON schema with four top-level fields:

- **`document_metadata`** — provenance and contextual information: dataset name, version, license, document ID, language, date, publication title, transcription unit scope, and segmentation origins. Also includes optional image links (IIIF URL or file path).

- **`ocr_hypothesis`** — the OCR text to be corrected (`transcription_unit`), along with token and character counts, optional sub-segmentation offsets (lines, sentences, paragraphs, semantic chunks), and a `quality_report` containing pre-computed CER, WER, and alignment scores against the ground truth.

- **`ground_truth`** — the reference transcription (`transcription_unit`), token and character counts, and the same optional sub-segmentation offsets as the OCR hypothesis. In test files, this field is masked.

- **`ocr_postcorrection_output`** — the field to be filled by participant systems. Contains the corrected transcription (`transcription_unit`) and an optional system identifier. A `quality_report` is computed by the scorer after submission.

The schema is available in the [data repository](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/blob/main/schema/hipe-ocrepair.schema.json).

Documents are serialised in **JSON Lines** (`.jsonl`) files.

The key fields for participants are:

- `ocr_hypothesis`: the OCR text to correct.
- `ocr_postcorrection_output`: where systems must fill in their response, leaving all other fields unchanged.

### File Naming and Releases

Files follow the naming convention:

```
hipe-ocrepair-bench_<version>_<dataset>_<split>_<language>.jsonl
```

Data is available on GitHub and Hugging Face. Each release has a corresponding git tag with release notes. **Test set ground truth is masked in released files** and published after the evaluation phase ends.

## 5. Evaluation Campaign and System Responses

### 5.1 General Rules

- **Registration** is required; see the competition website for the deadline and instructions.
- Teams may submit up to **3 runs** per dataset/language.
- External resources and pre-trained models — including proprietary ones — are permitted, provided they are documented in the system report.
- All submissions must pass the JSON schema validator before scoring.

### 5.2 Submission Format

For each document in the test file, fill the `ocr_postcorrection_output` field. All other fields must be preserved unchanged. Any document left with `ocr_postcorrection_output: null` is treated as identical to the OCR input (no correction applied).

**File naming:** `teamname_<inputfilename>_runX.jsonl` (where `runX` ∈ {`run1`, `run2`, `run3`})

Submit a single ZIP archive (see [submission instructions](https://hipe-eval.github.io/HIPE-OCRepair-2026/)).

### 5.3 Pre-processing Before Scoring

Two normalisation steps are applied sequentially to both system output and ground truth before metric computation:

**Step 1 — Layout normalisation:**

- `¬\n` (soft hyphen + line break) → `""` (removed; word parts joined)
- `-\n` (hard hyphen + line break) → `"-"` (hyphen preserved; line break removed)
- `\n` (remaining line breaks) → `" "` (converted to space)

**Step 2 — Whitespace normalisation:**

- Multiple consecutive whitespace characters collapsed to a single space
- Leading and trailing whitespace removed

Case, punctuation, digits, and accented characters are preserved as-is. Evaluation is therefore **case-sensitive** and **punctuation-sensitive**.

### 5.4 Metrics

#### Primary Metric: Character Match Error Rate (cMER)

All metrics are based on the **Match Error Rate (MER)**, computed at the character level as:

```
cMER = (S + D + I) / (H + S + D + I)
```

where H = hits, S = substitutions, D = deletions, I = insertions. Unlike standard CER, MER is bounded in [0, 1] because insertions appear in the denominator, reducing sensitivity to extreme hallucinations. cMER is equivalent to the normalised CER in the [OCR-D evaluation spec](https://ocr-d.de/en/spec/ocrd_eval.html#character-error-rate-cer).

cMER is **micro-averaged** at corpus level: characters are summed across all documents before dividing, so longer documents contribute proportionally more. cMER is preferred over wMER because word-level metrics unduly penalise systems for historical spelling variation and transcription conventions.

#### Secondary Metric: Preference Score

A sign-based score computed per document and then **macro-averaged** (unweighted) across all transcription units:

```
s_i = sign(cMER_in,i − cMER_out,i) ∈ {+1, 0, −1}; 0 iff cMER_in,i = cMER_out,i
```

A score of +1 means the system improved over the input OCR, 0 means no change, −1 means degradation. The mean preference score captures the _consistency_ of improvement across documents, complementing the _magnitude_ measured by cMER. Because it is sign-based and macro-averaged, each document contributes equally regardless of length, large gains on a few documents cannot dominate the score, and effect size is ignored, making it complementary to magnitude-based cMER rather than redundant.

#### Additional Metrics

- **wMER** (word-level MER): reported for completeness.
- **95%-Confidence intervals**: computed for all measures to ensure statistical robustness. Method: bootstrap.

#### Pre-processing Before Scoring

Two normalisation steps are applied sequentially to both system output and ground truth before metric computation:

**Step 1 — Layout normalisation:**

- `\n` (line break) → space
- `¬\n` (soft hyphen + line break) → removed (word parts joined)
- `-` (hard hyphen) → preserved

**Step 2 — Whitespace normalisation:**

- Multiple consecutive whitespace characters collapsed to a single space
- Leading and trailing whitespace removed

Case, punctuation, digits, and accented characters are preserved as-is. Evaluation is therefore **case-sensitive** and **punctuation-sensitive**.

#### Stratification

Results are reported per dataset and then averaged across datasets. Stratification by language may also be reported.

### 5.5 Scoring Tools

The evaluation repository provides:

- a **JSON schema validator** — verify your file format before submission
- a **[scorer](https://github.com/hipe-eval/HIPE-OCRepair-scorer/)** — compute cMER, wMER, and preference score locally

Participants are encouraged to use both tools before the official submission deadline.

---

## 6. Competition Report

ICDAR Competitions do not foresee mandatory system description papers, but we strongly encourage participant team to submit a paper describing their system and results. Reports may be submitted to the ICDAR 2026 proceedings or published elsewhere (journal, preprint, conference of choice) and shared on the competition website.

A **competition overview paper** will be compiled by the organisers and submitted to the ICDAR 2026 proceedings, summarising the approaches and results of all participating teams. Organisers will contact participants shortly after the competition to collect the necessary information.

---

## License

See per-dataset licenses on datasets individual [README files](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/tree/main/documentation).

---

## Acknowledgments

The HIPE-OCRepair-2026 organising team expresses its sincere appreciation to the ICDAR 2026 Conference and Competition Committee for hosting the task. HIPE-eval editions are organised within the framework of the [Impresso – Media Monitoring of the Past](https://impresso-project.ch) project, funded by the Swiss National Science Foundation under grant No. CRSII5_213585 and by the Luxembourg National Research Fund under grant No. 17498891.
