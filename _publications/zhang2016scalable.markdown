---
layout: publication
title: "Scalable Discrete Supervised Hash Learning with Asymmetric Matrix
Factorization"
authors: Zhang Shifeng, Li Jianmin, Guo Jinma, Zhang Bo
conference: "Arxiv"
year: 2016
bibkey: zhang2016scalable
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1609.08740"}
tags: ['ARXIV', 'Supervised']
---
Hashing method maps similar data to binary hashcodes with smaller hamming
distance, and it has received a broad attention due to its low storage cost and
fast retrieval speed. However, the existing limitations make the present
algorithms difficult to deal with large-scale datasets: (1) discrete constraints
are involved in the learning of the hash function; (2) pairwise or triplet
similarity is adopted to generate efficient hashcodes, resulting both time and
space complexity are greater than O(n^2). To address these issues, we propose a
novel discrete supervised hash learning framework which can be scalable to
large-scale datasets. First, the discrete learning procedure is decomposed into
a binary classifier learning scheme and binary codes learning scheme, which
makes the learning procedure more efficient. Second, we adopt the Asymmetric
Low-rank Matrix Factorization and propose the Fast Clustering-based Batch
Coordinate Descent method, such that the time and space complexity is reduced to
O(n). The proposed framework also provides a flexible paradigm to incorporate
with arbitrary hash function, including deep neural networks and kernel methods.
Experiments on large-scale datasets demonstrate that the proposed method is
superior or comparable with state-of-the-art hashing algorithms.
