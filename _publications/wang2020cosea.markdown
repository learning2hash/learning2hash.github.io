---
layout: publication
title: 'COSEA: Convolutional Code Search With Layer-wise Attention'
authors: Hao Wang, Jia Zhang, Yingce Xia, Jiang Bian, Chao Zhang, Tie-Yan Liu
conference: Arxiv
year: 2020
bibkey: wang2020cosea
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.09520'}]
tags: []
short_authors: Wang et al.
---
Semantic code search, which aims to retrieve code snippets relevant to a
given natural language query, has attracted many research efforts with the
purpose of accelerating software development. The huge amount of online
publicly available code repositories has prompted the employment of deep
learning techniques to build state-of-the-art code search models. Particularly,
they leverage deep neural networks to embed codes and queries into a unified
semantic vector space and then use the similarity between code's and query's
vectors to approximate the semantic correlation between code and the query.
However, most existing studies overlook the code's intrinsic structural logic,
which indeed contains a wealth of semantic information, and fails to capture
intrinsic features of codes. In this paper, we propose a new deep learning
architecture, COSEA, which leverages convolutional neural networks with
layer-wise attention to capture the valuable code's intrinsic structural logic.
To further increase the learning efficiency of COSEA, we propose a variant of
contrastive loss for training the code search model, where the ground-truth
code should be distinguished from the most similar negative sample. We have
implemented a prototype of COSEA. Extensive experiments over existing public
datasets of Python and SQL have demonstrated that COSEA can achieve significant
improvements over state-of-the-art methods on code search tasks.