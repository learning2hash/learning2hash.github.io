---
layout: publication
title: Adalora Adaptive Budget Allocation For Parameter-efficient Fine-tuning
authors: Qingru Zhang, Minshuo Chen, Alexander Bukharin, Nikos Karampatziakis, Pengcheng He, Yu Cheng, Weizhu Chen, Tuo Zhao
conference: "Arxiv"
year: 2023
bibkey: zhang2023adalora
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2303.10512v2"}
  - {name: "Code", url: "https://github.com/QingruZhang/AdaLoRA"}
tags: ['ARXIV', 'Has Code']
---
Fine-tuning large pre-trained language models on downstream tasks has become an important paradigm in NLP. However common practice fine-tunes all of the parameters in a pre-trained model which becomes prohibitive when a large number of downstream tasks are present. Therefore many fine-tuning methods are proposed to learn incremental updates of pre-trained weights in a parameter efficient way e.g. low-rank increments. These methods often evenly distribute the budget of incremental updates across all pre-trained weight matrices and overlook the varying importance of different weight parameters. As a consequence the fine-tuning performance is suboptimal. To bridge this gap we propose AdaLoRA which adaptively allocates the parameter budget among weight matrices according to their importance score. In particular AdaLoRA parameterizes the incremental updates in the form of singular value decomposition. Such a novel approach allows us to effectively prune the singular values of unimportant updates which is essentially to reduce their parameter budget but circumvent intensive exact SVD computations. We conduct extensive experiments with several pre-trained models on natural language processing question answering and natural language generation to validate the effectiveness of AdaLoRA. Results demonstrate that AdaLoRA manifests notable improvement over baselines especially in the low budget settings. Our code is publicly available at https://github.com/QingruZhang/AdaLoRA .
