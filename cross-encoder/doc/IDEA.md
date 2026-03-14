### This file contains ideas of cross-encoder architecture
##### Created by w45242hy


## Potential improvement
- ### Model architecture (MVP)
    - Segment Swap Consistency Loss
        - For the same pair (but different order), ```<pair_1>, <pair_2>``` vs ```<pair_2>, <pair_1>```, I expect to get the same prediction
        - Can train the model to do this by adjusting the loss function
            $$
            Loss_{consistency} = |p_1 - p_2|
            $$
    - Instead of 1 classifier after BERT, we have 3 models that give 3 scores, i.e. semantic similarity, style similarity, lexical overlap
        - We calculate a weighted final score based on the above 3 scores for our final prediction
        $$
        L = n_1 \times L_1 + n_2 \times L_2 + ...
        \\
        \text{Example: }
        \\
        L = L_{author_verification} + \lambda L_{style_prediction}
        $$
- ### Data preprocessing
    - Multi levels of granularity
        - Document-level
        - Paragraph-level
        - Sentence-level