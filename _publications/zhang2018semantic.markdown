---
layout: publication
title: Semantic Cluster Unary Loss For Efficient Deep Hashing
authors: Zhang Shifeng, Li Jianmin, Zhang Bo
conference: "IEEE Transactions on Image Processing"
year: 2018
bibkey: zhang2018semantic
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1805.08705"}
tags: ['Deep Learning', 'Supervised']
---
Hashing method maps similar data to binary hashcodes with smaller hamming distance which has received a broad attention due to its low storage cost and fast retrieval speed. With the rapid development of deep learning deep hashing methods have achieved promising results in efficient information retrieval. Most of the existing deep hashing methods adopt pairwise or triplet losses to deal with similarities underlying the data but the training is difficult and less efficient because (O(n^2)) data pairs and (O(n^3)) triplets are involved. To address these issues we propose a novel deep hashing algorithm with unary loss which can be trained very efficiently. We first of all introduce a Unary Upper Bound of the traditional triplet loss thus reducing the complexity to (O(n)) and bridging the classification-based unary loss and the triplet loss. Second we propose a novel Semantic Cluster Deep Hashing (SCDH) algorithm by introducing a modified Unary Upper Bound loss named Semantic Cluster Unary Loss (SCUL). The resultant hashcodes form several compact clusters which means hashcodes in the same cluster have similar semantic information. We also demonstrate that the proposed SCDH is easy to be extended to semi-supervised settings by incorporating the state-of-the-art semi-supervised learning algorithms. Experiments on large-scale datasets show that the proposed method is superior to state-of-the-art hashing algorithms.
