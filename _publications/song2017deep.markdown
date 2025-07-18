---
layout: publication
title: Deep Discrete Hashing With Self-supervised Pairwise Labels
authors: Song et al.
conference: Lecture Notes in Computer Science
year: 2017
bibkey: song2017deep
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.02112'}]
tags: [Image Retrieval, DATASETS, Hashing Methods, Compact Codes, Neural Hashing,
  Tools & Libraries, Evaluation]
---
Hashing methods have been widely used for applications of large-scale image
retrieval and classification. Non-deep hashing methods using handcrafted
features have been significantly outperformed by deep hashing methods due to
their better feature representation and end-to-end learning framework. However,
the most striking successes in deep hashing have mostly involved discriminative
models, which require labels. In this paper, we propose a novel unsupervised
deep hashing method, named Deep Discrete Hashing (DDH), for large-scale image
retrieval and classification. In the proposed framework, we address two main
problems: 1) how to directly learn discrete binary codes? 2) how to equip the
binary representation with the ability of accurate image retrieval and
classification in an unsupervised way? We resolve these problems by introducing
an intermediate variable and a loss function steering the learning process,
which is based on the neighborhood structure in the original space.
Experimental results on standard datasets (CIFAR-10, NUS-WIDE, and Oxford-17)
demonstrate that our DDH significantly outperforms existing hashing methods by
large margin in terms of~mAP for image retrieval and object recognition. Code
is available at https://github.com/htconquer/ddh.