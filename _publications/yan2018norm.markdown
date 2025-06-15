---
layout: publication
title: 'Norm-range Partition: A Universal Catalyst For LSH Based Maximum Inner Product Search (MIPS)'
authors: Xiao Yan, Xinyan Dai, Jie Liu, Kaiwen Zhou, James Cheng
conference: "Arxiv"
year: 2018
citations: 0
bibkey: yan2018norm
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1810.09104'}
tags: ['Hashing Fundamentals', 'Evaluation Metrics', 'Hashing Methods', 'Tools and Libraries']
---
Recently, locality sensitive hashing (LSH) was shown to be effective for MIPS
and several algorithms including \\(L_2\\)-ALSH, Sign-ALSH and Simple-LSH have been
proposed. In this paper, we introduce the norm-range partition technique, which
partitions the original dataset into sub-datasets containing items with similar
2-norms and builds hash index independently for each sub-dataset. We prove that
norm-range partition reduces the query processing complexity for all existing
LSH based MIPS algorithms under mild conditions. The key to performance
improvement is that norm-range partition allows to use smaller normalization
factor most sub-datasets. For efficient query processing, we also formulate a
unified framework to rank the buckets from the hash indexes of different
sub-datasets. Experiments on real datasets show that norm-range partition
significantly reduces the number of probed for LSH based MIPS algorithms when
achieving the same recall.
