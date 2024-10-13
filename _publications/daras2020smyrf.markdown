---
layout: publication
title: SMYRF - Efficient Attention Using Asymmetric Clustering
authors: Giannis Daras, Nikita Kitaev, Augustus Odena, Alexandros G. Dimakis
conference: "Neural Information Processing Systems"
year: 2020
bibkey: daras2020smyrf
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2020/hash/47d40767c7e9df50249ebfd9c7cfff77-Abstract.html"}
tags: ['LSH', 'NEURIPS', 'Unsupervised']
---
We propose a novel type of balanced clustering algorithm to approximate attention. Attention complexity is reduced from \{O(N^2)\} to \{O(N log N)\}, where N is the sequence length. Our algorithm, SMYRF, uses Locality Sensitive Hashing (LSH) in a novel way by defining new Asymmetric transformations and an adaptive scheme that produces balanced clusters. The biggest advantage of SMYRF is that it can be used as a drop-in replacement for dense attention layers without any retraining. On the contrary, prior fast attention methods impose constraints (e.g. tight queries and keys) and require re-training from scratch. We apply our method to pre-trained state-of-the-art Natural Language Processing and Computer Vision models and we report significant memory and speed benefits. Notably, SMYRF-BERT outperforms (slightly) BERT on GLUE, while using 50% less memory. We also show that SMYRF can be used interchangeably with dense attention before and after training. Finally, we use SMYRF to train GANs with attention in high resolutions.  Using a single TPU, we train BigGAN on Celeba-HQ, with attention at resolution 128x128 and 256x256, capable of generating realistic human faces.
