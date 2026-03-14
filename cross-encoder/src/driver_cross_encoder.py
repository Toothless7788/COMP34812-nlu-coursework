from multi_head_cross_encoder import MultiHeadCrossEncoder
import torch
from transformers import AutoTokenizer


"""
The driver program for testing
"""

INPUT_DATA = [
    ("Hello World", "Byte world"),
    ("Yippy", "Bruh"),
]
HEAD_WEIGHTS = [0.3, 0.7]
ENCODER_NAME = f"bert-base-uncased"

if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained(ENCODER_NAME)
    encoding = tokenizer(
        [t[0] for t in INPUT_DATA],
        [t[1] for t in INPUT_DATA],
        padding=True,
        truncation=True,
        return_tensors="pt"
    )

    model = MultiHeadCrossEncoder(
        model_name=ENCODER_NAME,
        head_weights=HEAD_WEIGHTS
    )

    model.eval()

    with torch.no_grad():
        outputs = model(
            input_ids=encoding["input_ids"],
            attention_mask=encoding["attention_mask"]
        )

    print(f"Outputs: {outputs}")

    print(f"driver_cross_encoder.py finishes running ...")
