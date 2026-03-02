# Overproof OCR Post-Correction Dataset

**HIPE-OCRepair Benchmark identifier:** `overproof`  
**HIPE-OCRepair Benchmark version:** `v0.9`    
**Hugging Face:** <tocome>
 
The Overproof datasets were originally released in the context of OCR quality evaluation. They were extracted from digitised historical newspaper collections held by the National Library of Australia (Trove) and Chronicling America (Library of Congress).

The documents correspond to newspaper articles, for which OCR transcriptions are aligned with ground truth (GT) at the line level. The original ground truth was generated through crowdsourced corrections by users of the Trove platform (thus with varying completeness and consistency).

For inclusion in the Impresso HIPE-OCRepair benchmark, the corpus underwent additional processing and curation. The benchmark version comprises Overproof Dataset 2 and Dataset 3.

## In a nutshell

| Property | Value                                                                                        |
|:----------|:---------------------------------------------------------------------------------------------|
| **Language(s)** | English                                                                                      |
| **OCR engine(s)** | ABBYY                                                                                        |
| **Total documents (benchmark)** | 208                                                                                          |
| **Total tokens (benchmark)** | _updated after competition_                                                                  |
| **Document granularity** | article                                                                                      |
| **Segmentation level(s)** | sentence (auto), line (original)                                                             |
| **Data splits available** | train, dev and test splits newly created over both SMH and CA (test not part of competition) |
| **Image linkage** | Not available presently                                                                      |


### HIPE-OCRepair Benchmark Release Notes

- **Release v0.9**
    - Initial release with curated and converted Overproof Dataset 2 and Dataset 3.
    - Exclusion of Dataset 1 due to unreliable ground truth.
    - JSONL format following the HIPE-OCRepair JSON schema.
    - Creation of splits (train/dev/test) stratified by CER quality.
    - Inclusion of quality assurance metrics: ocr error rates (CER, WER) and alignment quality scores.
    - Manual checking of ground truth
    - Sentence segmentation (automatically thus not perfect)

## 1. Original Datasets

- **Dataset 1 (SMH)**: Sydney Morning Herald (1842-1954) from Trove, National Library of Australia  
- **Dataset 2 (SMH)**: Sydney Morning Herald (1842-1954) from Trove, National Library of Australia  
- **Dataset 3 (CA)**: Chronicling America (19th-20th century) from Library of Congress, U.S.

**Note**: Dataset 1 was excluded from the HIPE-OCRepair benchmark due to poor ground truth quality.

### Key Characteristics (original)

