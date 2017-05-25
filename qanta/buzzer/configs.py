class mlp():
    optimizer = 'Adam'
    max_grad_norm = 5
    batch_size = 128
    n_hidden = 5
    n_layers = 0
    dropout = 0
    step_size = 1
    neg_weight = 1
    batch_norm = False
    ckp_dir = 'output/buzzer/mlp_buzzer.ckp'
    model_dir = 'output/buzzer/mlp_buzzer.npz'

class rnn():
    optimizer = 'Adam'
    max_grad_norm = 5
    batch_size = 128
    n_hidden = 128
    ckp_dir = 'output/buzzer/rnn_buzzer.ckp'
    model_dir = 'output/buzzer/rnn_buzzer.npz'
