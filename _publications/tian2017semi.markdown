---
layout: publication
title: Semi-supervised Multimodal Hashing
authors: Tian Dayong, Gong Maoguo, Zhou Deyun, Shi Jiao, Lei Yu
conference: Arxiv
year: 2017
bibkey: tian2017semi
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.03404'}]
tags: ["Hashing-Methods", "Compact-Codes", "Supervised", "Evaluation", "Unsupervised"]
short_authors: Tian et al.
---
Retrieving nearest neighbors across correlated data in multiple modalities,
such as image-text pairs on Facebook and video-tag pairs on YouTube, has become
a challenging task due to the huge amount of data. Multimodal hashing methods
that embed data into binary codes can boost the retrieving speed and reduce
storage requirement. As unsupervised multimodal hashing methods are usually
inferior to supervised ones, while the supervised ones requires too much
manually labeled data, the proposed method in this paper utilizes a part of
labels to design a semi-supervised multimodal hashing method. It first computes
the transformation matrices for data matrices and label matrix. Then, with
these transformation matrices, fuzzy logic is introduced to estimate a label
matrix for unlabeled data. Finally, it uses the estimated label matrix to learn
hashing functions for data in each modality to generate a unified binary code
matrix. Experiments show that the proposed semi-supervised method with 50%
labels can get a medium performance among the compared supervised ones and
achieve an approximate performance to the best supervised method with 90%
labels. With only 10% labels, the proposed method can still compete with the
worst compared supervised one.