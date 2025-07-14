---
layout: publication
title: Deep Priority Hashing
authors: Zhangjie Cao, Ziping Sun, Mingsheng Long, Jianmin Wang, Philip S. Yu
conference: Arxiv
year: 2018
citations: 33
bibkey: cao2018deep
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.01238'}]
tags: [Applications, Deep Hashing, Quantization, Tools and Libraries, Loss Functions,
  Benchmarks and Datasets, Hashing Methods]
---
Deep hashing enables image retrieval by end-to-end learning of deep
representations and hash codes from training data with pairwise similarity
information. Subject to the distribution skewness underlying the similarity
information, most existing deep hashing methods may underperform for imbalanced
data due to misspecified loss functions. This paper presents Deep Priority
Hashing (DPH), an end-to-end architecture that generates compact and balanced
hash codes in a Bayesian learning framework. The main idea is to reshape the
standard cross-entropy loss for similarity-preserving learning such that it
down-weighs the loss associated to highly-confident pairs. This idea leads to a
novel priority cross-entropy loss, which prioritizes the training on uncertain
pairs over confident pairs. Also, we propose another priority quantization
loss, which prioritizes hard-to-quantize examples for generation of nearly
lossless hash codes. Extensive experiments demonstrate that DPH can generate
high-quality hash codes and yield state-of-the-art image retrieval results on
three datasets, ImageNet, NUS-WIDE, and MS-COCO.