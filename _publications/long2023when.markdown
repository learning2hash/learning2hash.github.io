---
layout: publication
title: When Hard Negative Sampling Meets Supervised Contrastive Learning
authors: Zijun Long, George Killick, Richard Mccreadie, Gerardo Aragon Camarasa, Zaiqiao
  Meng
conference: Arxiv
year: 2023
bibkey: long2023when
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.14893'}]
tags: ["Distance Metric Learning", "Few Shot & Zero Shot", "Self-Supervised", "Supervised"]
short_authors: Long et al.
---
State-of-the-art image models predominantly follow a two-stage strategy:
pre-training on large datasets and fine-tuning with cross-entropy loss. Many
studies have shown that using cross-entropy can result in sub-optimal
generalisation and stability. While the supervised contrastive loss addresses
some limitations of cross-entropy loss by focusing on intra-class similarities
and inter-class differences, it neglects the importance of hard negative
mining. We propose that models will benefit from performance improvement by
weighting negative samples based on their dissimilarity to positive
counterparts. In this paper, we introduce a new supervised contrastive learning
objective, SCHaNe, which incorporates hard negative sampling during the
fine-tuning phase. Without requiring specialized architectures, additional
data, or extra computational resources, experimental results indicate that
SCHaNe outperforms the strong baseline BEiT-3 in Top-1 accuracy across various
benchmarks, with significant gains of up to \\(3.32%\\) in few-shot learning
settings and \\(3.41%\\) in full dataset fine-tuning. Importantly, our proposed
objective sets a new state-of-the-art for base models on ImageNet-1k, achieving
an 86.14% accuracy. Furthermore, we demonstrate that the proposed objective
yields better embeddings and explains the improved effectiveness observed in
our experiments.