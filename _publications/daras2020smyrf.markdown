---
layout: publication
title: 'SMYRF: Efficient Attention Using Asymmetric Clustering'
authors: Giannis Daras, Nikita Kitaev, Augustus Odena, Alexandros G. Dimakis
conference: Arxiv
year: 2020
bibkey: daras2020smyrf
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.05315'}]
tags: [Hashing Methods, Locality Sensitive Hashing]
short_authors: Daras et al.
---
We propose a novel type of balanced clustering algorithm to approximate
attention. Attention complexity is reduced from \(O(N^2)\) to \(O(N log N)\),
where \(N\) is the sequence length. Our algorithm, SMYRF, uses Locality Sensitive
Hashing (LSH) in a novel way by defining new Asymmetric transformations and an
adaptive scheme that produces balanced clusters. The biggest advantage of SMYRF
is that it can be used as a drop-in replacement for dense attention layers
without any retraining. On the contrary, prior fast attention methods impose
constraints (e.g. queries and keys share the same vector representations) and
require re-training from scratch. We apply our method to pre-trained
state-of-the-art Natural Language Processing and Computer Vision models and we
report significant memory and speed benefits. Notably, SMYRF-BERT outperforms
(slightly) BERT on GLUE, while using \(50%\) less memory. We also show that
SMYRF can be used interchangeably with dense attention before and after
training. Finally, we use SMYRF to train GANs with attention in high
resolutions. Using a single TPU, we were able to scale attention to 128x128=16k
and 256x256=65k tokens on BigGAN on CelebA-HQ.