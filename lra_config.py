config = {
    "listops":{
        "pe_type": "cpe",
        "vocab_size": 15 + 1 + 1, # 15 tokens + 1 PAD + 1 CLS
        "embed_dim": 32,
        "max_seq_len": 1999 + 1,
        "enable_kpm": True,
        "kernel_type": "none",
        "max_order": 2,
        "mu": 3,
        "xi": 4.0,
        "stigma": 0.5,
        "heta": 2,
        "hid_dim": 32 * 4,
        "dataset_name": "listops",
        "pooling_type": "CLS", # "CLS", "MEAN", "SUM", or "FLATTEN"
        "encoder_dim": 32,
        "mlp_dim": 32,
        "num_class": 10,
        "classifier_type": "single",
        "enable_cuda": True,
        "device_id": 0,
        "embed_drop_prob": 0.1,
        "eigenvalue_drop_prob": 0.0,
        "value_drop_prob": 0.0,
        "chsyconv_drop_prob": 0.0,
        "bffn_drop_prob": 0.1,
        "batch_size": 64,
        "lr": 0.001,
        "weight_decay": 0.0001,
        "epochs": 20, # 30 for 39.26%
        "optimizer": "sophia",
        "patience": 2,
        "criteria": 39
    },
    "image":{
        "pe_type": "cpe",
        "vocab_size": 256, # 256 unique pixel values
        "embed_dim": 64,
        "max_seq_len": 1024,
        "enable_kpm": True,
        "kernel_type": "none",
        "max_order": 2,
        "mu": 3,
        "xi": 4.0,
        "stigma": 0.5,
        "heta": 2,
        "hid_dim": 64 * 4,
        "dataset_name": "image",
        "pooling_type": "FLATTEN", # "CLS", "MEAN", "SUM", or "FLATTEN"
        "encoder_dim": 64,
        "mlp_dim": 64,
        "num_class": 10,
        "classifier_type": "single",
        "enable_cuda": True,
        "device_id": 0, # single GPU
        "embed_drop_prob": 0.1,
        "eigenvalue_drop_prob": 0.0,
        "value_drop_prob": 0.0,
        "chsyconv_drop_prob": 0.0,
        "bffn_drop_prob": 0.1,
        "batch_size": 64,
        "lr": 0.001,
        "weight_decay": 0.001,
        "epochs": 15,
        "optimizer": "sophia",
        "patience": 2,
        "criteria": 46
    },
    "pathfinder":{
        "pe_type": "cpe",
        "vocab_size": 225, # 225 unique pixel values
        "embed_dim": 64,
        "max_seq_len": 1024,
        "enable_kpm": True,
        "kernel_type": "none",
        "max_order": 2,
        "mu": 3,
        "xi": 4.0,
        "stigma": 0.5,
        "heta": 2,
        "hid_dim": 64 * 4,
        "dataset_name": "pathfinder",
        "pooling_type": "FLATTEN", # "CLS", "MEAN", "SUM", or "FLATTEN"
        "encoder_dim": 64,
        "mlp_dim": 64,
        "num_class": 2,
        "classifier_type": "single",
        "enable_cuda": True,
        "device_id": 0,
        "embed_drop_prob": 0.1,
        "eigenvalue_drop_prob": 0.0,
        "value_drop_prob": 0.0,
        "chsyconv_drop_prob": 0.0,
        "bffn_drop_prob": 0.0,
        "batch_size": 64,
        "lr": 0.001,
        "weight_decay": 0.001,
        "epochs": 50,
        "optimizer": "sophia",
        "patience": 2,
        "criteria": 76
    },
    "text":{
        "pe_type": "cpe",
        "vocab_size": 95 + 1 + 1, # 95 unique symbols + 1 PAD + 1 CLS
        "embed_dim": 64,
        "max_seq_len": 4096 + 1,
        "enable_kpm": True,
        "kernel_type": "none",
        "max_order": 2,
        "mu": 3,
        "xi": 4.0,
        "stigma": 0.5,
        "heta": 2,
        "hid_dim": 64,
        "dataset_name": "text",
        "pooling_type": "CLS", # "CLS", "MEAN", "SUM", or "FLATTEN"
        "encoder_dim": 64,
        "mlp_dim": 64,
        "num_class": 2,
        "classifier_type": "single",
        "enable_cuda": True,
        "device_id": 0,
        "embed_drop_prob": 0.1,
        "eigenvalue_drop_prob": 0.0,
        "value_drop_prob": 0.0,
        "chsyconv_drop_prob": 0.0,
        "bffn_drop_prob": 0.1,
        "batch_size": 64,
        "lr": 0.001,
        "weight_decay": 0.001,
        "epochs": 20,
        "optimizer": "sophia",
        "patience": 2,
        "criteria": 76
    },
    "retrieval":{
        "pe_type": "cpe",
        "vocab_size": 96 + 1 + 1, # 96 unique symbols + 1 PAD + 1 CLS
        "embed_dim": 128,
        "max_seq_len": 4000,
        "enable_kpm": True,
        "kernel_type": "none",
        "max_order": 2,
        "mu": 3,
        "xi": 4.0,
        "stigma": 0.5,
        "heta": 2,
        "hid_dim": 512,
        "dataset_name": "retrieval",
        "pooling_type": "CLS", # "CLS", "MEAN", "SUM", or "FLATTEN"
        "encoder_dim": 128,
        "mlp_dim": 1024,
        "num_class": 2,
        "classifier_type": "dual",
        "interaction": "NLI",
        "enable_cuda": True,
        "device_id": 0,
        "embed_drop_prob": 0.1,
        "eigenvalue_drop_prob": 0.0,
        "value_drop_prob": 0.0,
        "chsyconv_drop_prob": 0.0,
        "bffn_drop_prob": 0.1,
        "batch_size": 32,
        "lr": 0.001,
        "weight_decay": 0.001,
        "epochs": 30,
        "optimizer": "sophia",
        "patience": 2,
        "criteria": 66
    }
}