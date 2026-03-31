---
{}
---
language: en
license: cc-by-4.0
tags:
- text-classification
repo: https://github.com/Toothless7788/COMP34812-nlu-coursework

---

# Model Card for u14554as-w45242hy-AV

<!-- Provide a quick summary of what the model is/does. -->

This is a Siamese LSTM model that employs a multi-modal late-fusion approach to detect whether two pieces of text were written by the same author.


## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

The model uses a Siamese architecture with two primary branches:
 - **Semantics**: A 3-layer bidirectional LSTM with attention pooling that processes FastText-embedded tokens to capture the author's semantics
 - **Stylometry**: A dense feed-forward network that processes the absolute difference between both texts for 203 hand-crafted features such as type-token ratio, OOV rates, pronoun analysis, mean word/sentence lengths, common POS trigrams and the top 30 function words (among others)

Through extensive random search, the optimal semantic feature configuration was found to be [u, v, |u - v|] (where u and v are the semantic embeddings of the two texts), which corroborates the findings of the SBERT paper[^1]. Subsequently, semantic features are combined with stylometric features. Finally, a classification head outputs one raw logit to be passed to the BCEWithLogitsLoss objective function.

- **Developed by:** Abdullah Sweesi and Hin Yui Jacob Yip
- **Language(s):** English
- **Model type:** Supervised
- **Model architecture:** Siamese LSTM
- **Finetuned from model [optional]:** N/A

### Model Resources

<!-- Provide links where applicable. -->

- **Repository:** N/A
- **Paper or documentation:** See project README

## Training Details

### Training Data

<!-- This is a short stub of information on the training data that was used, and documentation related to data pre-processing or additional filtering (if applicable). -->

Trained on over 27K pairs of text provided as part of the AV training set.

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Training Hyperparameters

<!-- This is a summary of the values of hyperparameters used in training the model. -->

| Hyperparameter | Search Space | Final Value |
| -------------- | ------------ | ----------- |
| LSTM layers | [1, 2, 3] | 3 |
| Semantic dimensionality | [64, 128, 256] | 64 |
| Stylometric dimensionality | [64, 128, 256] | 128 |
| Dropout | [0.3, 0.4, 0.5] | 0.4 |
| Learning rate | [2e-4, 5e-4] | 5e-4 |
| Weight decay | [0, 1e-5, 1e-4] | 1e-4 |
| Batch size | [64, 128] | 128 |

Note:
- Batch size was large (64, 128) to make the best use of the double T4 GPUs during training and evaluation
- The maximum number of epochs was 25, with early stopping at patience 3
- The optimizer was Adam

#### Speeds, Sizes, Times

<!-- This section provides information about how roughly how long it takes to train the model and the size of the resulting model. -->


      - overall training time: 30-45 minutes
      - duration per training epoch: 60-90s
      - model size: 80MB

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data & Metrics

#### Testing Data

<!-- This should describe any evaluation data used (e.g., the development/validation set provided). -->

Evaluated on about 6K pairs of text provided as part of the AV development set.

#### Metrics

<!-- These are the evaluation metrics being used. -->


      - Accuracy
      - Macro-F1
      - Matthews Correlation Coefficient
      

### Results

The model obtained an accuracy of 0.738, a macro-precision of 0.738, and a Matthews Correlation Coefficient of 0.476.
| Metric | Score |
| ------ | ----- |
| Accuracy | 0.7380 |
| Macro Precision | 0.7380 |
| Macro Recall | 0.7380 |
| Macro F1 | 0.7380 |
| Weighted Macro Precision | 0.7382 |
| Weighted Macro Recall | 0.7380 |
| Weighted Macro F1 | 0.7381 |
| Matthews Correlation Coefficient | 0.4761 |


## Technical Specifications

### Hardware


      - RAM: at least 8 GB
      - Storage: at least 2.5GB
      - GPU: T4 * 2

### Software


      - Pytorch 2.10.0+cu128
      - Spacy 3.8.11
      - NLTK 3.9.1
      - scikit-learn 1.6.1
      - joblib 1.5.3
      

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

- Texts were padded/truncated to be exactly 256 tokens
- The vocabulary was limited to 50,000 words
- Specifically trained on prose; requires further training for more technical documents
- Restricted to English

## Additional Information

<!-- Any other information that would be useful for other people to know. -->

The hyperparameters were tuned via random search through a hyperparameter grid.


[^1]: Reimers, N. and Gurevych, I., 2019, November. Sentence-BERT: Sentence embeddings using Siamese BERT-Networks. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) (pp. 3982-3992).
