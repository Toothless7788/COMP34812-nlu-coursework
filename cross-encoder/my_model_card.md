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
- To augment the transformer's raw text processing, a two-stage feature engineering pipeline was implemented to generated additional signals for more accurate predictions. 

#### 1. Neural Style Similarity
For each pair, both documents are projected into a high-dimensional vector space using a pre-trained ```SentenceTransformer``` (```all-MiniLM-L6-v2```). The **cosine similarity** between these embeddings is calculated to produce a ```style_similarity_score```. This score serves as a continuous supervision signal for the second head of the decoder. It helps the model to recognise semantic alignment beyond simple token overlap. 

#### 2. Stylometric Delta Vector
To incorporate classical linguistic insights, the model utilises a $171$-dimensional Stylometric Delta Vector. This vector is constructed by the following steps: 
1. Extracting a comprehensive suite of features, e.g. function word frequencies, POS trigrams, punctuation density and lexical richness, for both pieces of text, i.e. $text_1$ and $text_2$. 
2. Computing the absolute difference between these feature sets, i.e. $\left|text_1 - text_2\right|$. 
3. Normalising the resulting vector using a ```StandardScaler``` fitted on the training dataset. 
This vector provides the third decoder head with an explicit map of difference of the author's linguistic habits, which is passed directly to the decoder to complement the neural embeddings. 

### Training Procedure
<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->
The training workflow is designed as a Multi-Input Supervised Learning task. Unlike standard BERT classifiers, this model requires a synchronised data stream from all three sources, i.e. the pair of raw text pieces, the neural nsimilarity scores and the stylometric delta vectors. 

#### Optimisation and Loss Strategy
The model is optimised over $n$ epochs (see ```num_epochs``` in [Training Hyperparameters](#training-hyperparameters) for the final value picked) using the **AdamW** optimiser with a linear learning rate. To ensure robust convergence across all specialised heads, a composite loss function is employed: 
- **Objective Function**: ```BCEWithLogitsLoss``` from PyTorch is utilised for all heads to increase numerical stability using the log-sum-exp trick
- **Joint Loss Calculation**: The total loss of the whole model $\mathcal{L}_{total}$ is a weighted summation of the primary author verification loss and the additional stylistic losses. It uses the same weightings as the one used in predictions: 
      $$
      \mathcal{L}_{total} = w_1 \mathcal{L}_{author} + w_2 \mathcal{L}_{neural\_style} + w_3 \mathcal{L}_{stylometric}
      $$
      $$
      prediction_{total} = w_1 prediction_{author} + w_2 prediction_{neural\_style} + w_3 prediction_{stylometric}
      $$
- **Backpropagation**: Gradients are flowed back through the multi-head decoder into the shared projection layer and finally into the BERT encoder. This ensures that the transformer backbone learns representations that are simultaneously optimised for semantic intent, neural style and linguistic structure. 

#### Training Hyperparameters
<!-- This is a summary of the values of hyperparameters used in training the model. -->
- ```learning_rate```: 2e-05
- ```train_batch_size```: 32
- ```eval_batch_size```: 32
- ```seed```: N/A
- ```num_epochs```: 3 (After hyperparameter selection)
- ```model_name```: "bert-base-cased" (After hyperparameter selection)
- ```head_weights```: ```torch.tensor([0.8, 0.1, 0.1], dtype=torch.float)``` (After hyperparameter selection; ```head_weights[0]``` is the weight for the first head and so on)

#### Speeds, Sizes, Times
<!-- This section provides information about how roughly how long it takes to train the model and the size of the resulting model. -->
- overall training time: 3 hours
- duration per training epoch: 50 minutes
- model size: 400MB


## Evaluation
<!-- This section describes the evaluation protocols and provides the results. -->
- Self-implemented F1-score, precision and recall metrics have been used in validation, which essentially calculates the number of true-positive (TP), false-positive (FP), true-negative (TN) and false-negative (FN). Based on these metrics, graphs of different hyperparameter settings have been plotted and the best hyperparameter settings are picked by developers manually. Below contains the formulae for calculating the metrics: 
      $$
      precision = \frac{TP}{TP + FP}
      $$
      $$
      recall = \frac{TP}{TP + FN}
      $$
      $$
      F1 = \frac{2 \times precision \times recall}{precision + recall}
      $$
- In addition to the observing from the graph during hyperparameter selection, more metrics of models (e.g. *weighted macro F1-score* and *Matthews Correlation Coefficient*) have been computed and compared. Below contains the command to generate those metrics: 
```sh
python ./local_scorer/main.py --task av --prediction <path_to_predictions_csv>
```


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
- Matthews Correlation Coefficient
- Binary Cross-Entropy Loss for each head (PyTorch ```BCEWithLogitsLoss``` is used)
- Combined Binary Cross-Entropy Loss among all heads taken into account weights of each head (PyTorch ```BCEWithLogitsLoss``` is used)
      $$
      \mathcal{L}_{total} = w_1 \mathcal{L}_{author} + w_2 \mathcal{L}_{neural\_style} + w_3 \mathcal{L}_{stylometric}
      \\
      \text{where }\mathcal{L}\text{ is Binary Cross-Entropy Loss}
      $$

### Results
- The selected model in hyperparameter selection obtained an F1-score of $83\%$ and an accuracy of $83\%$. 

| Metric                          | Value              |
|--------------------------------:|-------------------:|
| Accuracy                        | $0.83247121641916$ |
| Macro Precision                 | $0.83297824961783$ |
| Macro Recall                    | $0.83286917947045$ |
| Macro F1                        | $0.83246915936938$ |
| Weighted Macro Precision        | $0.83297824961783$ |
| Weighted Macro Recall           | $0.83286917947045$ |
| Weighted Macro F1               | $0.83246915936938$ |
| Matthews Correlation Coefficient| $0.66584742015508$ |


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