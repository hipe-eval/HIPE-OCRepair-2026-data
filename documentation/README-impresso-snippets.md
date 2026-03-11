# Impresso Snippets OCR Post-Correction Dataset

**HIPE-OCRepair Benchmark identifier:** `impresso-snippets`  
**HIPE-OCRepair Benchmark version:** `v0.9`  
**Hugging Face:** <tocome>

The Impresso Snippets dataset consists of manually corrected OCR transcriptions of historical newspaper paragraphs extracted from digitized collections within the Impresso project (https://impresso-project.ch). The snippets are paragraph-level transcription units designed to capture complete contextual units while maintaining a manageable length of 9-15 lines.

The documents are sampled from various European newspaper collections spanning 1800-1959. Ground truth was created through manual correction by trained annotators with access to the original facsimiles (paragraph images with line segmentation), ensuring high-quality reference texts for OCR post-correction research.

## In a nutshell

| Property                        | Value                                                                                                                            |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------- |
| **Language(s)**                 | German (de), English (en), French (fr)                                                                                           |
| **OCR engine(s)**               | Various (from Impresso digitization pipeline)                                                                                    |
| **Total documents (benchmark)** | 180 (60 per language: 50 train, 10 dev); test set held back                                                                      |
| **Total tokens (benchmark)**    | ~16,000 tokens (across train + dev splits)                                                                                       |
| **Document granularity**        | paragraph (9-15 lines)                                                                                                           |
| **Segmentation level(s)**       | line (original), paragraphs from OLR/OCR with some heuristics (uppercase character at start); lines have been cut after 15 lines |
| **Data splits available**       | train and dev splits, test splits for benchmarking                                                                               |
| **Image linkage**               | Not available presently                                                                                                          |

### HIPE-OCRepair Benchmark Release Notes

- **Release v0.9**
  - Initial release with manually corrected impresso snippets across three languages.
  - JSONL format following the HIPE-OCRepair JSON schema.
  - Creation of splits (train/dev) for each language.
  - Inclusion of quality assurance metrics: OCR error rates (CER, WER).
  - Sentence segmentation (automatically computed, thus not perfect).
  - Preservation of line structure and hyphenation patterns.

## 1. Dataset Description

The Impresso Snippets dataset was created exclusively for the HIPE-OCRepair benchmark, consisting of manually corrected OCR transcriptions of historical newspaper paragraphs. The dataset is derived from the Impresso project's digitized newspaper collections, which include materials from various European archives and libraries spanning 1800-1959. Ground truth was created through manual correction by trained annotators with reference to paragraph images, ensuring high-quality reference texts for OCR post-correction research.

### Dataset Characteristics

| Property                 | Value                                                                                                                                                   |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Benchmark Name**       | `impresso-snippets`                                                                                                                                     |
| **Version**              | v1.0 (within Benchmark v0.9)                                                                                                                            |
| **Source**               | [Impresso Project](https://impresso-project.ch) - Historical newspaper collections                                                                      |
| **Release Date**         | 2025-2026                                                                                                                                               |
| **Language**             | German (de), English (en), French (fr)                                                                                                                  |
| **Document Type**        | Historical newspaper paragraphs                                                                                                                         |
| **Temporal Coverage**    | 1800-1959                                                                                                                                               |
| **OCR Engine**           | Various (Institutional digitization pipelines - includes Tesseract and other engines)                                                                   |
| **Document Granularity** | Paragraph (9-15 lines per snippet, 1 paragraph = 1 JSON document)                                                                                       |
| **Format**               | JSON Lines (.jsonl)                                                                                                                                     |
| **Schema**               | [benchmark_document_schema.json](https://github.com/hipe-eval/HIPE-OCRepair-scorer/blob/main/data/schema/hipe-ocrepair.schema.json)                     |
| **Character Encoding**   | UTF-8                                                                                                                                                   |
| **License**              | [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/) |
| **Metadata**             | Document ID, publication title, date, source filename                                                                                                   |
| **Ground Truth Source**  | Manual correction by trained annotators with reference to paragraph images                                                                              |
| **Font Types**           | Predominantly antiqua (roman type); some fraktur for German materials                                                                                   |
|                          |                                                                                                                                                         |
| **Segmentation Levels**  | line (original)                                                                                                                                         |
| **Offset Format**        | Character positions `[start, end]` in transcription_unit text                                                                                           |
|                          |                                                                                                                                                         |
| **Text Processing**      | Ligature normalization, whitespace normalization                                                                                                        |
| **Line Breaks in Text**  | **Preserved as `\n`** (original line structure maintained)                                                                                              |
| **Soft Hyphens**         | **Represented as `¬`** (U+00AC, NOT SIGN character) - may appear in OCR hypothesis                                                                      |
| **Hard Hyphens**         | **Represented as `-`** (U+002D, standard hyphen-minus) - predominant in OCR                                                                             |
| **Hyphenation**          | Soft hyphens may appear in OCR hypothesis; predominantly hard hyphens in practice; ground truth has soft hyphens                                        |
| **Layout Preservation**  | Yes - line breaks and hyphens preserved for layout information                                                                                          |
| **Paragraph Boundaries** | Snippets begin at real paragraph starts; end may be truncated due to 15-line limit                                                                      |
|                          |                                                                                                                                                         |
| **Data Splits**          | Train (50 paragraphs), Dev (10), Test (100) for each language (de, fr, en)                                                                              |
| **Split Strategy**       | Language-specific splits (not combined across languages)                                                                                                |
| **Split Level**          | Document-level (paragraphs not fragmented)                                                                                                              |
| **Test Set**             | Not included in public v0.9 release (reserved for evaluation)                                                                                           |
|                          |                                                                                                                                                         |
| **Quality Metrics**      | CER, WER, character-level edit operations (substitutions, deletions, insertions)                                                                        |
| **Image Links**          | Not available in current version                                                                                                                        |

## 2. Dataset Statistics

| Split/Language   | Documents | Lines | Sentences | Tokens (OCR) | Characters (OCR) | Avg CER | Avg WER |
| :--------------- | --------: | ----: | --------: | -----------: | ---------------: | ------: | ------: |
| **German (de)**  |           |       |           |              |                  |         |         |
| Train            |        50 |   577 |         - |        4,241 |           28,036 |  0.0431 |  0.2930 |
| Dev              |        10 |   109 |         - |          910 |            6,045 |  0.0460 |  0.3462 |
| **DE Total**     |    **60** |   686 |         - |        5,151 |           34,081 |  0.0437 |  0.3020 |
|                  |           |       |           |              |                  |         |         |
| **English (en)** |           |       |           |              |                  |         |         |
| Train            |        50 |   586 |         - |        4,771 |           27,662 |  0.0318 |  0.1270 |
| Dev              |        10 |   111 |         - |          885 |            5,144 |  0.0490 |  0.1955 |
| **EN Total**     |    **60** |   697 |         - |        5,656 |           32,806 |  0.0348 |  0.1378 |
|                  |           |       |           |              |                  |         |         |
| **French (fr)**  |           |       |           |              |                  |         |         |
| Train            |        50 |   550 |         - |        4,196 |           24,206 |  0.0351 |  0.2555 |
| Dev              |        10 |   111 |         - |          905 |            5,034 |  0.0292 |  0.2266 |
| **FR Total**     |    **60** |   661 |         - |        5,101 |           29,240 |  0.0341 |  0.2507 |
|                  |           |       |           |              |                  |         |         |
| **Grand Total**  |   **180** | 2,044 |         - |       15,908 |           96,127 |       - |       - |

_Note: Sentence segmentation was performed automatically but sentence offsets are not included in the current version._

## 3. Encoding Details

**Text Layout Preservation:**

- **Line breaks**: Preserved as `\n` in transcription_unit (maintains original line structure)
- **Soft hyphens** (line-break hyphens): Encoded as `¬` (U+00AC, NOT SIGN)
  - Example: `"Jour¬\nnal"` = soft hyphen at line break
  - **Note**: While soft hyphens may appear in OCR hypothesis, they are less common in this dataset; hard hyphens predominate
- **Hard hyphens** (lexical hyphens): Encoded as `-` (U+002D, HYPHEN-MINUS)
  - Example: `"co-operate"` = lexical compound word
- Layout information is preserved in the text for optional use

**Paragraph Structure:**

- **Start**: Snippets begin at genuine paragraph boundaries (not mid-paragraph cuts)
- **End**: May be truncated at 15-line maximum length constraint
  - Last line of snippet may not represent end of original paragraph
  - Length restriction (9-15 lines) prioritizes manageable transcription units

**Character Offsets:**

- All offsets `[start, end]` are character positions in the transcription_unit
- Line offsets: Mark original line boundaries (between `\n` positions)
- Sentence offsets: Not currently included (automatic segmentation performed but not exported)

## 4. Quality Profile and Usage Notes

### Quality Profile

The Impresso Snippets dataset exhibits relatively high OCR quality:

- **French**: Best quality (CER: 0.034, WER: 0.251)
- **English**: Very good quality (CER: 0.035, WER: 0.138)
- **German**: Good quality (CER: 0.044, WER: 0.302)

The higher German WER is partially due to fraktur font challenges and older OCR engines.

### For OCR Post-Correction Research

- **Paragraph-level context**: Each document provides 9-15 lines of continuous text
- **Layout awareness**: Original line breaks preserved for layout-aware models
- **Hyphenation**: Both soft and hard hyphens available for dehyphenation research
- **Language diversity**: Multilingual dataset enables cross-lingual experiments

### Limitations

- **Incomplete paragraphs**: Last line may be truncated (15-line maximum)
- **No images**: Paragraph images not included in current release

## 5. Citation and Acknowledgments

### Citation

If you use the Impresso Snippets dataset, please cite:

```bibtex
@dataset{impresso_snippets_2025,
  title = {Impresso Snippets OCR Post-Correction Dataset},
  author = {{Impresso Project Team}},
  year = {2025},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.18822569},
  url = {https://doi.org/10.5281/zenodo.18822569},
  note = {Part of HIPE-OCRepair Benchmark v0.9}
}
```

### Acknowledgments

This dataset was created as part of the Impresso project ("Media Monitoring of the Past"), which is funded by the Swiss National Science Foundation (SNSF) under grants CRSII5_173719 and CRSII5_213585.

The Impresso project develops tools and methods for processing and exploring digitized historical newspaper collections. For more information, visit: https://impresso-project.ch

### Related Resources

- **Impresso Interface**: https://impresso-project.ch/app
- **Impresso GitHub**: https://github.com/impresso
- **HIPE-OCRepair Benchmark**: https://github.com/hipe-eval/HIPE-OCRepair-scorer
