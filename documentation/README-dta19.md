# DTA-19 OCR Post-Correction Dataset

**Benchmark identifier:** `dta19`  
**Benchmark version:** `v0.9.x`  
**Hugging Face:** _tocome_    
**Status**: not yet released, will be very soon

**Short description:**  
The DTA-19 dataset originates from the GT4HistOCR corpus ([Springmann et al., 2018](https://doi.org/10.21248/jlcl.33.2018.220)), specifically the DTA19 subset derived from the DFG-funded [Deutsches Textarchiv (DTA)](http://www.deutschestextarchiv.de/). The original dataset contains 39 German books from the period 1797-1898, comprising 243,942 lines in German Fraktur and early modern typefaces. Originally created for benchmarking OCR engines, the dataset provides high-quality manual transcriptions at the line level with corresponding images.

For the HIPE-OCRepair benchmark, synthetic OCR transcriptions at multiple noise levels were generated using Tesseract, producing OCR/ground truth pairs suitable for post-correction tasks. The dataset is organized at the page level into train, dev, and test splits, with additional sentence and semantic chunk segmentation. A key challenge, beyond imperfect OCR itself, is the presence of truncated sentences at page boundaries, where models should refrain from hallucinating missing content.

**Two Sampling Strategies Available:**
The benchmark provides two distinct versions of the dataset using different page sampling strategies across noise levels:

1. **Matched Strategy**: The same pages appear across all three noise levels (l0, l1, l2) within each split. This enables controlled evaluation of model robustness to increasing noise on identical content.

2. **Unmatched Strategy**: Different pages are sampled for each noise level within each split, with no page repetition across the entire dataset. This provides realistic independent evaluation and prevents information leakage when testing models sequentially across noise levels.

## In a nutshell

| Property | Value                                           |
|:----------|:------------------------------------------------|
| **Language(s)** | German                                          |
| **OCR engine(s)** | Tesseract model |
| **Total documents (benchmark)** | _updated after competition_                     |
| **Total tokens (benchmark)** | _updated after competition_                     |
| **Document granularity** | page                                            |
| **Segmentation level(s)** | chunk, sentence, line                           |
| **Data splits available** | train, dev, and test                            |
| **Image linkage** | yes, available after the competition            |


### Benchmark Release Notes

- **Release v0.9.5** (2026-04-20):
  - Post-competition ground truth corrections: All test files were manually reviewed and corrected after participant submissions, based on inspection of the best system outputs. Official evaluation results are based on these corrected files.
  - DTA19 test file naming convention change: Test files now consist exclusively of unmatched documents, and the `unmatched` label has been removed from their filenames for clarity (e.g., `*_test_de.jsonl` instead of `*_test-unmatched_de.jsonl`).
  - DTA19 train/dev files retain original naming: Files explicitly labeled with `unmatched` (e.g., `*_train-unmatched_de.jsonl`) contain unmatched documents; files labeled with matched (e.g., `*_train-matched_de.jsonl`) contain matched documents.
- **Release v0.9.3** (2026-04-06): 
  - Publication of masked test files for all DTA19 unmatched test sets (GT labels hidden for blind evaluation).
- **Release v0.9.2** (2026-03-20) and **Release v0.9.1** (2026-03-11): 
  - Updates to other datasets; DTA19 files unchanged from v0.9.
- **Release v0.9** (2026-03-02)
  - Initial DTA19 dataset release
  - Page samples from 39 German books from the Deutsche Textarchiv (period: 1797-1898)
  - Three synthetic OCR noise levels (l0, l1, l2) with controlled image degradation
  - Two sampling strategies available: 
    - Matched: Same pages used across all three noise levels (enables paired comparison)
    - Unmatched: Different pages per noise level (maximizes data diversity, 3× more unique pages)
  - Text normalization applied to both ground truth and OCR
  - Line breaks preserved in transcription with offset metadata
  - Automatic sentence and chunk segmentation applied (chunks may correspond to full pages given small page size)

## 1. Original Dataset

### Key Characteristics (original)

| Property                 | Value                                                                                                                                                                                                                                                                                                                     |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Source**               | GT4HistOCR dataset and Deutsches Textarchiv                                                                                                                                                                                                                                                                               |
| **Publication**          | Uwe Springmann, Christian Reul, Stefanie Dipper, and Johannes Baiter. 2018. [Ground Truth for training OCR engines on historical documents in German Fraktur and Early Modern Latin](https://doi.org/10.21248/jlcl.33.2018.220). Journal for Language Technology and Computational Linguistics 33, 1 (July 2018), 97–114. |
| **Release Date**         | August 2018                                                                                                                                                                                                                                                                                                               |
| **Languages**            | German  (multi-font)                                                                                                                                                                                                                                                                                                      |
| **Document Type**        | _To be completed_                                                                                                                                                                                                                                                                                                         |
| **Temporal Coverage**    | 18th-19th century (see Table 6 of the above reference, page 107)                                                                                                                                                                                                                                                          |
| **OCR Engine**           | No OCR hypothesis in original dataset (only line image/transcription pairs)                                                                                                                                                                                                                                               |
| **Original Format**      | line image/transcription pairs                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                           |
| **Alignment Level**      | _To be completed_                                                                                                                                                                                                                                                                                                         |
| **License**              | [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)                                                                                                                                                                                                                                                                                                                 |
| **Metadata**             | yes                                                                                                                                                                                                                                                                                                                       |
| **Ground Truth Source**  | manual transcription                                                                                                                                                                                                                                                                                                      |
| **Original Data Splits** | not present                                                                                                                                                                                                                                                                                                               |
| **Image Access**         | after the competition                                                                                                                                                                                                                                                                                                     |
| **Original Version**     | v1.0                                                                                                                                                                                                                                                                                                                      |

## 2. Benchmark Version

_To be completed with benchmark processing description_

### Synthetic OCR Generation with Controlled Noise Injection

For the benchmark, synthetic OCR transcriptions were generated using a controlled noise injection process to create three distinct difficulty levels:

1. **Noise Level 0 (Clean)**: No artificial noise injected into images before OCR. Represents baseline OCR quality with an OCR model (details after the competition) on clean historical documents.

2. **Noise Level 1 (Low Noise)**: Artificial degradation applied to page images targeting a Character Error Rate (CER) of approximately **0.03** (3%). Simulates moderate document quality issues.

3. **Noise Level 2 (Medium Noise)**: Stronger artificial degradation targeting a CER of approximately **0.07** (7%). Simulates more challenging OCR conditions with significant document degradation.

The noise injection process applies image degradation techniques (blur, noise, contrast adjustments) before running Tesseract OCR, ensuring reproducible and controlled error characteristics across the dataset. This approach allows systematic evaluation of post-correction systems under varying OCR quality conditions, using the same source documents and ground truth across all noise levels.

**Important**: In the default "Matched" sampling strategy the same pages appear in corresponding splits (train/dev/test) across all three noise levels, enabling direct comparison of post-correction performance under different OCR quality conditions. For more information, see below.

### Sampling Strategies: Matched vs. Unmatched

The DTA19 benchmark provides **two versions** differing in how pages are sampled across noise levels, while sharing the same book-level train/dev/test assignment (50%/30%/20%).
The **matched** strategy uses the same pages across noise levels, enabling controlled paired comparisons that isolate the effect of noise. The **unmatched** strategy uses entirely different pages at each noise level, providing a more realistic evaluation and avoiding context priming when models process texts sequentially.

#### Matched Strategy (Default)

**Concept:** The same pages appear across all three noise levels (l0, l1, l2) within each split.

**Evaluation Scenario:** Controlled evaluation of model robustness to increasing noise. This strategy supports testing how well a model handles the same content at different OCR quality levels.

**Characteristics:**
- Books randomly assigned to train (50%), dev (30%), test (20%) with seed=42
- 10 pages randomly sampled per book
- **The exact same 10 pages are used for l0, l1, and l2 within each split**
- Total: ~390 unique pages across all splits (39 books × 10 pages)
- Each page appears 3 times in the dataset (once per noise level)
- Enables paired comparison: same content, different noise levels

**File Naming:**
```
hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_train_de.jsonl
hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_train_de.jsonl
hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_train_de.jsonl
```


#### Unmatched Strategy

**Concept:** Different pages are sampled for each noise level within each split, with no page repetition anywhere in the entire dataset.

**Evaluation Scenario:** Realistic independent evaluation for testing models at different noise levels without any information leakage. This strategy supports training or evaluating models sequentially across noise levels.

**Characteristics:**
- Books randomly assigned to train (50%), dev (30%), test (20%) with seed=42 (same as matched)
- 10 pages sampled per book **per noise level** = 30 unique pages per book
- **Different pages for l0, l1, and l2** within each split
- Total: ~1,170 unique pages across all splits (39 books × 30 pages)
- No page appears twice in the entire dataset
- Prevents information leakage across noise levels

**File Naming:**
```
hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_train-unmatched_de.jsonl
hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_train-unmatched_de.jsonl
hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_train-unmatched_de.jsonl
```

#### Strategy Comparison

The benchmark provides both strategies to support different evaluation scenarios:

**Matched Strategy characteristics:**
- Enables controlled evaluation of model robustness to noise
- Supports paired comparisons (same content, different noise levels)
- Facilitates studying how noise level affects correction quality
- Controls for content variability across noise levels

**Unmatched Strategy characteristics:**
- Provides realistic, independent evaluation at each noise level
- Supports sequential model training on different noise levels
- Avoids information leakage between training and evaluation
- Offers maximum data diversity (3× more unique pages)

**Both strategies maintain:**
- Same book-level split assignments (books don't move between train/dev/test)
- Same random seed (42) for reproducibility

### Benchmark Characteristics

| Property                 | Value                                                                                                                                                                                                                                                                                                                                                                                                |
|:-------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Benchmark Name**       | `dta19`                                                                                                                                                                                                                                                                                                                                                                                              |
| **Version**              | v0.9                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Components**           | page samples from the 39 books                                                                                                                                                                                                                                                                                                                                                                       |
| **Exclusions**           | Only a sample of pages are retained from each book                                                                                                                                                                                                                                                                                                                                                   |
| **Languages**            | German                                                                                                                                                                                                                                                                                                                                                                                               |
| **Document Granularity** | page                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Format**               | JSON Lines (.jsonl)                                                                                                                                                                                                                                                                                                                                                                                  |
| **Schema**               | [hipe-ocrepair.schema.json](https://github.com/hipe-eval/HIPE-OCRepair-scorer/blob/main/data/schema/hipe-ocrepair.schema.json)                                                                                                                                                                                                                                                                       |
| **License**              | [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)                                                                                                                                                                                                                                                    |
| **Benchmark DOI**        | [https://doi.org/10.5281/zenodo.18824344](https://doi.org/10.5281/zenodo.18824344)                                                                                                                                                                                                                                                                                                                   |
| **Segmentation Levels**  | chunk, sentence, line                                                                                                                                                                                                                                                                                                                                                                                |
| **Offset Format**        | Character positions `[start, end]` in transcription_unit text                                                                                                                                                                                                                                                                                                                                        |
| **Text Normalisation**   | ligature normalisation                                                                                                                                                                                                                                                                                                                                                                               |
| **Line Breaks in Text**  | yes, with `\n`                                                                                                                                                                                                                                                                                                                                                                                       |
| **Data Splits**          | Train, Dev, and Test (newly done, for two scenarios `matched` and `unmatched`and three noise levels)                                                                                                                                                                                                                                                                                                 |
| **Split Strategy**       | Two strategies available: (1) **Matched** - same pages across all noise levels for controlled robustness testing; (2) **Unmatched** - different pages per noise level for realistic independent evaluation. Each split contains a fixed set of books (no book spanning several splits); 10 pages sampled per book. |
| **Split Level**          | page                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Quality Metrics**      | CER, WER, OCR-QA score, alignment quality scores                                                                                                                                                                                                                                                                                                                                                     |
| **Image Links**          | Not given for the competition                                                                                                                                                                                                                                                                                                                                                                        |

### Dataset Statistics 

_to be completed_

| Split                                                            | Documents | Sentences | Paragraphs | Tokens (OCR) |  Characters (OCR) | Avg CER | Avg WER |
|:-----------------------------------------------------------------|----------:|----------:|-----------:|-------------:|------------------:|--------:|--------:|
| **Train** (matched/unmatched, all noise levels)                  |   190/180 |         - |          - |            - |                 - |       - |       - |
| **Dev**  (matched/unmatched, all noise levels)                   |   110/100 |         - |          - |            - |                 - |       - |       - |
| **Test**  (matched/unmatched, all noise levels)                  |         - |         - |          - |            - |                 - |       - |       - |
| **Total**                                                        |         - |         - |          - |            - |                 - |       - |       - |


## 4. Known Issues and Considerations

None at this time. Please let us know if you encounter any issues!
