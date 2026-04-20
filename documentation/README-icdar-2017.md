# ICDAR-2017 OCR Post-Correction Dataset

**Benchmark identifier:** `icdar2017`  
**Benchmark version:** `v0.9`  
**Hugging Face:** _tocome_

**Short description:**  
The ICDAR-2017 dataset was originally released as part of the ICDAR-2017 Competition on Post-OCR Text Correction. It contains historical documents (newspapers and monographs) from the National Library of France (BnF) and the British Library (BL), digitized as part of the IMPACT project. The documents include OCR transcriptions aligned with ground truth corrections at the document level.

All ICDAR-2017 documents are very long, apparently resulting from the concatenation of various articles or from digitization at the page level. This differs from typical article-level newspaper segmentation.

For inclusion in the Impresso HIPE-OCRepair benchmark, only the **periodical (newspaper)** materials were retained. Given the very long document lengths, semantic chunking was applied (using Chonkie) to create more manageable units, and low-quality chunks (CER > 0.15) were filtered out. The corpus underwent conversion, segmentation enhancement, and manual ground truth correction for dev and test sets. The benchmark version includes both English and French newspaper chunks organized into train, dev and test splits.

## In a nutshell

| Property | Value                                                              |
|:----------|:-------------------------------------------------------------------|
| **Language(s)** | English, French                                                    |
| **OCR engine(s)** | Various OCR systems (as provided in the original dataset)          |
| **Total documents (benchmark)** | _updated after competition_                                        |
| **Total tokens (benchmark)** | _updated after competition_                                                |
| **Document granularity** | document chunk (semantically chunked from original long documents) |
| **Segmentation level(s)** | chunk (auto), sentence (auto)                                      |
| **Data splits available** | train, dev, and test                                               |
| **Image linkage** | Not available presently                                            |


### Benchmark Release Notes

- **Release v0.9.5** (2026-04-20):
  - Post-competition ground truth corrections: All test files were manually reviewed and corrected after participant submissions, based on inspection of the best system outputs. Official evaluation results are based on these corrected files.
- **Release v0.9.3** (2026-04-06): 
  - Publication of masked test files (GT labels hidden for blind evaluation).
- **Release v0.9.2** (2026-03-20) and **Release v0.9.1** (2026-03-11): 
  - Updates to other datasets; icdar2017 files unchanged from v0.9.
- **Release v0.9**
    - Initial release with converted ICDAR-2017 periodical materials (newspapers only).
    - Exclusion of monograph materials (not relevant for newspaper OCR post-correction).
    - Semantic chunking applied to very long documents using Chonkie (semantic chunker).
    - Sentence segmentation (automatically added, thus not perfect).
    - Quality filtering: OCR/GT chunk pairs with CER > 0.15 were excluded.
    - Manual ground truth correction applied to dev and test sets.
    - JSONL format following the HIPE-OCRepair JSON schema.
    - Data split strategy:
        - **Train**: benchmark chunks from original ICDAR-2017 train split 
        - **Dev**: benchmark chunks from original ICDAR-2017 train split, for 
          English only (manually 
          checked again for this benchmark)
        - **Test**: benchmark chunks from original ICDAR-2017 test split (manually 
          checked again for this benchmark)
    - Inclusion of quality assurance metrics: OCR error rates (CER, WER) and alignment quality scores.

## 1. Original Dataset

### Key Characteristics (original)

