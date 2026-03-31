# COMP34812-nlu-coursework
The repository for 2025-2026 COMP34812 NLU coursework


# Cross-Encoder
- ## Category
    - **C**: Deep learning-based approaches underpinned by transformer architectures
- ## External Code/Model Reused
    - [transformers/bert-base-cased](https://huggingface.co/google-bert/bert-base-cased)
        - Encoder part of the model
    - [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
        - For computing ```style_similarity_score```, which is an additional input to the model (the model expects more than two pieces of text)
    - [en_core_web_md](https://huggingface.co/spacy/en_core_web_md)
        - For tokenisation
        - Indirectly used in extracting the stylometric features of the two pieces of text, which is another additional input to the model
- ## External Essential Links
    - [Weights of fine-tuned model](https://livemanchesterac-my.sharepoint.com/:u:/g/personal/hin_yip-2_student_manchester_ac_uk/IQCqvNYKjup1TJiuN0rNVV5pATcs55cOX-ljPt6ymyYczzc?e=8RqG2L)
        - Make sure you are using the **university email account**
- ## Required Files
    1. ```submission_C_training.ipynb```
        - The notebook to train the model, i.e. training
        - The weights of the trained model will be saved to a ```.pth``` file
    2. ```submission_C_validation.ipynb```
        - The notebook to perform hyperparameter selection, i.e. validation
        - A ```.pth``` file of weights of the fine-tuned model is required
    3. ```submission_C_demo.ipynb```
        - The notebook to demonstrate running model in inference mode, i.e. testing
        - A ```.pth``` file of weights of the fine-tuned model is required
    4. ```model_card_C.md```
        - The model card of this model
        - Provide more detailed documentations
    5. ```AV_trial.csv```
        - The csv file containing data for trial
    6. ```train.csv```
        - The csv file containing the training data
        - For ```submission_C_training.ipynb```
    7. ```dev.csv```
        - The csv file containing the validation data
        - For ```submission_C_validation.ipynb```
    8. ```test.csv```
        - The csv file containing the testing data
        - For ```submission_C_demo.ipynb```
- ## Run Notebooks
    1. Download the ```.pth``` file, which contains the weights of the fine-tuned model, from OneDriver
        - Refer to Section [External Essential Links](#external-essential-links)
        - Make sure the filename is ```cross-encoder_080101_bert-base-cased.pth```
    2. Make sure all files are at the same folder level
    3. Look for "TODO: Update me if applicable" in the notebook and update the variables if applicable
    4. Make sure ```INPUT_FOLDER_PATH``` and ```OUTPUT_FOLDER_PATH``` are the same
        - Otherwise, you have to manually update ```CROSS_ENCODER_PATH``` to read the ```.pth``` file correctly
    5. Run the notebook! 


# Siamese LSTM
- ## Category
    - **B**: Deep learning-based approaches that do not employ transformer architectures
- ## External Code/Model Reused
    - [fasttext-crawl-300d-2m](https://www.kaggle.com/datasets/yekenot/fasttext-crawl-300d-2m)
        - The source of pre-computed static word embeddings
    - [en_core_web_md](https://huggingface.co/spacy/en_core_web_md)
        - For tokenisation
        - Indirectly used in extracting the stylometric features of the two pieces of text, which is another additional input to the model
        - Also used for generating word embeddings
- ## External Essential Links
    - [Final model state dict](https://drive.google.com/file/d/13x43HGyn8Rx2BIATovEJzMeT7XUTjhgG/view?usp=drive_link)
    - [Generated embeddings](https://drive.google.com/file/d/17rFP_70pke2ynrLT_ryzS-KKVxzbKnbf/view?usp=drive_link)
    - [Vocabulary](https://drive.google.com/file/d/1U-sNRiCwe5WkAbqs6s48CMPSpQw9u_UO/view?usp=drive_link)
    - [Stylometric feature scaler](https://drive.google.com/file/d/16C-RxvSCvaHrya89Tj59tUHWp8c41TSa/view?usp=drive_link)
- ## Deliverables (found in './lstm/deliverables' folder)
    1. ```submission_B_training.ipynb```
        - The notebook to train the model, i.e. training
        - The 'fasttext-crawl-300d-2m' dataset (found on Kaggle) is necessary to run this file
    2. ```submission_B_validation.ipynb```
        - The notebook to perform hyperparameter selection, i.e. validation
        - A ```.pth``` file of weights of the fine-tuned model is required
    3. ```submission_B_demo.ipynb```
        - The notebook to demonstrate running model in inference mode, i.e. testing
        - A ```.pth``` file of weights of the fine-tuned model is required
    4. ```model_card_B.md```
        - The model card of this model
        - Provide more detailed documentations
- ## Other required files (found in './data/AV' folder)
    2. ```train.csv```
        - The csv file containing the training data
        - For ```submission_B_training.ipynb```
    3. ```dev.csv```
        - The csv file containing the validation data
        - For ```submission_B_validation.ipynb``` and ```submission_B_training.ipynb``` (hyperparameter tuning)
    4. ```test.csv```
        - The csv file containing the testing data
        - For ```submission_B_demo.ipynb```
- ## Run Notebooks
    1. Download the corresponding input data file(s) (and for training, also download the 'fasttext-crawl-300d-2m' dataset - see External Links)
    3. Update input/output path variables (in the 'Constants' section) to reflect your folder structure
    5. Run the notebook! 