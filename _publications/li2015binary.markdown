---
layout: publication
title: 'Binary Speaker Embedding'
authors: Lantian Li, Dong Wang, Chao Xing, Kaimin Yu, Thomas Fang Zheng
conference: "Arxiv"
year: 2015
citations: 4
bibkey: li2015binary
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1510.05937'}
tags: ['Hashing Fundamentals', 'Evaluation Metrics', 'Hashing Methods']
---
The popular i-vector model represents speakers as low-dimensional continuous
vectors (i-vectors), and hence it is a way of continuous speaker embedding. In
this paper, we investigate binary speaker embedding, which transforms i-vectors
to binary vectors (codes) by a hash function. We start from locality sensitive
hashing (LSH), a simple binarization approach where binary codes are derived
from a set of random hash functions. A potential problem of LSH is that the
randomly sampled hash functions might be suboptimal. We therefore propose an
improved Hamming distance learning approach, where the hash function is learned
by a variable-sized block training that projects each dimension of the original
i-vectors to variable-sized binary codes independently. Our experiments show
that binary speaker embedding can deliver competitive or even better results on
both speaker verification and identification tasks, while the memory usage and
the computation cost are significantly reduced.
