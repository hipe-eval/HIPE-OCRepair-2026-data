# DTA-19 OCR Post-Correction Dataset

**Benchmark identifier:** `dta19`  
**Benchmark version:** `v0.9.x`  
**Hugging Face:** _tocome_    
**Status**: not yet released, will be very soon

**Short description:**  
The DTA-19 dataset originates from the GT4HistOCR corpus ([Springmann et al., 2018](https://doi.org/10.21248/jlcl.33.2018.220)), specifically the DTA19 subset derived from the DFG-funded [Deutsches Textarchiv (DTA)](http://www.deutschestextarchiv.de/). The original dataset contains 39 German books from the period 1797-1898, comprising 243,942 lines in German Fraktur and early modern typefaces. Originally created for benchmarking OCR engines, the dataset provides high-quality manual transcriptions at the line level with corresponding images.

For the HIPE-OCRepair benchmark, synthetic OCR transcriptions with multiple noise levels were generated using Tesseract, creating OCR/ground truth pairs suitable for post-correction tasks. The dataset was sampled at the page level and organized into train, dev, and test splits, with additional sentence and semantic chunk segmentation. Pages in the test set were manually curated to remove truncated sentences at the beginning and end of each page, ensuring complete sentence boundaries.

## In a nutshell

| Property | Value                                            |
|:----------|:-------------------------------------------------|
| **Language(s)** | German                                           |
| **OCR engine(s)** | Tesseract model `frak2021_0.905_1587027_9141630` |
| **Total documents (benchmark)** | _updated after competition_                      |
| **Total tokens (benchmark)** | _updated after competition_                      |
| **Document granularity** | page                                             |
| **Segmentation level(s)** | chunk, sentence, line                            |
| **Data splits available** | train, dev, and test                             |
| **Image linkage** | yes, available after the competition             |


### Benchmark Release Notes

- **Release vx.x**
    - _will be released soon_

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

### Benchmark Characteristics

| Property | Value                                                                                                                                          |
|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Benchmark Name** | `dta19`                                                                                                                                        |
| **Version** | _To be completed_                                                                                                                              |
| **Components** | page samples from the 39 books                                                                                                                 |
| **Exclusions** | Only a sample of pages are retained from each book                                                                                             |
| **Languages** | German                                                                                                                                         |
| **Document Granularity** | page                                                                                                                                           |
| **Format** | JSON Lines (.jsonl)                                                                                                                            |
| **Schema** | [hipe-ocrepair.schema.json](https://github.com/hipe-eval/HIPE-OCRepair-scorer/blob/main/data/schema/hipe-ocrepair.schema.json)                                                                |
| **License** | [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/) |
| **Benchmark DOI** | [https://doi.org/10.5281/zenodo.18824344](https://doi.org/10.5281/zenodo.18824344) |
| **Segmentation Levels** | chunk, sentence, line                                                                                                                          |
| **Offset Format** | Character positions `[start, end]` in transcription_unit text                                                                                  |
| **Text Processing** | _To be completed_                                                                                                                              |
| **Line Breaks in Text** | _To be completed_                                                                                                                              |
| **Layout Preservation** | _To be completed_                                                                                                                              |
| **Data Splits** | Train, Dev, and Test                                                                                                           |
| **Split Strategy** | Each split contains a fix set of books (no book spanning several splits); first and last pages excluded; random sample. Test set pages manually curated to remove truncated sentences at page boundaries.                        |
| **Split Level** | page                                                                                                                           |
| **Quality Metrics** | CER, WER, OCR-QA score, alignment quality scores                                                                                               |
| **Image Links** | Not given for the competition                                                                                                                  |

### Dataset Statistics 

_to be completed_

| Split             |   Documents | Sentences | Paragraphs | Tokens (OCR) |  Characters (OCR) | Avg CER | Avg WER |
|:------------------|------------:|----------:|-----------:|-------------:|------------------:|--------:|--------:|
| **German Train**  |           - |         - |          - |            - |                 - |       - |       - |
| **German Dev**    |           - |         - |          - |            - |                 - |       - |       - |
| **German Test**   |           - |         - |          - |            - |                 - |       - |       - |
| **Total**         |           - |         - |          - |            - |                 - |       - |       - |


## 4. Known Issues and Considerations

- _To be completed if necessary_
