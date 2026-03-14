import pandas as pd
import torch
from torch.utils.data import Dataset


class AVDataset(Dataset):
    def __init__(self, csv_file: str, text_1_column="text_1", text_2_column="text_2", label_column="label", separation_token="[SEP]"):
        # Load CSV
        self.df = pd.read_csv(csv_file)

        # Columns
        self.text_1 = self.df[text_1_column].astype(str).tolist()
        self.text_2 = self.df[text_2_column].astype(str).tolist()
        self.label = self.df[label_column].astype(float).tolist()

        self.separation_token = separation_token

        # Sanity check
        assert len(self.text_1) == len(self.label) and len(self.text_2) == len(
            self.label), f"Mismatch between lengths: text_1={len(self.text_1)}, text_2={len(self.text_2)}, author_score={len(self.label)}"

    def __len__(self):
        return len(self.label)

    def __getitem__(self, idx):
        # Original: Deprecated
        # Combine text_1 and text_2 with a separator
        # combined_text = f"{self.text_1[idx]} {self.separation_token} {self.text_2[idx]}"
        # Current: Return a tuple instead
        combined_text = (self.text_1[idx], self.text_2[idx])
        label = torch.tensor(self.label[idx], dtype=torch.float)

        return (combined_text, label)
