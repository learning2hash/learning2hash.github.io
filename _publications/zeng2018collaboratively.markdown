---
layout: publication
title: Collaboratively Weighting Deep And Classic Representation Via L2 Regularization
  For Image Classification
authors: Shaoning Zeng, Bob Zhang, Yanghao Zhang, Jianping Gou
conference: PMLR Volume 95 Asian Conference on Machine Learning 14-16 November 2018
year: 2018
bibkey: zeng2018collaboratively
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1802.07589'}]
tags: []
short_authors: Zeng et al.
---
Deep convolutional neural networks provide a powerful feature learning
capability for image classification. The deep image features can be utilized to
deal with many image understanding tasks like image classification and object
recognition. However, the robustness obtained in one dataset can be hardly
reproduced in the other domain, which leads to inefficient models far from
state-of-the-art. We propose a deep collaborative weight-based classification
(DeepCWC) method to resolve this problem, by providing a novel option to fully
take advantage of deep features in classic machine learning. It firstly
performs the L2-norm based collaborative representation on the original images,
as well as the deep features extracted by deep CNN models. Then, two distance
vectors, obtained based on the pair of linear representations, are fused
together via a novel collaborative weight. This collaborative weight enables
deep and classic representations to weigh each other. We observed the
complementarity between two representations in a series of experiments on 10
facial and object datasets. The proposed DeepCWC produces very promising
classification results, and outperforms many other benchmark methods,
especially the ones claimed for Fashion-MNIST. The code is going to be
published in our public repository.