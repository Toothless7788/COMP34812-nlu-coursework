import torch

experiment_outputs = {
    (torch.tensor([0.1000, 0.1000, 0.8000]), 'bert-base-uncased'): {
        'losses_train': {
            'loss': [0.656348803046125], 
            'loss_author': [0.47105027709363234], 
            'loss_style_similarity': [0.47400654424671773], 
            'loss_manual_stylometry': [0.7023038839990342]
        }, 
        'losses_validation': {
            'loss': [0.6507573879145562], 
            'loss_author': [0.4168124519922632], 
            'loss_style_similarity': [0.4709009957757402], 
            'loss_manual_stylometry': [0.7024825380203572], 
            'f1': [0.6436830835117773], 
            'precision': [0.9312267657992565], 
            'recall': [0.4918193717277487]
        }
    }
}