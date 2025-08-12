---
layout: publication
title: Improving Generalization Of Metric Learning Via Listwise Self-distillation
authors: Zelong Zeng, Fan Yang, Zheng Wang, Shin'Ichi Satoh
conference: Arxiv
year: 2022
bibkey: zeng2022improving
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.08880'}]
tags: ["Distance Metric Learning"]
short_authors: Zeng et al.
---
Most deep metric learning (DML) methods employ a strategy that forces all
positive samples to be close in the embedding space while keeping them away
from negative ones. However, such a strategy ignores the internal relationships
of positive (negative) samples and often leads to overfitting, especially in
the presence of hard samples and mislabeled samples. In this work, we propose a
simple yet effective regularization, namely Listwise Self-Distillation (LSD),
which progressively distills a model's own knowledge to adaptively assign a
more appropriate distance target to each sample pair in a batch. LSD encourages
smoother embeddings and information mining within positive (negative) samples
as a way to mitigate overfitting and thus improve generalization. Our LSD can
be directly integrated into general DML frameworks. Extensive experiments show
that LSD consistently boosts the performance of various metric learning methods
on multiple datasets.