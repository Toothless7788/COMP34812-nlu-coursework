import pandas as pd
import torch
from torch.utils.data import Dataset


class FinalAVDataset(Dataset):
    def __init__(self, csv_file: str, text_1_column="text_1", text_2_column="text_2", author_score_column="author_score", style_similarity_score_column="style_similarity_score", separation_token="[SEP]"):
        # Load CSV
        self.df = pd.read_csv(csv_file)

        # Columns
        self.text_1 = self.df[text_1_column].astype(str).tolist()
        self.text_2 = self.df[text_2_column].astype(str).tolist()
        self.author_score = self.df[author_score_column].astype(float).tolist()
        self.style_similarity_score = self.df[style_similarity_score_column].astype(
            float).tolist()

        self.separation_token = separation_token

        # Sanity check
        assert len(self.text_1) == len(self.author_score) and len(self.text_2) == len(self.author_score) and len(self.style_similarity_score) == len(
            self.author_score), f"Mismatch between lengths: text_1={len(self.text_1)}, text_2={len(self.text_2)}, author_score={len(self.author_score)}, style_similarity_score={len(self.style_similarity_score)}"

    def __len__(self):
        return len(self.author_score)

    def __getitem__(self, idx):
        # Original: Deprecated
        # Combine text_1 and text_2 with a separator
        # combined_text = f"{self.text_1[idx]} {self.separation_token} {self.text_2[idx]}"
        # Current: Return a tuple instead
        combined_text = (self.text_1[idx], self.text_2[idx])
        author_score = torch.tensor(self.author_score[idx], dtype=torch.float)
        style_similarity_score = torch.tensor(
            self.style_similarity_score[idx], dtype=torch.float)

        return (combined_text, author_score, style_similarity_score)
