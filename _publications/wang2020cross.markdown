---
layout: publication
title: Cross-batch Memory For Embedding Learning
authors: Xun Wang, Haozhi Zhang, Weilin Huang, Matthew R. Scott
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: wang2020cross
citations: 221
additional_links: [{name: Code, url: 'https://github'}, {name: Paper, url: 'https://arxiv.org/abs/1912.06798'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval", "Scalability"]
short_authors: Wang et al.
---
Mining informative negative instances are of central importance to deep
metric learning (DML), however this task is intrinsically limited by mini-batch
training, where only a mini-batch of instances is accessible at each iteration.
In this paper, we identify a "slow drift" phenomena by observing that the
embedding features drift exceptionally slow even as the model parameters are
updating throughout the training process. This suggests that the features of
instances computed at preceding iterations can be used to considerably
approximate their features extracted by the current model. We propose a
cross-batch memory (XBM) mechanism that memorizes the embeddings of past
iterations, allowing the model to collect sufficient hard negative pairs across
multiple mini-batches - even over the whole dataset. Our XBM can be directly
integrated into a general pair-based DML framework, where the XBM augmented DML
can boost performance considerably. In particular, without bells and whistles,
a simple contrastive loss with our XBM can have large R@1 improvements of
12%-22.5% on three large-scale image retrieval datasets, surpassing the most
sophisticated state-of-the-art methods, by a large margin. Our XBM is
conceptually simple, easy to implement - using several lines of codes, and is
memory efficient - with a negligible 0.2 GB extra GPU memory. Code is available
at: https://github.com/MalongTech/research-xbm.