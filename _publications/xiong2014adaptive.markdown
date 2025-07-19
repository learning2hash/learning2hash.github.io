---
layout: publication
title: 'Adaptive Quantization For Hashing: An Information-based Approach To Learning
  Binary Codes'
authors: Xiong et al.
conference: Proceedings of the 2014 SIAM International Conference on Data Mining
year: 2014
bibkey: xiong2014adaptive
citations: 13
additional_links: [{name: Paper, url: 'https://www.cse.buffalo.edu//~jcorso/pubs/cxiong_SDM2014_adahash.pdf'}]
tags: [Quantization, Hashing Methods, Compact Codes]
---
Large-scale data mining and retrieval applications have
increasingly turned to compact binary data representations
as a way to achieve both fast queries and efficient
data storage; many algorithms have been proposed for
learning effective binary encodings. Most of these algorithms
focus on learning a set of projection hyperplanes
for the data and simply binarizing the result from each
hyperplane, but this neglects the fact that informativeness
may not be uniformly distributed across the projections.
In this paper, we address this issue by proposing
a novel adaptive quantization (AQ) strategy that
adaptively assigns varying numbers of bits to different
hyperplanes based on their information content. Our
method provides an information-based schema that preserves
the neighborhood structure of data points, and
we jointly find the globally optimal bit-allocation for
all hyperplanes. In our experiments, we compare with
state-of-the-art methods on four large-scale datasets
and find that our adaptive quantization approach significantly
improves on traditional hashing methods.