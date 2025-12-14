---
layout: publication
title: Deep Metric Learning With Soft Orthogonal Proxies
authors: Farshad Saberi-Movahed, Mohammad K. Ebrahimpour, Farid Saberi-Movahed, Monireh
  Moshavash, Dorsa Rahmatian, Mahvash Mohazzebi, Mahdi Shariatzadeh, Mahdi Eftekhari
conference: Arxiv
year: 2023
bibkey: saberimovahed2023deep
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.13055'}]
tags: [Distance Metric Learning, Image Retrieval, Evaluation]
short_authors: Saberi-Movahed et al.
---
Deep Metric Learning (DML) models rely on strong representations and
similarity-based measures with specific loss functions. Proxy-based losses have
shown great performance compared to pair-based losses in terms of convergence
speed. However, proxies that are assigned to different classes may end up being
closely located in the embedding space and hence having a hard time to
distinguish between positive and negative items. Alternatively, they may become
highly correlated and hence provide redundant information with the model. To
address these issues, we propose a novel approach that introduces Soft
Orthogonality (SO) constraint on proxies. The constraint ensures the proxies to
be as orthogonal as possible and hence control their positions in the embedding
space. Our approach leverages Data-Efficient Image Transformer (DeiT) as an
encoder to extract contextual features from images along with a DML objective.
The objective is made of the Proxy Anchor loss along with the SO
regularization. We evaluate our method on four public benchmarks for
category-level image retrieval and demonstrate its effectiveness with
comprehensive experimental results and ablation studies. Our evaluations
demonstrate the superiority of our proposed approach over state-of-the-art
methods by a significant margin.