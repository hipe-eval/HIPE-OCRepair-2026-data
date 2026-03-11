# Impresso-NZZ OCR Post-Correction Dataset

**Benchmark identifier:** `impresso-nzz`  
**Benchmark version:** `v0.9`  
**Hugging Face:** _tocome_

**Short description:**  
The Impresso-NZZ dataset originates from the [NZZ black letter ground truth repository](https://github.com/impresso/NZZ-black-letter-ground-truth) ([Ströbel & Clematide, 2019](https://www.zora.uzh.ch/id/eprint/177164/1/Improving_OCR_of_Black_Letter_in_Historical_Newspapers_The_Unreasonable_Effecti.pdf)). It comprises 167 randomly sampled front pages from the Neue Zürcher Zeitung (NZZ) spanning the period 1780–1947, when the newspaper was published in German Fraktur (black letter) font. The original ground truth contains 304,268 words and 43,151 lines, manually corrected on word and line levels using Transkribus after initial OCR with ABBYY FineReader Server 11.

For the HIPE-OCRepair benchmark, pages were filtered to exclude cases where OCR and ground truth had structural misalignments (missing lines or regions). The remaining pages were organized into the original train and test splits with additional sentence and semantic chunk segmentation and ocr quality metrics.

## In a nutshell

| Property | Value                                 |
|:----------|:--------------------------------------|
| **Language(s)** | German                                |
| **OCR engine(s)** | ABBYY FineReader Server 11            |
| **Total documents (benchmark)** | _updated after competition_           |
| **Total tokens (benchmark)** | _updated after competition_           |
| **Document granularity** | Page (newspaper front pages)          |
| **Segmentation level(s)** | Sentence, paragraph (region), line    |
| **Data splits available** | train and test                        |
| **Image linkage** | Yes (via DVC, only after competition) |


### Benchmark Release Notes

- **Release v0.9**
    - Pages with structural misalignments between OCR and ground truth excluded
    - Text constructed by concatenating lines and regions, preserving layout with line breaks (`\n`) and region breaks (`\n\n`).
    - Text normalization: ligature expansion, whitespace normalization applied at line level.
    - Sentence and semantic chunk segmentation added (computed on GT at page level, offsets mapped back to original text with layout markers).
    - JSONL format following the HIPE-OCRepair JSON schema.
    - Train/test splits derived from original sampling.
    - Quality metrics: OCR error rates (CER, WER) and alignment quality scores.

## 1. Original Dataset

### Key Characteristics (original)

| Property                 | Value                                                                                                                                                                                                                                                             |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Source**               | [NZZ black letter ground truth](https://github.com/impresso/NZZ-black-letter-ground-truth)                                                                                                                                                                        |
| **Publication**          | Ströbel, P. & Clematide, S. (2019). "[Improving OCR of Black Letter in Historical Newspapers: The Unreasonable Effectiveness of HTR Models on Low-Resolution Images](https://www.zora.uzh.ch/entities/publication/5c091957-40a8-40e4-ac37-cb4ed22938ff)". DH2019. |
| **Release Date**         | 2019                                                                                                                                                                                                                                                              |
| **Languages**            | German (Fraktur/black letter)                                                                                                                                                                                                                                     |
| **Document Type**        | Newspaper front pages                                                                                                                                                                                                                                             |
| **Temporal Coverage**    | 1780–1947                                                                                                                                                                                                                                                         |
| **OCR Engine**           | ABBYY FineReader Server 11 (via Transkribus)                                                                                                                                                                                                                      |
| **Original Format**      | XML (PAGE format) with images (.tif)                                                                                                                                                                                                                              |
| **Statistics**           | 167 pages; 304,268 words; 43,151 lines                                                                                                                                                                                                                            |
| **Alignment Level**      | Word and line level (word-level for 134 pages, line-level for all)                                                                                                                                                                                                |
| **Character Encoding**   | UTF-8                                                                                                                                                                                                                                                             |
| **License**              | [![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)                                                                                                                                                                                                                                                      |
| **Metadata**             | Page-level metadata (year, issue)                                                                                                                                                                                                                                 |
| **Ground Truth Source**  | Manual correction in Transkribus; HTR model used for ~47 pages                                                                                                                                                                                                    |
| **Original Data Splits** | Training/test splits used for HTR evaluation (17 test years)                                                                                                                                                                                                      |
| **Image Access**         | Available in original repository                                                                                                                                                                                                                                  |
| **Original Version**     | v1.1                                                                                                                                                                                                                                                              |
| **Original dataset DOI** | [https://doi.org/10.5281/zenodo.3333627](https://doi.org/10.5281/zenodo.3333627) |

### Original Sampling Strategy and Transcription Guidelines

Please refer to [https://github.com/impresso/NZZ-black-letter-ground-truth]
(https://github.com/impresso/NZZ-black-letter-ground-truth)

## 2. Benchmark Version

### Conversion Process

The HIPE-OCRepair conversion process involves:

1. **Filtering**: Exclude pages where OCR missed lines/regions that were manually added in ground truth (~5% reduction)
2. **Text Construction**: 
   - Lines concatenated within regions with `\n` separators
   - Regions concatenated with `\n\n` separators
   - Layout information preserved in transcription unit text
3. **Text Normalization**: Applied once at line level (ligature expansion, whitespace normalization)
4. **Segmentation**:
   - Sentence segmentation: Applied to GT text (no line breaks), offsets mapped back to original text
   - Semantic chunking: Applied to full page text using Chonkie
   - Line offsets: Extracted from PAGE XML structure
   - Paragraph offsets: Extracted from PAGE XML regions
5. **Alignment**: Sentence offsets computed for ground truth, then mapped to corresponding OCR text (line-aligned)
6. **Quality Metrics**: CER, WER, OCR-QA scores, and alignment quality scores computed
7. **Data Splits**: Train and test splits based on original splits.

### Benchmark Characteristics

| Property                 | Value                                                                                                                                             |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| **Benchmark Name**       | `impresso-nzz`                                                                                                                                    |
| **Version**              | v0.9                                                                                                                                              |
| **Components**           | Filtered pages from NZZ black letter corpus (1780–1947)                                                                                           |
| **Exclusions**           | Pages with structural misalignments                                                                                                               |
| **Languages**            | German (Fraktur)                                                                                                                                  |
| **Document Granularity** | Page (newspaper front page)                                                                                                                       |
| **Format**               | JSON Lines (.jsonl)                                                                                                                               |
| **Schema**               | [hipe-ocrepair.schema.json](https://github.com/hipe-eval/HIPE-OCRepair-scorer/blob/main/data/schema/hipe-ocrepair.schema.json)                    |
| **License**              | [![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/) |
| **Segmentation Levels**  | Lines, sentences, paragraphs (regions), semantic chunks                                                                                           |
| **Offset Format**        | Character positions `[start, end]` in transcription_unit text                                                                                     |
| **Text Normalisation**   | Ligature normalization, whitespace normalization at line level                                                                                    |
| **Line Breaks in Text**  | Preserved with `\n` (between lines) and `\n\n` (between regions)                                                                                  |
| **Data Splits**          | Train and Test                                                                                                                                    |
| **Split Strategy**       | Based on original dataset structure                                                                                                               |
| **Split Level**          | Page                                                                                                                                              |
| **Quality Metrics**      | CER, WER, OCR-QA score, alignment quality scores (the latter internal use)                                                                        |
| **Image Links**          | _after the competition_                                                                                                                           |

### Dataset Statistics

| Split             | Documents |    Sentences | Paragraphs | Tokens (GT) | Characters (GT) | Avg CER | Avg WER |
|:------------------|----------:|-------------:|-----------:|------------:|----------------:|--------:|--------:|
| **German Train**  |       150 |       12,525 |   1,466 |     197,797 |       1,542,112 |       0.0398 |       0.1756 |
| **German Test**   |        17 |        1,450 |     164 |      23,306 |         183,719 |       0.0485 |       0.1996 |
| **Total**         |       167 |            - |          - |           - |               - |       - |       - |
