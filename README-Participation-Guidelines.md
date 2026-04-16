# ICDAR HIPE-OCRepair-2026: Participation Guidelines

**Competition on LLM-Assisted OCR Post-Correction for Historical Documents**  
_v.2026-03-27 — HIPE-OCRepair-2026 Team_

## Useful Links

|                                     |                                                       |
| ----------------------------------- | ----------------------------------------------------- |
| 🌐 Competition website              | https://hipe-eval.github.io/HIPE-OCRepair-2026/       |
| 📦 Data repository                  | https://github.com/hipe-eval/HIPE-OCRepair-2026-data  |
| 📈 HIPE-OCRepair-scorer repository  | https://github.com/hipe-eval/HIPE-OCRepair-scorer/    |
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

The benchmark adopts a **semi-diplomatic transcription** approach: historical spelling and archaic forms are preserved in the ground truth, and the focus is on linguistic accuracy rather than layout reproduction. Systems are not required to reproduce line breaks or soft hyphens in their output (see [Section 3.4](#34-layout-encoding) and [Section 5.4](#54-pre-processing-before-scoring)).

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
- **Quality filtering**: where necessary, documents with CER > 0.15 or very short documents were removed;
- **Transcription unit harmonisation**: OCR text units should neither be too short (individual lines are avoided) nor excessively long aggregations of unrelated text. Where article- and paragraph-like units exist they are preserved; elsewhere, semantic chunks are computationally derived;
- **Manual correction/verification** of GT for dev and test sets. Training sets retain original transcriptions (segmentation and formatting harmonisation only).

The benchmark reflects the diversity and complexity of real historical OCR data. Where original error rates were too low for meaningful evaluation (`dta19`), OCR conditions were artificially degraded by introducing noise at increasing intensity levels.

### 3.2 Dataset Descriptions

**`icdar2017`** ([readme-icdar](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/tree/main/documentation/README-icdar-2017.md)) — Historical newspapers from the BnF (French) and British Library (English). Monographs excluded. Original documents were very long concatenations of articles; semantic chunking (Chonkie, max 1024 tokens, min 5 sentences) was applied. Chunks with CER > 0.15 filtered out. No line information. Dev and test sets manually corrected.

**`overproof`** ([readme-overproof]((https://github.com/hipe-eval/HIPE-OCRepair-2026-data/tree/main/documentation/README-overproof.md)) — Newspaper articles from the Sydney Morning Herald (Trove / NLA) and Chronicling America (Library of Congress). Dataset 1 excluded due to poor GT quality. Line-level alignment; original GT from crowdsourced Trove corrections plus manual verification. New splits created for this benchmark. All GT additionally verified for this benchmark.

**`impresso-nzz`** ([readme-nzz]((https://github.com/hipe-eval/HIPE-OCRepair-2026-data/tree/main/documentation/README-impresso-nzz.md)) — Neue Zürcher Zeitung in Black Letter (Fraktur) font, digitised with ABBYY FineReader Server 11. Semantic chunk and sentence segmentation provided.

**`dta19`** ([readme-dta19]((https://github.com/hipe-eval/HIPE-OCRepair-2026-data/tree/main/documentation/README-dta19.md))— Pages from 39 DTA corpus books (30 samples per book). Original error 
rates were very low; images artificially corrupted at two noise levels (level 1 and 
level 2) to produce more challenging conditions. Note that there was no OCR 
hypothesis in the original data (only images and GT); the OCR hypothesis was 
generated by applying an OCR model to the model.

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
| `impresso-snippets` |         ✓          |         ✓         |         —          |         —         |          —          |         ✓          |

> **Note on `overproof`:** soft hyphens are present in the GT but not in the OCR. This reflects the fact that the original OCR output did not encode hyphenation, while the ground truth was reconstructed with explicit soft hyphen markers during curation.

> **Note on `icdar2017`:** the original data had no line-break information; residual layout artefacts may remain in some documents despite curation efforts.

**Important**: Layout information is preserved to support future layout-aware work, but systems are not required to reproduce it. The evaluation script normalises both output and ground truth before scoring, so systems are not penalised for layout encoding differences (see [Section 5.4](#54-pre-processing-before-scoring)). Concretely, the following transformations are applied:

- `¬\n` → `""` (soft hyphen + line break removed; word parts joined)
- `-\n` → `"-"` (hard hyphen preserved; layout break removed)
- `\n` → `" "` (remaining line breaks converted to spaces)

These transformations can be applied to training data without affecting evaluation scores. See the [normalise_layout() function](https://github.com/hipe-eval/HIPE-OCRepair-scorer/blob/main/hipe_ocrepair_scorer/utils/normalisation.py) in the evaluation repository.

### 3.5 OCR Source, GT Quality and Filtering

| Dataset                 | Lang     | OCR Engine                 | Avg CER (train) | Avg CER (dev) | Avg CER (test) | CER Filter     | GT Source                     | GT Correction Status                 |
|:------------------------| :------- |:---------------------------| :-------------: | :-----------: | :------------: | :------------- | :---------------------------- | :----------------------------------- |
| `icdar2017`             | en       | various                    |      0.038      |     0.042     |      TBD       | > 0.15 removed | IMPACT project (manual)       | train: original; dev/test: corrected |
| `icdar2017`             | fr       | various                    |      0.038      |      TBD      |     0.028      | > 0.15 removed | IMPACT project (manual)       | train: original; dev/test: corrected |
| `overproof`             | en       | ABBYY                      |      0.083      |      TBD      |      TBD       | > 0.15 removed | crowdsourced (Trove) + manual | train: original; dev/test: corrected |
| `impresso-nzz`          | de       | ABBYY FineReader Server 11 |       TBD       |       —       |      TBD       | none           | manual                        | train: original; test: corrected     |
| `dta19` (level 0, 1, 2) | de       | Tesseract                  |       TBD       <br/>|      TBD      |      TBD       | none           | manual (DTA)                  | train: original; dev/test: corrected |
| `impresso-snippets`     | fr,de,en | various                    |       TBD       |      TBD      |      TBD       | > 0.15 removed | manual (Impresso)             | newly created                        |

### 3.6 Splits

| Dataset                 | Lang |  Train  |   Dev   | Test | Competition Test\* | Split Origin                                 |
|:------------------------| :--- |:-------:|:-------:|:----:| :----------------: |:---------------------------------------------|
| `icdar2017`             | en   |   455   |   188   | TBD  |         ✓          | original train→train+dev; original test→test |
| `icdar2017`             | fr   |   391   |    —    | 230  |         ✓          | original train→train; original test→test     |
| `overproof`             | en   |   145   |   30    |  32  |         —          | no original split; new splits over SMH+CA    |
| `impresso-nzz`          | de   |   150   |    —    |  17  |         —          | original splits                              |
| `dta19` (noise 0, 1, 2) | de   | 190/180 | 110/100 | TBD  |         ✓          | new splits                                   |
| `impresso-snippets`     | fr   |   50    |   10    | 100  |         ✓          | new splits                                   |
| `impresso-snippets`     | de   |   50    |   10    | 100  |         ✓          | new splits                                   |
| `impresso-snippets`     | en   |   50    |   10    | 100  |         ✓          | new splits                                   |

(\*) ✓ = used as official competition test set; — = available for training/evaluation but not part of the official competition ranking.

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
hipe-ocrepair-bench_{bench-version}_{dataset}_{primary_dataset_version}_{split}_{language}.jsonl
```

Data is available on GitHub and will be available on Hugging Face after the competition. Each release has a corresponding git tag with release notes. **Test set ground truth is masked in released files** and published after the evaluation phase ends.

## 5. Evaluation Campaign and System Responses

### 5.1 General Rules

- **Registration** is required; see the competition website for the deadline and instructions.
- Teams may submit up to **3 runs** per dataset/language.
- External resources and pre-trained models — including proprietary ones — are permitted, provided they are documented in the system report.
- All submissions must pass the JSON schema validator before scoring.

### 5.2 Submission Format

Submission files are JSONL files (one JSON object per line). Each record must contain at least the following fields:

```json
{
  "document_metadata": {
    "document_id": "unique-id",
    "primary_dataset_name": "unversioned dataset name as it appears in the reference file (e.g., icdar2017, impresso-snippets, dta19-l0)",
    "language": "Language code (e.g., en, de, fr)",
    "... other metadata fields as in the reference files": "..."
  },
  "ocr_hypothesis": {
    "transcription_unit": "Original OCR text (as provided)"
  },
  "ocr_postcorrection_output": {
    "transcription_unit": "Your system's corrected text"
  }
}
```

To be considered valid, a submission file must:   
1.	Validate against the json [schema](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/blob/main/schema/hipe-ocrepair.schema.json).
2.	Contain text in the `ocr_postcorrection_output` field. Any document left with `ocr_postcorrection_output: null` is treated as identical to the OCR input (no correction applied).

**File naming convention:**
A submission filename is formed by prepending your team name and appending a run suffix to the reference filename:

```
<teamname>_<reference-stem>_run<N>.jsonl
```

where `<reference-stem>` is the reference file's name without the `.jsonl` extension, and `run<N>` ∈ `{run1, run2, run3}`.

Expanded, this gives:

```
<teamname>_hipe-ocrepair-bench_<bench-version>_<dataset>_<dataset-version>_<split>_<language>_run<N>.jsonl
```

- `<teamname>`: lowercase alphanumeric characters and hyphens only — **no underscores**
- `<bench-version>`: benchmark version, currently `v0.9`
- `<dataset>_<dataset-version>`: exact versioned dataset identifier — see table in [Section 5.3](#53-datasets-part-of-the-2026-competition)
- `<split>`: `test`
- `<language>`: `en`, `de`, or `fr`
- `run<N>`: `run1`, `run2`, or `run3` — up to 3 runs per reference file per team

Example: `myteam_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run1.jsonl`

### 5.3 Datasets Part of the 2026 Competition

The following datasets are part of the official competition and test files are expected to be submitted for evaluation and ranking.

**Competition 2026 Test Data Table**

| Source dataset               | Versioned dataset identifier | Language(s) | Test Files                                                               |
| ---------------------------- | ---------------------------- | ----------- |--------------------------------------------------------------------------|
| icdar2017                    | `icdar2017_v1.1`             | en          | `hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en.jsonl`           |
| icdar2017                    | `icdar2017_v1.1`             | fr          | `hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr.jsonl`                  |
| impresso-snippets            | `impresso-snippets_v1.0`     | de          | `hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de.jsonl`          |
| impresso-snippets            | `impresso-snippets_v1.0`     | en          | `hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en.jsonl`          |
| impresso-snippets            | `impresso-snippets_v1.0`     | fr          | `hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr.jsonl`          |
| dta19 (level 0, unmatched)   | `dta19-l0_v0.1`              | de          | `hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test-unmatched_de.jsonll` |
| dta19 (level 1, unmatched)   | `dta19-l1_v0.1`              | de          | `hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test-unmatched_de.jsonl`  |
| dta19 (level 2, unmatched)   | `dta19-l2_v0.1`              | de          | `hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test-unmatched_de.jsonl`  |
| overproof                    | `overproof-combined_v1.0`    | en          | not part of competition                                                  |
| impresso-nzz                 | `impresso-nzz_v1.1`          | de          | not part of competition                                                  |

 **Note on dta19 level numbering:** the competition test sets cover levels 0, 1, and 2. Level 0 corresponds to the least degraded condition; levels 1 and 2 introduce increasing noise. 

### 5.4 Pre-processing Before Scoring

Before scoring, both the system output and the ground truth are normalised (see below).

### 5.5 Evaluation Metrics and Ranking Criteria

### Metrics and rankings

The primary evaluation metric is **character-level Match Error Rate (cMER)**. Secondary metrics include word-level MER and preference-based comparison scores against the raw OCR baseline.

Before scoring with normalization enabled, texts are normalized as follows:

- lowercased
- punctuation and other non-word characters replaced by spaces
- underscores replaced by spaces
- repeated whitespace collapsed

Evaluation is therefore **case-insensitive** and **punctuation-insensitive**, but still sensitive to accented characters (for example, `é` and `e` remain different).

A cMER of 0.05 means that the hypothesis and reference differ by 5% at the character level.

#### Aggregation levels

Each test dataset consists of a set of **transcription units**. All metrics are first computed at the level of individual transcription units and then aggregated.

For each dataset, the scorer reports:

- **`cmer_micro`**: character-level MER obtained by summing alignment counts across all transcription units in the dataset and computing cMER once from the summed totals within a test set
- **`cmer_macro`**: arithmetic mean of the transcription-unit-level cMER scores within a test set
- **`wmer_micro`** and **`wmer_macro`** are computed in the same way as cmer_micro and cmer_macro, but using word-level alignments produced by jiwer.process_words(...) after normalization. Here, hits, substitutions, deletions, and insertions are counted over aligned word sequences rather than character sequences.

In other words:

- **micro** aggregation gives more weight to longer transcription units in a test set
- **macro** aggregation gives equal weight to each transcription unit in a test set

#### Metric definitions used in the reports

The evaluation reports show the following metrics:

- **`cmer_micro`**: micro-averaged character-level Match Error Rate
- **`cmer_macro`**: macro-averaged character-level Match Error Rate
- **`wmer_micro`**: micro-averaged word-level Match Error Rate
- **`wmer_macro`**: macro-averaged word-level Match Error Rate
- **`pref_score_cmer_macro`**: macro-averaged preference score based on cMER

At the transcription-unit level, MER is defined as:

$$
\mathrm{MER} = \frac{S + D + I}{H + S + D + I}
$$

where \(H\) = hits, \(S\) = substitutions, \(D\) = deletions, and \(I\) = insertions at the relevant alignment level (characters for cMER, words for wMER).

For a dataset with transcription units \(i = 1, ..., N\):

```math
\mathrm{cMER\_micro} =
\frac{\sum_i S_i + \sum_i D_i + \sum_i I_i}
     {\sum_i H_i + \sum_i S_i + \sum_i D_i + \sum_i I_i}
```

```math
\mathrm{wMER\_micro} =
\frac{\sum_i S_i + \sum_i D_i + \sum_i I_i}
     {\sum_i H_i + \sum_i S_i + \sum_i D_i + \sum_i I_i}
```

```math
\mathrm{cMER\_macro} = \frac{1}{N} \sum_{i=1}^{N} \mathrm{cMER}_{i}
```

```math
\mathrm{wMER\_macro} = \frac{1}{N} \sum_{i=1}^{N} \mathrm{wMER}_{i}
```

The preference score for one transcription unit _i_ is defined as follows:

```math
\mathrm{pref}(i) =
\begin{cases}
1 & \text{if the system score is better than the raw OCR score} \\
0 & \text{if both scores are equal} \\
-1 & \text{if the system score is worse than the raw OCR score}
\end{cases}
```

The reported preference metrics are macro averages over transcription units:

```math
\mathrm{pref\_score\_cMER\_macro} =
\frac{1}{N} \sum_{i=1}^{N} \mathrm{pref\_cMER}(i)
```

#### Confidence intervals

The report tables include **95% bootstrap confidence intervals** for **`cmer_micro`** and **`pref_score_cmer_macro`**. These intervals are based on **10,000 bootstrap resamples** of the transcription units.

For **micro-averaged** metrics such as `cmer_micro`, the scorer resamples transcription units, sums their alignment counts, and recomputes the score from the pooled totals. For **macro-averaged** metrics such as `pref_score_cmer_macro`, it resamples the transcription units, recomputes the per-unit scores, and then takes their mean.

The reported lower and upper bounds correspond to the **2.5th** and **97.5th
percentiles** of the bootstrap distribution. In `fold_scores`, each metric is stored as
`(score, low_ci, high_ci)`. In `averaged_scores`, the central value is the unweighted
mean across datasets, and the confidence interval is obtained from the mean of the
per-dataset bootstrap samples.

#### Per-dataset scores and overall averages

Scoring is performed **per dataset** (using `primary_dataset_name` as the grouping key). In the output of the scorer, these dataset-level results are stored under `fold_scores`.

The overall results in `averaged_scores` are then computed as the **unweighted mean across datasets** of the corresponding dataset-level scores.

This means that:

- `fold_scores[dataset]["cmer_micro"]` is the **micro cMER within that dataset**
- `averaged_scores["cmer_micro"]` is the **mean of the dataset-level micro cMER values**

So the overall average is **not** a single global micro-average over all transcription units from all datasets combined. Instead, it is an equal-weight average over datasets.

#### Primary and secondary ranking criteria

The **primary per-test-set ranking metric** is **`cmer_micro`**:

- lower is better
- computed separately for each dataset
- longer transcription units contribute more within a dataset

The **secondary ranking metric** is **`pref_score_cmer_macro`**:

- higher is better
- measures how consistently a system improves over the raw OCR input across transcription units
- each transcription unit contributes equally

#### Official competition ranking across test sets

The scorer outputs per-dataset scores, including `cmer_micro` for each dataset.
The **official competition ranking** is computed separately from these scorer outputs as a **weighted mean of per-test-set `cmer_micro`** across the 8 official test sets.

The weighting scheme is defined by the competition design and is **not** the same as the scorer’s internal `averaged_scores`, which uses an unweighted mean across datasets.

The weights are chosen so that the language-level contributions remain balanced:

- for **English** and **French**, each language score is based on **two test sets**, each with weight **1**
- for **German**, the score is based on **four test sets**: `impresso-snippets` with weight **1**, and the three DTA test sets (`dta19-l0`, `dta19-l1`, `dta19-l2`) with weight **1/3** each

Thus, the three DTA test sets together contribute the same total weight as one other test set. For German, this makes the combined DTA contribution match the weight of `impresso-snippets`, just as English and French each combine two equally weighted test sets.

| Unversioned dataset identifier | Lang | Weight |
| ------------------------------ | ---- | ------ |
| `dta19-l0`                     | de   | 1/3    |
| `dta19-l1`                     | de   | 1/3    |
| `dta19-l2`                     | de   | 1/3    |
| `impresso-snippets`            | de   | 1      |

| Unversioned dataset identifier | Lang | Weight |
| ------------------------------ | ---- | ------ |
| `icdar2017`                    | en   | 1      |
| `impresso-snippets`            | en   | 1      |

| Unversioned dataset identifier | Lang | Weight |
| ------------------------------ | ---- | ------ |
| `icdar2017`                    | fr   | 1      |
| `impresso-snippets`            | fr   | 1      |

`impresso-nzz` and `overproof-combined` datasets do not contribute to the official rankings because they have been released earlier to the public.

#### Per-language rankings

In addition to the overall competition ranking, we report **per-language rankings** of submitted runs.

For a given language, the ranking is computed as a **weighted mean of per-test-set `cmer_micro`** over the official test sets for that language. The secondary criterion is the corresponding **weighted mean of `pref_score_cmer_macro`**.

This means in terms of unversioned datasets:

- for **English**, the language score is the mean over `icdar2017` and `impresso-snippets`
- for **French**, the language score is the mean over `icdar2017` and `impresso-snippets`
- for **German**, the language score is computed from `impresso-snippets` with weight `1` and from `dta19-l0`, `dta19-l1`, and `dta19-l2` with weight `1/3` each

As in the overall ranking, these language-level rankings are based on weighted combinations of **per-test-set scores**. They should not be confused with the scorer’s internal notions of **micro** and **macro**, which refer to aggregation over transcription units within a dataset.

### Results

The evaluation results are available in [HIPE_OCRepair_2026_evaluation_results.md](HIPE_OCRepair_2026_evaluation_results.md) and on the [HIPE-OCRepair-2026 website](https://hipe-eval.github.io/HIPE-OCRepair-2026/results).

The **official competition ranking** is computed as described above: a **weighted mean of `cmer_micro`** across the official test sets, with the corresponding **weighted mean of `pref_score_cmer_macro`** as secondary criterion.


### 5.6 Scorer

The [Scorer Repository](https://github.com/hipe-eval/HIPE-OCRepair-scorer/) provides:

- a **JSON schema validator** — verify your file format before submission
- a **[scorer](https://github.com/hipe-eval/HIPE-OCRepair-scorer/)** (available as `pip install`) — compute cMER, wMER, and preference score locally

Participants are encouraged to use both tools before the official submission deadline.

### 5.7 How to Submit

Submit a **single ZIP archive** named after your team name, containing all your run files. For example, if your team name is `myteam`, the archive should be named `myteam.zip` and contain files like `myteam_hipe-ocrepair-bench_v1.0_impresso-snippets_v1.0_test_de_run1.jsonl`.

Please submit the ZIP file at the emails communicated via the mailing list. A confirmation email will be sent upon successful receipt of your submission.

### 5.8 Reproducibility and Leaderboard

After the competition:

- All submissions and results will be made publicly available in a dedicated GitHub repository, together with the competition evaluation scripts.
- A Hugging Face leaderboard will be launched to present the official results and to enable future submissions and system comparisons. Scoring will follow the normalisation policy defined by the HIPE-OCRepair scorer.

Participants are also encouraged to share their system description papers and code repositories in order to support reproducibility and foster further research in this area.


## 6. Competition Report

ICDAR Competitions do not foresee mandatory system description papers, but we strongly encourage participant teams to submit a paper describing their system and results. Reports may be submitted to the ICDAR 2026 proceedings or published elsewhere (journal, preprint, conference of choice) and shared on the competition website.

A **competition overview paper** will be compiled by the organisers and submitted to the ICDAR 2026 proceedings, summarising the approaches and results of all participating teams. Organisers will contact participants shortly after the competition to collect the necessary information.


## License

See per-dataset licenses on datasets individual [README files](https://github.com/hipe-eval/HIPE-OCRepair-2026-data/tree/main/documentation).


## Acknowledgments

The HIPE-OCRepair-2026 organising team expresses its sincere appreciation to the ICDAR 2026 Conference and Competition Committee for hosting the task. HIPE-eval editions are organised within the framework of the [Impresso – Media Monitoring of the Past](https://impresso-project.ch) project, funded by the Swiss National Science Foundation under grant No. CRSII5_213585 and by the Luxembourg National Research Fund under grant No. 17498891.
