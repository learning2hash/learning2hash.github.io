---
layout: publication
title: 'Kalahash: Knowledge-anchored Low-resource Adaptation For Deep Hashing'
authors: Shu Zhao, Tan Yu, Xiaoshuai Hao, Wenchao Ma, Vijaykrishnan Narayanan
conference: Arxiv
year: 2024
bibkey: zhao2024kalahash
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.19417'}]
tags: ["Efficiency", "Hashing Methods", "Neural Hashing"]
short_authors: Zhao et al.
---
Deep hashing has been widely used for large-scale approximate nearest
neighbor search due to its storage and search efficiency. However, existing
deep hashing methods predominantly rely on abundant training data, leaving the
more challenging scenario of low-resource adaptation for deep hashing
relatively underexplored. This setting involves adapting pre-trained models to
downstream tasks with only an extremely small number of training samples
available. Our preliminary benchmarks reveal that current methods suffer
significant performance degradation due to the distribution shift caused by
limited training samples. To address these challenges, we introduce
Class-Calibration LoRA (CLoRA), a novel plug-and-play approach that dynamically
constructs low-rank adaptation matrices by leveraging class-level textual
knowledge embeddings. CLoRA effectively incorporates prior class knowledge as
anchors, enabling parameter-efficient fine-tuning while maintaining the
original data distribution. Furthermore, we propose Knowledge-Guided Discrete
Optimization (KIDDO), a framework to utilize class knowledge to compensate for
the scarcity of visual information and enhance the discriminability of hash
codes. Extensive experiments demonstrate that our proposed method, Knowledge-
Anchored Low-Resource Adaptation Hashing (KALAHash), significantly boosts
retrieval performance and achieves a 4x data efficiency in low-resource
scenarios.