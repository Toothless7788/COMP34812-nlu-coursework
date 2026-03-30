import torch

experiment_outputs = {
    (torch.tensor([0.2500, 0.2500, 0.5000]), 'bert-base-cased'): {
        'losses_train': {
            'loss': [0.5798117134168193], 
            'loss_author': [0.4497284750212674], 
            'loss_style_similarity': [0.4753393569133348], 
            'loss_manual_stylometry': [0.6970895113492453]
        }, 
        'losses_validation': {
            'loss': [0.5657090392518551], 
            'loss_author': [0.3890712350765441], 
            'loss_style_similarity': [0.47331247447018926], 
            'loss_manual_stylometry': [0.7002262222640058], 
            'f1': [0.6841776110068793], 
            'precision': [0.9425617461229179], 
            'recall': [0.536976439790576]
        }
    }, 
    (torch.tensor([0.2500, 0.5000, 0.2500]), 'bert-base-cased'): {
        'losses_train': {
            'loss': [0.5259907859963951], 
            'loss_author': [0.46429316114841235], 
            'loss_style_similarity': [0.47218578933151784], 
            'loss_manual_stylometry': [0.6952984070888272]
        }, 
        'losses_validation': {
            'loss': [0.5093903172206371], 
            'loss_author': [0.403021957011933], 
            'loss_style_similarity': [0.46990386491760294], 
            'loss_manual_stylometry': [0.6947315852058694], 
            'f1': [0.6201688138605065], 
            'precision': [0.9654218533886584], 
            'recall': [0.4568062827225131]
        }
    }, 
    (torch.tensor([0.5000, 0.2500, 0.2500]), 'bert-base-cased'): {
        'losses_train': {
            'loss': [0.5176317831846299], 
            'loss_author': [0.44638245337194316], 
            'loss_style_similarity': [0.4800005172620769], 
            'loss_manual_stylometry': [0.6977617136996102]
        }, 
        'losses_validation': {
            'loss': [0.4852057137387864], 
            'loss_author': [0.3839713877185862], 
            'loss_style_similarity': [0.4761090416540491], 
            'loss_manual_stylometry': [0.6967710430951829], 
            'f1': [0.7603686635944701], 
            'precision': [0.9200743494423792], 
            'recall': [0.6479057591623036]
        }
    }
}