---
layout: publication
title: Supervised Deep Hashing for Hierarchical Labeled Data
authors: Wang et al.
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2018
bibkey: wang2018supervised
citations: 26
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.02088'}]
tags: ["AAAI", "Hashing-Methods", "Neural-Hashing", "Supervised"]
---
Recently, hashing methods have been widely used in large-scale image
retrieval. However, most existing hashing methods did not consider the
hierarchical relation of labels, which means that they ignored the rich
information stored in the hierarchy. Moreover, most of previous works treat
each bit in a hash code equally, which does not meet the scenario of
hierarchical labeled data. In this paper, we propose a novel deep hashing
method, called supervised hierarchical deep hashing (SHDH), to perform hash
code learning for hierarchical labeled data. Specifically, we define a novel
similarity formula for hierarchical labeled data by weighting each layer, and
design a deep convolutional neural network to obtain a hash code for each data
point. Extensive experiments on several real-world public datasets show that
the proposed method outperforms the state-of-the-art baselines in the image
retrieval task.