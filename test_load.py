from datasets import load_dataset
from pprint import pprint

# dataset = load_dataset(
#     "impresso-project/multilingual-ocr-post-correction",
#     dataset="icdar2017",
#     language="en",
#     split="test"
# )
# pprint(dataset[0])
dataset = load_dataset("impresso-project/multilingual-ocr-post-correction", name="impresso-nzz-de", split="test")

pprint(dataset[0])
