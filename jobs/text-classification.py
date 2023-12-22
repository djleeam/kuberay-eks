from typing import Dict

import numpy as np
from transformers import pipeline

import ray

class TextClassifier:
    def __init__(self):

        self.model = pipeline("text-classification")

    def __call__(self, batch: Dict[str, np.ndarray]) -> Dict[str, list]:
        predictions = self.model(list(batch["text"]))
        batch["label"] = [prediction["label"] for prediction in predictions]
        return batch

ds = (
    ray.data.read_text("s3://anonymous@ray-example-data/this.txt")
    .map_batches(TextClassifier, concurrency=2)
)

ds.show(3)