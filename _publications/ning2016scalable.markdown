---
layout: publication
title: 'Scalable Image Retrieval By Sparse Product Quantization'
authors: Qingqun Ning, Jianke Zhu, Zhiyuan Zhong, Steven C. H. Hoi, Chun Chen
conference: "Arxiv"
year: 2016
citations: 29
bibkey: ning2016scalable
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1603.04614'}
tags: ['Applications', 'Approximate Nearest Neighbor Search', 'Indexing', 'Quantization and Compression', 'Tools and Libraries', 'ANN Search', 'Quantization', 'Hashing for Real-World Applications']
---
Fast Approximate Nearest Neighbor (ANN) search technique for high-dimensional
feature indexing and retrieval is the crux of large-scale image retrieval. A
recent promising technique is Product Quantization, which attempts to index
high-dimensional image features by decomposing the feature space into a
Cartesian product of low dimensional subspaces and quantizing each of them
separately. Despite the promising results reported, their quantization approach
follows the typical hard assignment of traditional quantization methods, which
may result in large quantization errors and thus inferior search performance.
Unlike the existing approaches, in this paper, we propose a novel approach
called Sparse Product Quantization (SPQ) to encoding the high-dimensional
feature vectors into sparse representation. We optimize the sparse
representations of the feature vectors by minimizing their quantization errors,
making the resulting representation is essentially close to the original data
in practice. Experiments show that the proposed SPQ technique is not only able
to compress data, but also an effective encoding technique. We obtain
state-of-the-art results for ANN search on four public image datasets and the
promising results of content-based image retrieval further validate the
efficacy of our proposed method.
