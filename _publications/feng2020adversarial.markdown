---
layout: publication
title: Adversarial Attack On Deep Product Quantization Network For Image Retrieval
authors: Feng et al.
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2020
bibkey: feng2020adversarial
citations: 43
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.11374'}]
tags: [Image Retrieval, AAAI, DATASETS, Efficiency And Optimization, Quantization,
  Evaluation, Robustness]
---
Deep product quantization network (DPQN) has recently received much attention
in fast image retrieval tasks due to its efficiency of encoding
high-dimensional visual features especially when dealing with large-scale
datasets. Recent studies show that deep neural networks (DNNs) are vulnerable
to input with small and maliciously designed perturbations (a.k.a., adversarial
examples). This phenomenon raises the concern of security issues for DPQN in
the testing/deploying stage as well. However, little effort has been devoted to
investigating how adversarial examples affect DPQN. To this end, we propose
product quantization adversarial generation (PQ-AG), a simple yet effective
method to generate adversarial examples for product quantization based
retrieval systems. PQ-AG aims to generate imperceptible adversarial
perturbations for query images to form adversarial queries, whose nearest
neighbors from a targeted product quantizaiton model are not semantically
related to those from the original queries. Extensive experiments show that our
PQ-AQ successfully creates adversarial examples to mislead targeted product
quantization retrieval models. Besides, we found that our PQ-AG significantly
degrades retrieval performance in both white-box and black-box settings.