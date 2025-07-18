---
layout: publication
title: Learning Discrete Representations Via Information Maximizing Self-augmented
  Training
authors: Hu et al.
conference: Arxiv
year: 2017
bibkey: hu2017learning
citations: 206
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.08720'}]
tags: [DATASETS, Hashing Methods, Evaluation]
---
Learning discrete representations of data is a central machine learning task
because of the compactness of the representations and ease of interpretation.
The task includes clustering and hash learning as special cases. Deep neural
networks are promising to be used because they can model the non-linearity of
data and scale to large datasets. However, their model complexity is huge, and
therefore, we need to carefully regularize the networks in order to learn
useful representations that exhibit intended invariance for applications of
interest. To this end, we propose a method called Information Maximizing
Self-Augmented Training (IMSAT). In IMSAT, we use data augmentation to impose
the invariance on discrete representations. More specifically, we encourage the
predicted representations of augmented data points to be close to those of the
original data points in an end-to-end fashion. At the same time, we maximize
the information-theoretic dependency between data and their predicted discrete
representations. Extensive experiments on benchmark datasets show that IMSAT
produces state-of-the-art results for both clustering and unsupervised hash
learning.