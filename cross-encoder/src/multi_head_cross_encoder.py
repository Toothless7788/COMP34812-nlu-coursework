import torch
from torch import nn, functional as F
from transformers import AutoModel

"""
Return different scores, which will be used to determine the final score in the task of Author Verification
"""


class MultiHeadCrossEncoder(nn.Module):
    model_name: str
    head_weights: torch.Tensor

    def __init__(self, model_name: str, head_weights: torch.Tensor):
        super().__init__()

        self.encoder = AutoModel.from_pretrained(model_name)

        encoder_hidden_size = self.encoder.config.hidden_size

        self.shared = nn.Linear(encoder_hidden_size, encoder_hidden_size)
        self.shared_activation = nn.ReLU()

        self.head_author = nn.Linear(encoder_hidden_size, 1)
        self.head_style_similarity = nn.Linear(encoder_hidden_size, 1)

        assert isinstance(
            head_weights, torch.Tensor), f"Invalid type of head_weights: {type(head_weights)}"
        assert head_weights.dim() == 1 and head_weights.numel(
        ) == 2, f"Invalid shape of head_weights (expect [2]): {head_weights.shape}"

        if sum(head_weights) == 1:
            self.head_weights = head_weights
        else:
            # Apply softmax function
            self.head_weights = F.softmax(head_weights, dim=0)

    def forward(self, input_ids, attention_mask):
        encoder_outputs = self.encoder(
            input_ids=input_ids,
            attention_mask=attention_mask
        )

        embedding_cls = encoder_outputs.last_hidden_state[:, 0]

        shared_output = self.shared_activation(self.shared(embedding_cls))

        # Individual heads
        score_author = self.head_author(shared_output)
        score_style_similarity = self.head_style_similarity(shared_output)

        score_final = (
            score_author * self.head_weights[0]) + (score_style_similarity * self.head_weights[1])

        return {
            f"score_final": score_final,
            f"score_author": score_author,
            f"score_style_similarity": score_style_similarity
        }
