---
layout: publication
title: Pangu-σ Towards Trillion Parameter Language Model With Sparse Heterogeneous Computing
authors: Xiaozhe Ren, Pingyi Zhou, Xinfan Meng, Xinjing Huang, Yadao Wang, Weichao Wang, Pengfei Li, Xiaoda Zhang, Alexander Podolskiy, Grigory Arshinov, Andrey Bout, Irina Piontkovskaya, Jiansheng Wei, Xin Jiang, Teng Su, Qun Liu, Jun Yao
conference: "Arxiv"
year: 2023
bibkey: ren2023pangu
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2303.10845v1"}
tags: ['ARXIV', 'Cross Modal', 'Independent']
---
The scaling of large language models has greatly improved natural language understanding generation and reasoning. In this work we develop a system that trained a trillion-parameter language model on a cluster of Ascend 910 AI processors and MindSpore framework and present the language model with 1.085T parameters named PanGu-Sigma. With parameter inherent from PanGu-alpha we extend the dense Transformer model to sparse one with Random Routed Experts (RRE) and efficiently train the model over 329B tokens by using Expert Computation and Storage Separation(ECSS). This resulted in a 6.3x increase in training throughput through heterogeneous computing. Our experimental findings show that PanGu-Sigma provides state-of-the-art performance in zero-shot learning of various Chinese NLP downstream tasks. Moreover it demonstrates strong abilities when fine-tuned in application data of open-domain dialogue question answering machine translation and code generation.
