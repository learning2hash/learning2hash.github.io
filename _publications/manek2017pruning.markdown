---
layout: publication
title: Pruning Convolutional Neural Networks For Image Instance Retrieval
authors: Manek Gaurav, Lin Jie, Chandrasekhar Vijay, Duan Lingyu, Giduthuri Sateesh,
  Li Xiaoli, Poggio Tomaso
conference: Arxiv
year: 2017
bibkey: manek2017pruning
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.05455'}]
tags: ["Tools-&-Libraries", "Evaluation", "Distance-Metric-Learning", "Datasets"]
short_authors: Manek et al.
---
In this work, we focus on the problem of image instance retrieval with deep
descriptors extracted from pruned Convolutional Neural Networks (CNN). The
objective is to heavily prune convolutional edges while maintaining retrieval
performance. To this end, we introduce both data-independent and data-dependent
heuristics to prune convolutional edges, and evaluate their performance across
various compression rates with different deep descriptors over several
benchmark datasets. Further, we present an end-to-end framework to fine-tune
the pruned network, with a triplet loss function specially designed for the
retrieval task. We show that the combination of heuristic pruning and
fine-tuning offers 5x compression rate without considerable loss in retrieval
performance.