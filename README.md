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