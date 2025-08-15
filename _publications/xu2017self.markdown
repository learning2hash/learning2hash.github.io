---
layout: publication
title: Self-taught Convolutional Neural Networks For Short Text Clustering
authors: Jiaming Xu, Bo Xu, Peng Wang, Suncong Zheng, Guanhua Tian, Jun Zhao, Bo Xu
conference: Neural Networks
year: 2017
bibkey: xu2017self
citations: 208
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1701.00185'}]
tags: ["Compact Codes", "Unsupervised"]
short_authors: Xu et al.
---
Short text clustering is a challenging problem due to its sparseness of text
representation. Here we propose a flexible Self-Taught Convolutional neural
network framework for Short Text Clustering (dubbed STC^2), which can flexibly
and successfully incorporate more useful semantic features and learn non-biased
deep text representation in an unsupervised manner. In our framework, the
original raw text features are firstly embedded into compact binary codes by
using one existing unsupervised dimensionality reduction methods. Then, word
embeddings are explored and fed into convolutional neural networks to learn
deep feature representations, meanwhile the output units are used to fit the
pre-trained binary codes in the training process. Finally, we get the optimal
clusters by employing K-means to cluster the learned representations. Extensive
experimental results demonstrate that the proposed framework is effective,
flexible and outperform several popular clustering methods when tested on three
public short text datasets.