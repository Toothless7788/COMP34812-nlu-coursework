# COMP34812-nlu-coursework
The repository for 2025-2026 COMP34812 NLU coursework


# Cross-Encoder
- ## Category
    - **C**: Deep learning-based approaches underpinned by transformer architectures
- ## External Code/Model Reused
    - [transformers/bert-base-cased```](https://huggingface.co/google-bert/bert-base-cased)
        - Encoder part of the model
    - [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
        - For computing ```style_similarity_score```, which is an additional input to the model (the model expects more than two pieces of text)
    - [/kaggle/input/datasets/yekenot/fasttext-crawl-300d-2m/crawl-300d-2M.vec](https://www.kaggle.com/datasets/yekenot/fasttext-crawl-300d-2m)
        - For extracting the stylometric features of the two pieces of text, which is another additional input to the model
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