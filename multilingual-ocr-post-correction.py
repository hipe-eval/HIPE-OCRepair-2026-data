import json
import os
import datasets
from datasets import BuilderConfig


class OCRPostCorrectionConfig(datasets.BuilderConfig):
    """BuilderConfig for OCRPostCorrection datasets."""

    def __init__(self, dataset="icdar2017", language="en", **kwargs):
        super(OCRPostCorrectionConfig, self).__init__(**kwargs)
        self.dataset = dataset
        self.language = language


class MultilingualOCRPostCorrection(datasets.GeneratorBasedBuilder):
    VERSION = datasets.Version("1.0.0")
    BUILDER_CONFIG_CLASS = OCRPostCorrectionConfig
    BUILDER_CONFIGS = [
        OCRPostCorrectionConfig(
            name="impresso-nzz-de",
            dataset="impresso-nzz",
            language="de",
            version=datasets.Version("1.0.0"),
            description="Impresso NZZ German"
        ),

        OCRPostCorrectionConfig(
            name="icdar2017-en",
            dataset="icdar2017",
            language="en",
            version=datasets.Version("1.0.0"),
            description="ICDAR 2017 English"
        ),

        OCRPostCorrectionConfig(
            name="icdar2017-en",
            dataset="icdar2017",
            language="en",
            version=datasets.Version("1.0.0"),
            description="ICDAR 2017 English"
        ),
        OCRPostCorrectionConfig(
            name="overproof-en",
            dataset="overproof",
            language="en",
            version=datasets.Version("1.0.0"),
            description="Overproof English"
        ),
    ]
    VERSION = datasets.Version("1.0.0")
    BUILDER_CONFIG_CLASS = OCRPostCorrectionConfig

    def _info(self):
        return datasets.DatasetInfo(
            description="Multilingual OCR Post-Correction Benchmark",
            features=datasets.Features({
                "document_metadata": datasets.features.Features({
                    "document_id": datasets.Value("string"),
                    "primary_dataset_name": datasets.Value("string"),
                    "primary_dataset_filename": datasets.Value("string"),
                    "primary_dataset_doi": datasets.Value("string"),
                    "primary_dataset_version": datasets.Value("string"),
                    "primary_dataset_license": datasets.Value("string"),
                    "benchmark_dataset_name": datasets.Value("string"),
                    "benchmark_dataset_split": datasets.Value("string"),
                    "document_type": datasets.Value("string"),
                    "date": datasets.Value("string"),
                    "language": datasets.Value("string"),
                    "publication_title": datasets.Value("string"),
                    "transcription_unit_scope": datasets.Value("string"),
                    "segmentation_origin_article": datasets.Value("string"),
                    "segmentation_origin_lines": datasets.Value("string"),
                    "segmentation_origin_sentences": datasets.Value("string"),
                    "segmentation_origin_paragraphs": datasets.Value("string"),
                    "img_support_transcription_unit_iiif_url": datasets.Value("string"),
                    "img_support_transcription_unit_img_filepath": datasets.Value("string"),
                }),
                "ground_truth": datasets.features.Features({
                    "transcription_unit": datasets.Value("string"),
                    "line_offsets": datasets.Sequence(datasets.Value("int32")),
                    "sentence_offsets": datasets.Sequence(datasets.Sequence(datasets.Value("int32"))),
                    "paragraph_offsets": datasets.Sequence(datasets.Sequence(datasets.Value("int32"))),
                    "num_tokens": datasets.Value("int32"),
                    "num_chars": datasets.Value("int32"),
                    "quality_report": datasets.features.Features({
                        "ocr_quality_score": datasets.Value("float"),
                    }),
                }),
                "ocr_hypothesis": datasets.features.Features({
                    "transcription_unit": datasets.Value("string"),
                    "sentence_offsets": datasets.Sequence(datasets.Sequence(datasets.Value("int32"))),
                    "paragraph_offsets": datasets.Sequence(datasets.Sequence(datasets.Value("int32"))),
                    "num_tokens": datasets.Value("int32"),
                    "num_chars": datasets.Value("int32"),
                    "quality_report": datasets.features.Features({
                        "ocr_quality_score": datasets.Value("float"),
                        "cer": datasets.Value("float"),
                        "wer": datasets.Value("float"),
                    }),
                }),
                "ocr_postcorrection_output": datasets.features.Features({
                    "transcription_unit": datasets.Value("string"),
                    "ocr_postcorrection_system": datasets.Value("string"),
                    "num_tokens": datasets.Value("int32"),
                    "num_chars": datasets.Value("int32"),
                    "quality_report": datasets.features.Features({
                        "ocr_quality_score": datasets.Value("float"),
                        "cer": datasets.Value("float"),
                        "wer": datasets.Value("float"),
                    }),
                }),
            }),
        )

    def _split_generators(self, dl_manager):
        dataset = self.config.dataset
        lang = self.config.language
        split = "test"
        print(self.config)

        filename = f"data/{dataset}/{lang}/impresso-ocr-benchmark-{dataset}-{split}-{lang}.jsonl"
        data_path = dl_manager.download_and_extract(filename)

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={"filepath": data_path},
            ),
        ]

    def _generate_examples(self, filepath):
        with open(filepath, encoding="utf-8") as f:
            for idx, line in enumerate(f):
                yield idx, json.loads(line)
