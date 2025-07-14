---
layout: publication
title: Discrete Hashing With Deep Neural Network
authors: Thanh-toan Do, Anh-zung Doan, Ngai-man Cheung
conference: Arxiv
year: 2015
citations: 10
bibkey: do2015discrete
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1508.07148'}]
tags: [Tools and Libraries, Evaluation Metrics, Supervised, Benchmarks and Datasets,
  Hashing Methods]
---
This paper addresses the problem of learning binary hash codes for large
scale image search by proposing a novel hashing method based on deep neural
network. The advantage of our deep model over previous deep model used in
hashing is that our model contains necessary criteria for producing good codes
such as similarity preserving, balance and independence. Another advantage of
our method is that instead of relaxing the binary constraint of codes during
the learning process as most previous works, in this paper, by introducing the
auxiliary variable, we reformulate the optimization into two sub-optimization
steps allowing us to efficiently solve binary constraints without any
relaxation.
  The proposed method is also extended to the supervised hashing by leveraging
the label information such that the learned binary codes preserve the pairwise
label of inputs.
  The experimental results on three benchmark datasets show the proposed
methods outperform state-of-the-art hashing methods.