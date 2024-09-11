---
layout: publication
title: "Central Similarity Hashing for Efficient Image and Video Retrieval"
authors: Li Yuan, Tao Wang, Xiaopeng Zhang, Zequn Jie, Francis EH Tay, Jiashi Feng
conference: CVPR
year: 2020
bibkey: yuan2020central
additional_links:
   - {name: "PDF", url: "https://arxiv.org/pdf/1908.00347.pdf"}
   - {name: "Code", url: "https://github.com/yuanli2333/Hadamard-Matrix-for-hashing"}
tags: ["CVPR", "Video Retrieval", "Has Code", "Deep Learning"]
---
Existing data-dependent hashing methods usually learn
hash functions from the pairwise or triplet data relationships, which only capture the data similarity locally, and
often suffer low learning efficiency and low collision rate.
In this work, we propose a new global similarity metric,
termed as central similarity, with which the hash codes for
similar data pairs are encouraged to approach a common
center and those for dissimilar pairs to converge to different centers, to improve hash learning efficiency and retrieval accuracy. We principally formulate the computation of the proposed central similarity metric by introducing a new concept, i.e. hash center that refers to a set
of data points scattered in the Hamming space with sufficient mutual distance between each other. We then provide an efficient method to construct well separated hash
centers by leveraging the Hadamard matrix and Bernoulli
distributions. Finally, we propose the Central Similarity
Hashing (CSH) that optimizes the central similarity between data points w.r.t. their hash centers instead of optimizing the local similarity. The CSH is generic and applicable to both image and video hashing. Extensive experiments on large-scale image and video retrieval demonstrate CSH can generate cohesive hash codes for similar
data pairs and dispersed hash codes for dissimilar pairs,
and achieve noticeable boost in retrieval performance, i.e.
3%-20% in mAP over the previous state-of-the-art. The
codes are in: https://github.com/yuanli2333/
Hadamard-Matrix-for-hashing
