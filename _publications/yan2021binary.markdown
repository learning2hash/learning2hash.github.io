---
layout: publication
title: Binary Code Based Hash Embedding For Web-scale Applications
authors: Yan Bencheng, Wang Pengjie, Liu Jinquan, Lin Wei, Lee Kuang-chih, Xu Jian,
  Zheng Bo
conference: Proceedings of the 30th ACM International Conference on Information &amp;
  Knowledge Management
year: 2021
bibkey: yan2021binary
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.02471'}]
tags: ["Evaluation", "Compact-Codes", "CIKM", "Recommender-Systems", "Large-Scale-Search", "Scalability"]
short_authors: Yan et al.
---
Nowadays, deep learning models are widely adopted in web-scale applications
such as recommender systems, and online advertising. In these applications,
embedding learning of categorical features is crucial to the success of deep
learning models. In these models, a standard method is that each categorical
feature value is assigned a unique embedding vector which can be learned and
optimized. Although this method can well capture the characteristics of the
categorical features and promise good performance, it can incur a huge memory
cost to store the embedding table, especially for those web-scale applications.
Such a huge memory cost significantly holds back the effectiveness and
usability of EDRMs. In this paper, we propose a binary code based hash
embedding method which allows the size of the embedding table to be reduced in
arbitrary scale without compromising too much performance. Experimental
evaluation results show that one can still achieve 99% performance even if the
embedding table size is reduced 1000\\(\times\\) smaller than the original one with
our proposed method.