| Property                 | Value                                                                                                                                                                                                                                                                                                     |
|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Source**               | [ICDAR-2017 Competition on Post-OCR Text Correction](missing)                                                                                                                                                                                                                                             |
| **Publication**          | Guillaume Chiron, Antoine Doucet, Mickaël Coustaty, and Jean-Philippe Moreux. 2017. [ICDAR2017 Competition on Post-OCR Text Correction](https://ieeexplore.ieee.org/document/8270163). In 2017 14th IAPR International Conference on Document Analysis and Recognition (ICDAR), November 2017. 1423–1428. |
| **Release Date**         | 2017                                                                                                                                                                                                                                                                                                      |
| **Languages**            | English, French                                                                                                                                                                                                                                                                                           |
| **Document Type**        | Historical newspapers (periodicals) and monographs                                                                                                                                                                                                                                                        |
| **Temporal Coverage**    | 19th–20th century                                                                                                                                                                                                                                                                                         |
| **OCR Engine**           | Various OCR systems                                                                                                                                                                                                                                                                                       |
| **Original Format**      | Plain text (.txt) - OCR output and ground truth texts on different lines of document files                                                                                                                                                                                                                |
| **Document Length**      | Very long documents (concatenation of articles or page-level digitization)                                                                                                                                                                                                                                |
| **Alignment Level**      | Document-level                                                                                                                                                                                                                                                                                            |
| **Character Encoding**   | UTF-8                                                                                                                                                                                                                                                                                                     |
| **License**              | [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)                                                                                                                                                   |
| **Metadata**             | Document ID, language, document type (monograph/periodical)                                                                                                                                                                                                                                               |
| **Ground Truth Source**  | Manual corrections from IMPACT project digitization                                                                                                                                                                                                                                                       |
| **Original Data Splits** | Train and test splits provided per language                                                                                                                                                                                                                                                               |
| **Image Access**         | Not included in dataset                                                                                                                                                                                                                                                                                   |
| **Original Version**     | v1.1                                                                                                                                                                                                                                                                                                      |

## 2. Benchmark Version

For the Impresso HIPE-OCRepair benchmark, the original ICDAR-2017 dataset was **filtered (newspapers only)**, **semantically chunked** (necessary due to very long original documents that appear to result from concatenation of articles or page-level digitization), **quality-filtered** (CER threshold of 0.15), and converted to structured JSON format with enhanced segmentation and quality metrics. The dev and test sets underwent **manual ground truth correction**.

### Benchmark Characteristics

| Property | Value                                                                                                                                                                                |
|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Benchmark Name** | `icdar2017`                                                                                                                                                                          |
| **Version** | v1.2 (within Benchmark v0.9)                                                                                                                                                         |
| **Components** | English periodicals (BL), French periodicals (BnF)                                                                                                                                   |
| **Exclusions** | Monographs excluded (not newspaper materials); chunks with CER > 0.15 excluded                                                                                                       |
| **Languages** | English, French                                                                                                                                                                      |
| **Document Granularity** | Chunk (semantically chunked from long documents using Chonkie)                                                                                                                       |
| **Format** | JSON Lines (.jsonl)                                                                                                                                                                  |
| **Schema** | [benchmark_document_schema.json](../lib/schemas/benchmark_document_schema.json)                                                                                                      |
| **License** | [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)                              |
|          |                                                                                                                                                                                      |
| **Segmentation Levels** | chunk (semantic via Chonkie), sentence (SpaCy), paragraph (Chonkie)                                                                                                                  |
| **Offset Format** | Character positions `[start, end]` in transcription_unit text                                                                                                                        |
|          |                                                                                                                                                                                      |
| **Text Processing** | Ligature normalization, whitespace normalization                                                                                                                                     |
| **Line Breaks in Text** | Not present in original icdar, thus no information in HIPE-OCRepair benchmark either.                                                                                                |
| **Layout Preservation** | Not present in original icdar     |
|          |                                                     |
| **Data Splits** | Train, Dev, and Test (derived from original ICDAR-2017 splits)                                                                                                                       |
| **Split Strategy** | Train: chunks from original train split (auto-processed)<br>Dev: chunks from original train split (manually corrected)<br>Test: chunks from original test split (manually corrected) |
| **Split Level** | Chunk-level                                                                                                                                                                          |
|          |                                                                                                                                                                                      |
| **Quality Metrics** | CER, WER, OCR-QA score, alignment quality scores                                                                                                                                     |
| **Alignment Quality Categories** | Good (>0.9), Soft (>0.6), Wrong (<0.6)                                                                                                                                               |
| **Image Links** | Not available in current version                                                                                                                                                     |

### Dataset Statistics

| Split             |   Documents | Sentences | Paragraphs | Tokens (OCR) |  Characters (OCR) | Avg CER | Avg WER |
|:------------------|------------:|----------:|-----------:|-------------:|------------------:|--------:|--------:|
| **English Train** |       455 |     7,755 |          - |        173,063 |             998,169 |   0.0378 |   0.1582 |
| **English Dev**   |         188 |      3492 |          - |      58,641 |           343,843 |   0.0421 |   0.1700 |
| **English Test**  |          |      -  |       -  |         -  |              -  |    -  |    -  |
| **French Train**  |       391 |     13,539 |          - |          156,812  |              959,378  |   0.0376 |   0.1569 |
| **French Dev**    |        -  |      -  |       -  |         -  |              -  |    -  |    -  |
| **French Test**   |       - |     - |          - |       - |            - |   - |  - |
| **Total**         |        -  |      -  |       -  |         -  |              -  |    -  |    -  |


### 3.2 Encoding Details

**Text Layout Preservation:**
- None

**Character Offsets:**
- All offsets `[start, end]` are character positions in the transcription_unit
- Sentence offsets: Computed automatically (SpaCy) 
- No line offsets (not present in original dataset)

**Alignment Quality Scores  (not part of competition data):**
- Format: `[category, score1, score2]`
  - `category`: "good" (>0.9), "soft" (>0.6), "wrong" (<0.6)
  - `score1`: Similarity score (0-1)
  - `score2`: Levenshtein similarity (0-1)
- Computed at transcription_unit, sentence, and paragraph levels

**Complete specification**: See [benchmark_document_schema.json](../lib/schemas/benchmark_document_schema.json)

## 4. Known Issues and Considerations

- **Ground truth quality**: Several research papers have noted issues in the original ground truth. The dev and test sets have been manually corrected, but the train set retains the original ground truth with potential inconsistencies.
- **Semantic chunking**: Very long documents were chunked using Chonkie's semantic chunker, which may split documents at semantically appropriate but not always optimal boundaries.
- **Quality filtering**: Chunks with CER > 0.15 were excluded, which may affect the representation of very low-quality OCR in the dataset.
- **Sentence segmentation**: Automatically added during conversion and may not be perfect.
- **Monographs excluded**: Only newspaper (periodical) materials are included in the benchmark.
- **Split derivation**: Train, dev, and test splits are derived from the original ICDAR-2017 train and test sets, not randomly split.
