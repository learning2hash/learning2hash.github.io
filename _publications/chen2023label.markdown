---
layout: publication
title: Label-aware Hyperbolic Embeddings For Fine-grained Emotion Classification
authors: Chih-Yao Chen, Tun-Min Hung, Yi-Li Hsu, Lun-Wei Ku
conference: 'Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2023
bibkey: chen2023label
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.14822'}]
tags: []
short_authors: Chen et al.
---
Fine-grained emotion classification (FEC) is a challenging task.
Specifically, FEC needs to handle subtle nuance between labels, which can be
complex and confusing. Most existing models only address text classification
problem in the euclidean space, which we believe may not be the optimal
solution as labels of close semantic (e.g., afraid and terrified) may not be
differentiated in such space, which harms the performance. In this paper, we
propose HypEmo, a novel framework that can integrate hyperbolic embeddings to
improve the FEC task. First, we learn label embeddings in the hyperbolic space
to better capture their hierarchical structure, and then our model projects
contextualized representations to the hyperbolic space to compute the distance
between samples and labels. Experimental results show that incorporating such
distance to weight cross entropy loss substantially improves the performance
with significantly higher efficiency. We evaluate our proposed model on two
benchmark datasets and found 4.8% relative improvement compared to the previous
state of the art with 43.2% fewer parameters and 76.9% less training time. Code
is available at https: //github.com/dinobby/HypEmo.