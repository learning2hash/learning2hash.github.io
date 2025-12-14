---
layout: publication
title: 'GENIUS: A Generative Framework For Universal Multimodal Search'
authors: Sungyeon Kim, Xinliang Zhu, Xiaofan Lin, Muhammet Bastan, Douglas Gray, Suha
  Kwak
conference: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2025
bibkey: kim2025genius
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.19868'}]
tags: [Evaluation, Re-ranking, Efficiency, Quantization, CVPR, Tools & Libraries,
  Hybrid ANN Methods]
short_authors: Kim et al.
---
Generative retrieval is an emerging approach in information retrieval that generates identifiers (IDs) of target data based on a query, providing an efficient alternative to traditional embedding-based retrieval methods. However, existing models are task-specific and fall short of embedding-based retrieval in performance. This paper proposes GENIUS, a universal generative retrieval framework supporting diverse tasks across multiple modalities and domains. At its core, GENIUS introduces modality-decoupled semantic quantization, transforming multimodal data into discrete IDs encoding both modality and semantics. Moreover, to enhance generalization, we propose a query augmentation that interpolates between a query and its target, allowing GENIUS to adapt to varied query forms. Evaluated on the M-BEIR benchmark, it surpasses prior generative methods by a clear margin. Unlike embedding-based retrieval, GENIUS consistently maintains high retrieval speed across database size, with competitive performance across multiple benchmarks. With additional re-ranking, GENIUS often achieves results close to those of embedding-based methods while preserving efficiency.