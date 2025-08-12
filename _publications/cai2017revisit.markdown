---
layout: publication
title: A Revisit On Deep Hashings For Large-scale Content Based Image Retrieval
authors: Deng Cai, Xiuye Gu, Chaoqi Wang
conference: Arxiv
year: 2017
bibkey: cai2017revisit
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.06016'}]
tags: ["Compact Codes", "Hashing Methods", "Image Retrieval", "Neural Hashing", "Scalability"]
short_authors: Deng Cai, Xiuye Gu, Chaoqi Wang
---
There is a growing trend in studying deep hashing methods for content-based
image retrieval (CBIR), where hash functions and binary codes are learnt using
deep convolutional neural networks and then the binary codes can be used to do
approximate nearest neighbor (ANN) search. All the existing deep hashing papers
report their methods' superior performance over the traditional hashing methods
according to their experimental results. However, there are serious flaws in
the evaluations of existing deep hashing papers: (1) The datasets they used are
too small and simple to simulate the real CBIR situation. (2) They did not
correctly include the search time in their evaluation criteria, while the
search time is crucial in real CBIR systems. (3) The performance of some
unsupervised hashing algorithms (e.g., LSH) can easily be boosted if one uses
multiple hash tables, which is an important factor should be considered in the
evaluation while most of the deep hashing papers failed to do so.
  We re-evaluate several state-of-the-art deep hashing methods with a carefully
designed experimental setting. Empirical results reveal that the performance of
these deep hashing methods are inferior to multi-table IsoH, a very simple
unsupervised hashing method. Thus, the conclusions in all the deep hashing
papers should be carefully re-examined.