| Property | Value |
|:---------|:------|
| **Source** | [Overproof OCR Correction Dataset](https://overproof.projectcomputing.com/evaluation) |
| **Publication** | Evershed & Fitch (2014). [Correcting noisy OCR: context beats confusion](https://dl.acm.org/doi/10.1145/2595188.2595200). DATeCH '14. |
| **Release Date** | ca. 2013 |
| **Language** | English |
| **Document Type** | Historical newspaper articles |
| **Temporal Coverage** | 19th–20th century |
| **OCR Engine** | ABBYY |
| **Original Format** | Plain text (.txt) - one file per dataset with all articles |
| **Alignment Level** | Line-by-line (format: `OCR\|\|@@\|\|overproof_correction\|\|@@\|\|manual_correction`) |
| **Line Break Encoding** | Implicit (one line per .txt line) |
| **Character Encoding** | UTF-8 |
| **License** | Not explicitly stated; likely public domain (pre-1923 US, pre-1954 AU publications) |
| **Metadata** | Article title, year, document ID (embedded in delimiter lines) |
| **Ground Truth Source** | Dataset 2: Crowd-sourced (Trove) + manual verification <br> Dataset 3: Manual correction with reference to page images |
| **Original Data Splits** | None provided |
| **Image Access** | Possible from original sources (Trove, Chronicling America) but not included in dataset |


## 2. Benchmark Version

For the Impresso HIPE-OCRepair benchmark, the original Overproof dataset was **manually re-curated** and converted to structured JSON format with enhanced segmentation and quality metrics.

| Property | Value                                                                                                                                                                                                                                                             |
|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Benchmark Name** | `overproof`                                                                                                                                                                                                                                                       |
| **Version** | v1.0 (within Benchmark v0.9)                                                                                                                                                                                                                                      |
| **Components** | SMH (Sydney Morning Herald), CA (Chronicling America)                                                                                                                                                                                                             |
| **Exclusions** | Dataset 1 excluded due to inconsistent ground truth quality                                                                                                                                                                                                       |
| **Language** | English                                                                                                                                                                                                                                                           |
| **Document Granularity** | Article (1 article = 1 JSON document)                                                                                                                                                                                                                             |
| **Format** | JSON Lines (.jsonl)                                                                                                                                                                                                                                               |
| **Schema** | [benchmark_document_schema.json](https://github.com/hipe-eval/HIPE-OCRepair-scorer/blob/main/data/schema/hipe-ocrepair.schema.json)                                                                                                                               |
| **License** | [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) <br> *(Applies to structured format and annotations; underlying newspaper content remains public domain)* |
| |                                                                                                                                                                                                                                                                   |
| **Segmentation Levels** | article (original), line (original), sentence (SpaCy)                                                                                                                                                                                                             |
| **Offset Format** | Character positions `[start, end]` in transcription_unit text                                                                                                                                                                                                     |
| |                                                                                                                                                                                                                                                                   |
| **Text Processing** | Ligature normalization, whitespace normalization                                                                                                                                                                                                                  |
| **Line Breaks in Text** | **Preserved as `\n`** (original line structure kept)                                                                                                                                                                                                              |
| **Soft Hyphens** | **Represented as `¬`** (U+00AC, NOT SIGN character)                                                                                                                                                                                                               |
| **Hard Hyphens** | **Represented as `-`** (U+002D, standard hyphen-minus)                                                                                                                                                                                                            |
| **Layout Preservation** | Yes - line breaks and hyphens preserved for layout information                                                                                                                                                                                                    |
| |                                                                                                                                                                                                                                                                   |
| **Data Splits** | Train (70%), Dev (15%), Test (15%)                                                                                                                                                                                                                                |
| **Split Strategy** | Stratified by CER quality across combined SMH+CA corpus                                                                                                                                                                                                           |
| **Split Level** | Document-level (articles not fragmented)                                                                                                                                                                                                                          |
| |                                                                                                                                                                                                                                                                   |
| **Quality Metrics** | CER, WER, OCR-QA score, alignment quality scores                                                                                                                                                                                                                  |
| **Alignment Quality Categories** | Good (>0.9), Soft (>0.6), Wrong (<0.6) - internal usage, not for competition                                                                                                                                                                                      |
| **Image Links** | Not available in current version                                                                                                                                                                                                                                  |

### Dataset Statistics

| Split        | Documents |  Lines | Sentences | Chunks | Tokens (OCR) | Characters (OCR) | Avg CER | Avg WER |
|:-------------|----------:|-------:|----------:|-------:|-------------:|-----------------:|--------:|--------:|
| SMH (all)    |       159 |  7,624 |     2,930 |      - |       88,895 |          309,309 |  0.0829 |  0.2980 |
| CA (all)     |        49 |  3,209 |       918 |      - |       29,683 |          108,337 |  0.0902 |  0.3290 |
|              |           |        |           |        |              |                  |         |         |
| **Train**    |       146 |  7,377 |     2,575 |      - |       41,993 |          285,051 |  0.0836 |  0.3001 |
| **Dev**      |        30 |  1,759 |       643 |      - |        9,318 |           63,988 |  0.0870 |  0.3444 |
| **Test**     |        32 |  1,697 |       630 |      - |       10,309 |           68,866 |  0.0878 |  0.2969 |
| **Total**    |       208 | 10,833 |     3,848 |      - |       62,082 |          417,646 |       - |       - |


### Encoding Details

**Text Layout Preservation:**
- **Line breaks**: Preserved as `\n` in transcription_unit (maintains original line structure)
- **Soft hyphens** (line-break hyphens): Encoded as `¬` (U+00AC, NOT SIGN)
  - Example: `"Jour¬\nnal"` = soft hyphen at line break
- **Hard hyphens** (lexical hyphens): Encoded as `-` (U+002D, HYPHEN-MINUS)
  - Example: `"co-operate"` = lexical compound word
- Layout information is preserved in the text for optional use

**Character Offsets:**
- All offsets `[start, end]` are character positions in the transcription_unit
- Line offsets: Mark original line boundaries (between `\n` positions)
- Sentence offsets: Computed automatically (SpaCy) on text with layout characters


