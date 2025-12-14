---
layout: publication
title: Sparse-inductive Generative Adversarial Hashing For Nearest Neighbor Search
authors: Hong Liu
conference: Arxiv
year: 2023
bibkey: liu2023sparse
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.06928'}]
tags: [Compact Codes, Evaluation, Supervised, Neural Hashing, Quantization, Robustness,
  Scalability, Unsupervised, Tools & Libraries, Hashing Methods]
short_authors: Hong Liu
---
Unsupervised hashing has received extensive research focus on the past
decade, which typically aims at preserving a predefined metric (i.e. Euclidean
metric) in the Hamming space. To this end, the encoding functions of the
existing hashing are typically quasi-isometric, which devote to reducing the
quantization loss from the target metric space to the discrete Hamming space.
However, it is indeed problematic to directly minimize such error, since such
mentioned two metric spaces are heterogeneous, and the quasi-isometric mapping
is non-linear. The former leads to inconsistent feature distributions, while
the latter leads to problematic optimization issues. In this paper, we propose
a novel unsupervised hashing method, termed Sparsity-Induced Generative
Adversarial Hashing (SiGAH), to encode large-scale high-dimensional features
into binary codes, which well solves the two problems through a generative
adversarial training framework. Instead of minimizing the quantization loss,
our key innovation lies in enforcing the learned Hamming space to have similar
data distribution to the target metric space via a generative model. In
particular, we formulate a ReLU-based neural network as a generator to output
binary codes and an MSE-loss based auto-encoder network as a discriminator,
upon which a generative adversarial learning is carried out to train hash
functions. Furthermore, to generate the synthetic features from the hash codes,
a compressed sensing procedure is introduced into the generative model, which
enforces the reconstruction boundary of binary codes to be consistent with that
of original features. Finally, such generative adversarial framework can be
trained via the Adam optimizer. Experimental results on four benchmarks, i.e.,
Tiny100K, GIST1M, Deep1M, and MNIST, have shown that the proposed SiGAH has
superior performance over the state-of-the-art approaches.