---
layout: publication
title: 'Fast Top-k Cosine Similarity Search Through Xor-friendly Binary Quantization On Gpus'
authors: Xiaozheng Jian, Jianqiu Lu, Zexi Yuan, Ao Li
conference: "Arxiv"
year: 2020
citations: 2
bibkey: jian2020fast
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2008.02002'}
tags: ['Quantisation', 'Retrieval Models', 'Unimodal', 'Shallow', 'Vector Indexing', 'Quantization', 'Hashing']
---
We explore the use of GPU for accelerating large scale nearest neighbor
search and we propose a fast vector-quantization-based exhaustive nearest
neighbor search algorithm that can achieve high accuracy without any indexing
construction specifically designed for cosine similarity. This algorithm uses a
novel XOR-friendly binary quantization method to encode floating-point numbers
such that high-complexity multiplications can be optimized as low-complexity
bitwise operations. Experiments show that, our quantization method takes short
preprocessing time, and helps make the search speed of our exhaustive search
method much more faster than that of popular approximate nearest neighbor
algorithms when high accuracy is needed.
