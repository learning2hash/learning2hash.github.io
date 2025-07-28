---
layout: publication
title: 'FILM: How Can Few-shot Image Classification Benefit From Pre-trained Language
  Models?'
authors: Zihao Jiang, Yunkai Dang, Dong Pang, Huishuai Zhang, Weiran Huang
conference: Arxiv
year: 2023
bibkey: jiang2023film
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.04114'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Jiang et al.
---
Few-shot learning aims to train models that can be generalized to novel
classes with only a few samples. Recently, a line of works are proposed to
enhance few-shot learning with accessible semantic information from class
names. However, these works focus on improving existing modules such as visual
prototypes and feature extractors of the standard few-shot learning framework.
This limits the full potential use of semantic information. In this paper, we
propose a novel few-shot learning framework that uses pre-trained language
models based on contrastive learning. To address the challenge of alignment
between visual features and textual embeddings obtained from text-based
pre-trained language model, we carefully design the textual branch of our
framework and introduce a metric module to generalize the cosine similarity.
For better transferability, we let the metric module adapt to different
few-shot tasks and adopt MAML to train the model via bi-level optimization.
Moreover, we conduct extensive experiments on multiple benchmarks to
demonstrate the effectiveness of our method.