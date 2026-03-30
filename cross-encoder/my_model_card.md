---
{}
---
language: en
license: cc-by-4.0
tags:
- text-classification
repo: https://github.com/Toothless7788/COMP34812-nlu-coursework

---

# Model Card for w45242hy-username2-track_abbreviation

<!-- Provide a quick summary of what the model is/does. -->

This is a classification model that was trained to
      detect whether two pieces of text were written by the same author. 
      Its inputs are expected to be two strings, each representing the target piece of text. 
      Its output is expected to be a label with ```1``` predicting the given two pieces of text belong to the same author, ```0``` otherwise. 


## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

This model is based upon a BERT model that was fine-tuned
      on 30K pairs of texts. It consists of two parts, a cross-encoder and a multi-head decoder. 

      In the cross-encoder architecture, both texts are simultaneously fed through a transformer network. In this architecture, a single encoding for both texts is used for classification. Cross-encoders are normally used when there is a pre-defined set of text pairs to be scored. The truncation is done by the tokenizer. Cross-encoders usually outperform bi-encoders but do not scale well when the dataset is large. Given that the training dataset only has 30K pairs of text, this makes cross-encoders suitable for this task. 

      In the multi-head decoder, predictions are made based on sub-predictions from three heads. Predictions of each head are based on different aspects of the two given pieces of text. The first head aims at deciding whether the two pieces of text ... TODO: Update here next
      

- **Developed by:** Hin Yui Jacob Yip and Firstname2 Lastname2
- **Language(s):** English
- **Model type:** Supervised
- **Model architecture:** Transformers
- **Finetuned from model [optional]:** bert-base-uncased

### Model Resources

<!-- Provide links where applicable. -->

- **Repository:** https://huggingface.co/google-bert/bert-base-uncased
- **Paper or documentation:** [https://ceur-ws.org/Vol-3180/paper-206.pdf](https://ceur-ws.org/Vol-3180/paper-206.pdf)
- **Paper or documentation:**: [https://sbert.net/examples/cross_encoder/applications/README.html](https://sbert.net/examples/cross_encoder/applications/README.html)

## Training Details

### Training Data

<!-- This is a short stub of information on the training data that was used, and documentation related to data pre-processing or additional filtering (if applicable). -->

30K pairs of texts drawn from emails, news articles and blog posts.

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Training Hyperparameters

<!-- This is a summary of the values of hyperparameters used in training the model. -->


      - learning_rate: 2e-05
      - train_batch_size: 16
      - eval_batch_size: 16
      - seed: 42
      - num_epochs: 10

#### Speeds, Sizes, Times

<!-- This section provides information about how roughly how long it takes to train the model and the size of the resulting model. -->


      - overall training time: 5 hours
      - duration per training epoch: 30 minutes
      - model size: 300MB

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data & Metrics

#### Testing Data

<!-- This should describe any evaluation data used (e.g., the development/validation set provided). -->

A subset of the development set provided, amounting to 2K pairs.

#### Metrics

<!-- These are the evaluation metrics being used. -->


      - Precision
      - Recall
      - F1-score
      - Accuracy

### Results

The model obtained an F1-score of 67% and an accuracy of 70%.

## Technical Specifications

### Hardware


      - RAM: at least 16 GB
      - Storage: at least 2GB,
      - GPU: V100

### Software


      - Transformers 4.18.0
      - Pytorch 1.11.0+cu113

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

Any inputs (concatenation of two sequences) longer than
      512 subwords will be truncated by the model.

## Additional Information

<!-- Any other information that would be useful for other people to know. -->

The hyperparameters were determined by experimentation
      with different values.
