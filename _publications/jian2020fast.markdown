---
layout: publication
title: "Fast top-K Cosine Similarity Search through XOR-Friendly Binary Quantization on
GPUs"
authors: Jian Xiaozheng, Lu Jianqiu, Yuan Zexi, Li Ao
conference: Arxiv
year: 2020
bibkey: jian2020fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2008.02002"}
tags: ['ARXIV', 'Quantisation', 'TIP']
---
We explore the use of GPU for accelerating large scale nearest neighbor search
and we propose a fast vector-quantization-based exhaustive nearest neighbor
search algorithm that can achieve high accuracy without any indexing
construction specifically designed for cosine similarity. This algorithm uses a
novel XOR-friendly binary quantization method to encode floating-point numbers
such that high-complexity multiplications can be optimized as low-complexity
bitwise operations. Experiments show that, our quantization method takes short
preprocessing time, and helps make the search speed of our exhaustive search
method much more faster than that of popular approximate nearest neighbor
algorithms when high accuracy is needed.
