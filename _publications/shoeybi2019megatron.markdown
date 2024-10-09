---
layout: publication
title: Megatron-lm Training Multi-billion Parameter Language Models Using Model Parallelism
authors: Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick Legresley, Jared Casper, Bryan Catanzaro
conference: "Arxiv"
year: 2019
bibkey: shoeybi2019megatron
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/1909.08053v4"}
tags: ['ARXIV']
---
Recent work in language modeling demonstrates that training large transformer models advances the state of the art in Natural Language Processing applications. However very large models can be quite difficult to train due to memory constraints. In this work we present our techniques for training very large transformer models and implement a simple efficient intra-layer model parallel approach that enables training transformer models with billions of parameters. Our approach does not require a new compiler or library changes is orthogonal and complimentary to pipeline model parallelism and can be fully implemented with the insertion of a few communication operations in native PyTorch. We illustrate this approach by converging transformer based models up to 8.3 billion parameters using 512 GPUs. We sustain 15.1 PetaFLOPs across the entire application with 7637; scaling efficiency when compared to a strong single GPU baseline that sustains 39 TeraFLOPs which is 3037; of peak FLOPs. To demonstrate that large language models can further advance the state of the art (SOTA) we train an 8.3 billion parameter transformer language model similar to GPT-2 and a 3.9 billion parameter model similar to BERT. We show that careful attention to the placement of layer normalization in BERT-like models is critical to achieving increased performance as the model size grows. Using the GPT-2 model we achieve SOTA results on the WikiText103 (10.8 compared to SOTA perplexity of 15.8) and LAMBADA (66.537; compared to SOTA accuracy of 63.237;) datasets. Our BERT model achieves SOTA results on the RACE dataset (90.937; compared to SOTA accuracy of 89.437;).
