---
layout: publication
title: 'Transductive Zero-shot Hashing For Multilabel Image Retrieval'
authors: Qin Zou, Zheng Zhang, Ling Cao, Long Chen, Song Wang
conference: "IEEE Transactions on Neural Networks and Learning Systems 2020"
year: 2019
citations: 10
bibkey: zou2019transductive
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1911.07192'}
tags: ['Cross-Modal', 'Deep', 'Quantisation', 'Retrieval Models', 'Evaluation', 'Training Strategy', 'Datasets', 'Vector Indexing', 'Quantization', 'Similarity Learning', 'Hashing', 'Applications']
---
Hash coding has been widely used in approximate nearest neighbor search for
large-scale image retrieval. Given semantic annotations such as class labels
and pairwise similarities of the training data, hashing methods can learn and
generate effective and compact binary codes. While some newly introduced images
may contain undefined semantic labels, which we call unseen images, zeor-shot
hashing techniques have been studied. However, existing zeor-shot hashing
methods focus on the retrieval of single-label images, and cannot handle
multi-label images. In this paper, for the first time, a novel transductive
zero-shot hashing method is proposed for multi-label unseen image retrieval. In
order to predict the labels of the unseen/target data, a visual-semantic bridge
is built via instance-concept coherence ranking on the seen/source data. Then,
pairwise similarity loss and focal quantization loss are constructed for
training a hashing model using both the seen/source and unseen/target data.
Extensive evaluations on three popular multi-label datasets demonstrate that,
the proposed hashing method achieves significantly better results than the
competing methods.
