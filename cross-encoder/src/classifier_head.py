from torch import nn

"""
The final layer of the whole model
To be put on top of multi_head_cross_encoder.py

Take different scores calculated by multi_head_cross_encoder.py and return the final score
1. Author score
    - Trained using the given dataset
2. Style similarity score
    - Trained using another embedding model
"""


class ClassifierHead(nn.Module):
    def __int__(self):
        # TODO: To be removed
        pass
