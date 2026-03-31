---
{}
---
language: en
license: cc-by-4.0
tags:
- text-classification
repo: https://github.com/Toothless7788/COMP34812-nlu-coursework

---

# Model Card for w45242hy-u14554as-track_abbreviation

<!-- Provide a quick summary of what the model is/does. -->

This is a classification model that was trained to detect whether two pieces of text were written by the same author. 
Its inputs are expected to be two strings, each representing the target piece of text. 
Its output is expected to be a label with ```1``` predicting the given two pieces of text belong to the same author, ```0``` otherwise. 


## Model Details

### Model Description
<!-- Provide a longer summary of what this model is. -->
The model implements a Hybrid Multi-Head Cross-Encoder architecture, designed to capture both deep semantic interactions and explicit linguistic signatures. The system is composed of a high-capacity transformer backbone and a specialised multi-head decoder. 

#### 1. Joint Representation Cross-Encoder
The core architecture utilises a Cross-Encoder approach. It is based on the "bert-base-cased" (after hyperparameter selection mentioned in Section [Training Hyperparameters](#training-hyperparameters)). Unlike Bi-Encoders, which process texts independently, this model feeds both pieces of text simultaneously into the transformer. This allows for full self-attention across the pair, enabling the model to extract token-level interactions that are critical for identifying a single author’s unique writing style. 

Given the dataset scale of 30K pairs, the Cross-Encoder provides superior predictive accuracy over Bi-Encoder alternatives, effectively managing the computational trade-off between inference speed and classification performance. 

#### 2. Multi-Head Representation Fusion
The decoder stage employs a **Multi-Task Learning** (*MTL*) strategy to regularise the model and ensure it considers multiple dimensions of authorship. Before branching into individual heads, the pooled ```[CLS]``` embedding is passed through a shared linear projection layer. This facilitates feature extraction, distilling a unified representation from which three specialised heads operate:
- **Global Author Head**: The primary classification branch that assesses the probability of a shared identity based on the joint encoding. 
- **Neural Style Head**: This head is supervised by Style Similarity Scores. By calculating the cosine similarity between independent *SentenceTransformer* embeddings of the two texts, the model is forced to account for high-level semantic alignment. 
- **Stylometric Differential Head**: This head takes a $171$-dimensional **Feature Delta Vector**. This vector represents the absolute difference between explicit stylometric markers (e.g. function word frequencies, POS trigram distributions, and punctuation density). It is given by the formula $\left|text_1 - text_2\right|$. 

#### 3. Weighted Ensemble Inference
The final output is not a simple average, but a weighted linear combination of the logits from all three heads. This allows for fine-tuned calibration, prioritising the deep transformer interactions while using stylometric and neural similarities as weighted "expert opinions" to resolve ambiguous cases. 


- **Developed by:** Hin Yui Jacob Yip and Abdullah Sweesi
- **Language(s):** English
- **Model type:** Supervised
- **Model architecture:** Transformers
- **Fine-tuned from model [optional]:** bert-base-uncased

### Model Resources
<!-- Provide links where applicable. -->
- **Repository:** [Link to BERT model used](https://huggingface.co/google-bert/bert-base-cased)
- **Paper:** [Paper explaining why a cross-encoder is chosen for this task](https://ceur-ws.org/Vol-3180/paper-206.pdf)
- **Documentation:**: [Website explaining what a cross-encoder is](https://sbert.net/examples/cross_encoder/applications/README.html)


## Training Details

### Training Data
<!-- This is a short stub of information on the training data that was used, and documentation related to data pre-processing or additional filtering (if applicable). -->
- 30K pairs of texts drawn from emails, news articles and blog posts. 
- There are mainly two data pre-processing steps: both compute the similarity between the two pieces of text. 

#### 1. Similarity Score
- The two pieces of text are converted to embedding vectors using ```SentenceTransformer``` from ```sentence_transformers```. The similarity of the two vectors are then compared using cosine similarity to compute a similarity score. This score is then outputted to an external csv file with column "style_similarity_score", which is an input passed to the tokenizer and then the first head of the decoder. 

#### 2. Stylometric Delta Vector
- An embedding vector is created for each pair of text piece. The stylometric features of each of the text piece are first extracted and they are then compared. Their difference is represented by an embedding vector, i.e. $\left|text_1 - text_2\right|$, which is then outputted to a separate csv file. There are $171$ columns in this csv file, each representing 1 feature. This csv file is then read again during training, validation and evaluation, and the embedding vector is passed to the third head of the decoder directly. 

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
- In addition to using the self-implemented F1-score metric in validation, evluation is also done by running the command below: 
```sh
python ./local_scorer/main.py --task av --prediction <path_to_predictions_csv>
```
- This command provides other metrics, e.g. weighted macro F1-score and Matthews Correlation Coefficient, which allow better hyperparameter selections


### Testing Data & Metrics

#### Testing Data
<!-- This should describe any evaluation data used (e.g., the development/validation set provided). -->
- A subset of the development set provided, amounting to 2K pairs. 

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
- TODO: Update

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
      - A cross-encoder is used so the 512-token limit is shared between Text 1 and Text 2
- Batch size must not be larger than 32 or the GPU cannot allocate enough memory storage (at least on Kaggle). 


## Additional Information
<!-- Any other information that would be useful for other people to know. -->
- The hyperparameters were determined by experimentation with different values. 
- Graphs of losses, F1-score, Precision and Recall, are plotted to determine the optimla head weights and BERT model to be used for this task. Refer to [Hyperparameter Selection](#training-hyperparameters) for more information on the optimal hyperparameters found. 