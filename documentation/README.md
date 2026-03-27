# HIPE-OCRepair Benchmark - Dataset Documentation

This folder contains documentation for the **datasets** included in the **Impresso HIPE-OCRepair Benchmark** for OCR post-correction of historical documents. Each dataset has its own dedicated README serving as a data card with information about origin, processing, and benchmark characteristics.

## Available Datasets

* [ICDAR-2017 Dataset](README-icdar-2017.md) - Historical newspapers from BnF and British Library (English, French)
* [Overproof Dataset](README-overproof.md) - Sydney Morning Herald and Chronicling America articles (English)
* [Impresso NZZ Dataset](README-impresso-nzz.md) - Neue Zürcher Zeitung with Black Letter font (German)
* [Impresso Snippets Dataset](README-impresso-snippets.md) - Curated newspaper snippets from Impresso corpus (Multilingual)
* [dta19](README-dta19.md) - Pages from German books (18-19C).

## Data Card Contents

Each dataset documentation includes:

* **Release Notes**: Version history and changes
* **In a nutshell**: Quick overview table with key properties (language, OCR engine, document count, granularity, segmentation levels, splits)
* **Original Dataset**: Description of the source dataset, publication reference, format, and characteristics
* **Benchmark Version**: Processing pipeline, conversions, quality metrics, and curation details
* **Dataset Statistics**: Document counts, tokens, characters, and quality metrics per split
* **Encoding Details**: Text layout preservation, normalization strategies, offset formats, alignment scores
* **Known Issues**: Limitations and considerations for using the dataset

## Benchmark Overview

The HIPE-OCRepair benchmark standardizes diverse historical OCR datasets into a unified format with:
- Consistent JSON schema
- Multiple segmentation levels (document, paragraph, sentence, line)
- Quality metrics (CER, WER, alignment scores, OCR-QA)
- Train/dev/test splits for evaluation
- Layout information preservation where available

For more information about the benchmark pipeline and conversion process, see the main data conversion repository [README] (public after the competition).
