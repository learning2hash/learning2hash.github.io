---
layout: publication
title: 'PHPQ: Pyramid Hybrid Pooling Quantization For Efficient Fine-grained Image
  Retrieval'
authors: Ziyun Zeng, Jinpeng Wang, Bin Chen, Tao Dai, Shu-Tao Xia, Zhi Wang
conference: Pattern Recognition Letters Volume 178 2024 Pages 106-114
year: 2021
bibkey: zeng2021phpq
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.05206'}]
tags: [Compact Codes, Evaluation, Image Retrieval, Efficiency, Neural Hashing, Quantization,
  Scalability, Hashing Methods]
short_authors: Zeng et al.
---
Deep hashing approaches, including deep quantization and deep binary hashing,
have become a common solution to large-scale image retrieval due to their high
computation and storage efficiency. Most existing hashing methods cannot
produce satisfactory results for fine-grained retrieval, because they usually
adopt the outputs of the last CNN layer to generate binary codes. Since deeper
layers tend to summarize visual clues, e.g., texture, into abstract semantics,
e.g., dogs and cats, the feature produced by the last CNN layer is less
effective in capturing subtle but discriminative visual details that mostly
exist in shallow layers. To improve fine-grained image hashing, we propose
Pyramid Hybrid Pooling Quantization (PHPQ). Specifically, we propose a Pyramid
Hybrid Pooling (PHP) module to capture and preserve fine-grained semantic
information from multi-level features, which emphasizes the subtle
discrimination of different sub-categories. Besides, we propose a learnable
quantization module with a partial codebook attention mechanism, which helps to
optimize the most relevant codewords and improves the quantization.
Comprehensive experiments on two widely-used public benchmarks, i.e.,
CUB-200-2011 and Stanford Dogs, demonstrate that PHPQ outperforms
state-of-the-art methods.