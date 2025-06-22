---
layout: publication
title: Simultaneous Feature Aggregating And Hashing For Compact Binary Code Learning
authors: Thanh-toan Do et al.
conference: Arxiv
year: 2019
citations: 19
bibkey: do2019simultaneous
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.11820'}]
tags: [Hashing Methods, Unsupervised, Supervised, Evaluation Metrics, Applications,
  Benchmarks and Datasets]
---
Representing images by compact hash codes is an attractive approach for
large-scale content-based image retrieval. In most state-of-the-art
hashing-based image retrieval systems, for each image, local descriptors are
first aggregated as a global representation vector. This global vector is then
subjected to a hashing function to generate a binary hash code. In previous
works, the aggregating and the hashing processes are designed independently.
Hence these frameworks may generate suboptimal hash codes. In this paper, we
first propose a novel unsupervised hashing framework in which feature
aggregating and hashing are designed simultaneously and optimized jointly.
Specifically, our joint optimization generates aggregated representations that
can be better reconstructed by some binary codes. This leads to more
discriminative binary hash codes and improved retrieval accuracy. In addition,
the proposed method is flexible. It can be extended for supervised hashing.
When the data label is available, the framework can be adapted to learn binary
codes which minimize the reconstruction loss w.r.t. label vectors. Furthermore,
we also propose a fast version of the state-of-the-art hashing method Binary
Autoencoder to be used in our proposed frameworks. Extensive experiments on
benchmark datasets under various settings show that the proposed methods
outperform state-of-the-art unsupervised and supervised hashing methods.