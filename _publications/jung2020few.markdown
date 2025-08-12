---
layout: publication
title: Few-shot Learning With Geometric Constraints
authors: Hong-Gyu Jung, Seong-Whan Lee
conference: IEEE Transactions on Neural Networks and Learning Systems
year: 2020
bibkey: jung2020few
citations: 58
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.09151'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Hong-Gyu Jung, Seong-Whan Lee
---
In this article, we consider the problem of few-shot learning for
classification. We assume a network trained for base categories with a large
number of training examples, and we aim to add novel categories to it that have
only a few, e.g., one or five, training examples. This is a challenging
scenario because: 1) high performance is required in both the base and novel
categories; and 2) training the network for the new categories with a few
training examples can contaminate the feature space trained well for the base
categories. To address these challenges, we propose two geometric constraints
to fine-tune the network with a few training examples. The first constraint
enables features of the novel categories to cluster near the category weights,
and the second maintains the weights of the novel categories far from the
weights of the base categories. By applying the proposed constraints, we
extract discriminative features for the novel categories while preserving the
feature space learned for the base categories. Using public data sets for
few-shot learning that are subsets of ImageNet, we demonstrate that the
proposed method outperforms prevalent methods by a large margin.