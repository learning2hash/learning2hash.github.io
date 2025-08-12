---
layout: publication
title: Keep It Light! Simplifying Image Clustering Via Text-free Adapters
authors: "Yicen Li, Haitz S\xE1ez de Oc\xE1riz Borde, Anastasis Kratsios, Paul D.\
  \ McNicholas"
conference: Arxiv
year: 2025
bibkey: li2025keep
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.04226'}]
tags: []
short_authors: Li et al.
---
Many competitive clustering pipelines have a multi-modal design, leveraging
large language models (LLMs) or other text encoders, and text-image pairs,
which are often unavailable in real-world downstream applications.
Additionally, such frameworks are generally complicated to train and require
substantial computational resources, making widespread adoption challenging. In
this work, we show that in deep clustering, competitive performance with more
complex state-of-the-art methods can be achieved using a text-free and highly
simplified training pipeline. In particular, our approach, Simple Clustering
via Pre-trained models (SCP), trains only a small cluster head while leveraging
pre-trained vision model feature representations and positive data pairs.
Experiments on benchmark datasets including CIFAR-10, CIFAR-20, CIFAR-100,
STL-10, ImageNet-10, and ImageNet-Dogs, demonstrate that SCP achieves highly
competitive performance. Furthermore, we provide a theoretical result
explaining why, at least under ideal conditions, additional text-based
embeddings may not be necessary to achieve strong clustering performance in
vision.