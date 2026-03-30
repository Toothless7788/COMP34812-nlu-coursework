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

This is a classification model that was trained to detect whether two pieces of text were written by the same author. 
Its inputs are expected to be two strings, each representing the target piece of text. 
Its output is expected to be a label with ```1``` predicting the given two pieces of text belong to the same author, ```0``` otherwise. 


## Model Details

### Model Description
<!-- Provide a longer summary of what this model is. -->
This model is based upon a BERT model that was fine-tuned on 30K pairs of texts. It consists of two parts, a cross-encoder and a multi-head decoder. 

In the cross-encoder architecture, both texts are simultaneously fed through a transformer network. 

In this architecture, a single encoding for both texts is used for classification. Cross-encoders are normally used when there is a pre-defined set of text pairs to be scored. The truncation is done by the tokenizer. Cross-encoders usually outperform bi-encoders but do not scale well when the dataset is large. Given that the training dataset only has 30K pairs of text, this makes cross-encoders suitable for this task. 

In the multi-head decoder, predictions are made based on sub-predictions from three heads. Predictions of each head are based on different aspects of the two given pieces of text. Before passing the embeddings to the three heads, they are first passed to a linear layer to extract shared features. This ensures the three heads do not generate predictions independently, but rather work on shared features to give the final prediction. The first head aims at deciding whether the two pieces of text belongs to the same author primarily. However, there might be other aspects that this head is not sufficient to take into account. Thus, a second head is added which targets at comparing the style similarities between the writing styles of the two pieces of text. The two pieces of text are converted to two embedding vectors using a transformer and a similarity score is created using cosine similarity. This score is one of the inputs of the decoder. A third head is added, which focuses heavility on the difference between stylometric features of the two pieces of text. Such embedding vector is represented by $171$ features, which is then passed to the decoder directly. The final prediction is a weighted prediction of all predictions from all heads. The weight of each head can be customised, which is a hyperparameter tuned in hyperparameter selection. 
      

- **Developed by:** Hin Yui Jacob Yip and Firstname2 Lastname2
- **Language(s):** English
- **Model type:** Supervised
- **Model architecture:** Transformers
- **Finetuned from model [optional]:** bert-base-uncased

### Model Resources
<!-- Provide links where applicable. -->
- **Repository:** [Link to BERT model used](https://huggingface.co/google-bert/bert-base-uncased)
- **Paper:** [Paper explaining why a cross-encoder is chosen for this task](https://ceur-ws.org/Vol-3180/paper-206.pdf)
- **Documentation:**: [Website explaining what a cross-encoder is](https://sbert.net/examples/cross_encoder/applications/README.html)


## Training Details

### Training Data
<!-- This is a short stub of information on the training data that was used, and documentation related to data pre-processing or additional filtering (if applicable). -->
- 30K pairs of texts drawn from emails, news articles and blog posts. 
- There are mainly two data pre-processing steps: both compute the similarity between the two pieces of text. 

#### 1. Similarity Score
- The two pieces of text are converted to embedding vectors using ```SentenceTransformer``` from ```sentence_transformers```. The similarity of the two vectors are then compared using cosine similarity to compute a similarity score. This score is then outputted to an external csv file with column "style_similarity_score", which is an input passed to the tokenizer and then the first head of the decoder. 

#### 2. Similarity Vector
- An embedding vector is created for each pair of text piece. The stylometric features of each of the text piece are first extracted and they are then compared. Their difference is represented by an embedding vector, which is then outputted to a separate csv file. There are $171$ columns in this csv file, each representing 1 feature. This csv file is then read again during training, validation and evaluation, and the embedding vector is passed to the third head of the decoder directly. 

### Training Procedure
<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->
- In addition to ```train.csv```, the model also requires two additional files for training. As mentioned in Sections [Similarity Score](#1-similarity-score) and [Similarity Vector](#2-similarity-vector), the model inputs require more than just the two pieces of text. Thus, before trianing, the corresponding customised csv files of the above data are generated, which are then later generated and combined with input data in ```train.csv```. 
- The training consists of ```n``` epochs, where ```n``` is a hyperparameter selected by developers (refer to Section [Training Hyperparameters](#training-hyperparameters)). In each training loop, the input data are first moved to the correct device, e.g. cuda GPU. They are then passed to the model to generate a prediction. Binary Cross-Entropy Loss is used to compute the loss of each individual heads and also the combined loss. In PyTorch, ```BCEWithLogitsLoss``` is used. Note that the combined loss takes into account different weights of heads in calculation (refer to Section [Metrics](#metrics) for the complete formula). Backpropagation is then applied to update the fine tune the BERT (the encoder) and also the three heads (decoder). 

#### Training Hyperparameters
<!-- This is a summary of the values of hyperparameters used in training the model. -->
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: N/A
- num_epochs: 3
      - After hyperparameter selection

#### Speeds, Sizes, Times
<!-- This section provides information about how roughly how long it takes to train the model and the size of the resulting model. -->
- overall training time: 3 hours
- duration per training epoch: 50 minutes
- model size: 400MB


## Evaluation
<!-- This section describes the evaluation protocols and provides the results. -->
- In addition to using the self-implemented TODO: Update here next

### Testing Data & Metrics

#### Testing Data
<!-- This should describe any evaluation data used (e.g., the development/validation set provided). -->
- A subset of the development set provided, amounting to 2K pairs. 
- TODO: Update

#### Metrics
<!-- These are the evaluation metrics being used. -->
- Precision
- Recall
- F1-score
- Accuracy
- Binary Cross-Entropy Loss for each head
      - PyTorch BCEWithLogitsLoss is used
- Combined Binary Cross-Entropy Loss among all heads taken into account weights of each head
      - PyTorch BCEWithLogitsLoss is used
      - It is given by the formula $combined\_bce = head\_weights_1 * bce\_head_1 + head\_weights_2 * bce\_head_2 + head\_weights_3 * bce\_head_3$

### Results
- The model obtained an F1-score of $67\%$ and an accuracy of $70\%$.

## Technical Specifications

### Hardware
- RAM: at least 16 GB
- Storage: at least 2GB,
- GPU: T4 x 2

### Software
- Transformers 4.18.0
- Pytorch 1.11.0+cu113


## Bias, Risks, and Limitations
<!-- This section is meant to convey both technical and sociotechnical limitations. -->
- Any inputs (concatenation of two sequences) longer than 512 subwords will be truncated by the model.
- Batch size must not be larger than 32 or the GPU cannot allocate enough memory storage (at least on Kaggle). 


## Additional Information
<!-- Any other information that would be useful for other people to know. -->
- The hyperparameters were determined by experimentation with different values. 
- Graphs of losses, F1-score, Precision and Recall, are plotted to determine the optimla head weights and BERT model to be used for this task. Refer to [Hyperparameter Selection](#training-hyperparameters) for more information on the optimal hyperparameters found. 