---
layout: publication
title: 'Llave: Large Language And Vision Embedding Models With Hardness-weighted Contrastive
  Learning'
authors: Zhibin Lan, Liqiang Niu, Fandong Meng, Jie Zhou, Jinsong Su
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2025'
year: 2025
bibkey: lan2025llave
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.04812'}]
tags: ["Datasets", "Efficiency", "Few Shot & Zero Shot", "Image Retrieval", "Video Retrieval"]
short_authors: Lan et al.
---
Universal multimodal embedding models play a critical role in tasks such as
interleaved image-text retrieval, multimodal RAG, and multimodal clustering.
However, our empirical results indicate that existing LMM-based embedding
models trained with the standard InfoNCE loss exhibit a high degree of overlap
in similarity distribution between positive and negative pairs, making it
challenging to distinguish hard negative pairs effectively. To deal with this
issue, we propose a simple yet effective framework that dynamically improves
the embedding model's representation learning for negative pairs based on their
discriminative difficulty. Within this framework, we train a series of models,
named LLaVE, and evaluate them on the MMEB benchmark, which covers 4 meta-tasks
and 36 datasets. Experimental results show that LLaVE establishes stronger
baselines that achieve state-of-the-art (SOTA) performance while demonstrating
strong scalability and efficiency. Specifically, LLaVE-2B surpasses the
previous SOTA 7B models, while LLaVE-7B achieves a further performance
improvement of 6.2 points. Although LLaVE is trained on image-text data, it can
generalize to text-video retrieval tasks in a zero-shot manner and achieve
strong performance, demonstrating its remarkable potential for transfer to
other embedding tasks.