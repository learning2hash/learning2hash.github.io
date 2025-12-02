---
layout: publication
title: A Universal Framework For Compressing Embeddings In CTR Prediction
authors: Kefan Wang, Hao Wang, Kenan Song, Wei Guo, Kai Cheng, Zhi Li, Yong Liu, Defu
  Lian, Enhong Chen
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2025
bibkey: wang2025a
citations: 958
additional_links: [{name: Code, url: 'https://github.com/USTC-StarTeam/MEC'}, {name: Paper,
    url: 'https://arxiv.org/abs/2502.15355'}]
tags: ["Hashing Methods", "Quantization", "Similarity Search", "Survey Paper"]
short_authors: Wang et al.
---
Accurate click-through rate (CTR) prediction is vital for online advertising
and recommendation systems. Recent deep learning advancements have improved the
ability to capture feature interactions and understand user interests. However,
optimizing the embedding layer often remains overlooked. Embedding tables,
which represent categorical and sequential features, can become excessively
large, surpassing GPU memory limits and necessitating storage in CPU memory.
This results in high memory consumption and increased latency due to frequent
GPU-CPU data transfers. To tackle these challenges, we introduce a
Model-agnostic Embedding Compression (MEC) framework that compresses embedding
tables by quantizing pre-trained embeddings, without sacrificing recommendation
quality. Our approach consists of two stages: first, we apply
popularity-weighted regularization to balance code distribution between high-
and low-frequency features. Then, we integrate a contrastive learning mechanism
to ensure a uniform distribution of quantized codes, enhancing the
distinctiveness of embeddings. Experiments on three datasets reveal that our
method reduces memory usage by over 50x while maintaining or improving
recommendation performance compared to existing models. The implementation code
is accessible in our project repository https://github.com/USTC-StarTeam/MEC.