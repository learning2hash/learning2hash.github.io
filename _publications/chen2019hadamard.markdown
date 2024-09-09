---
layout: publication
title: "Hadamard Codebook Based Deep Hashing"
authors: Chen Shen, Cao Liujuan, Lin Mingbao, Wang Yan, Sun Xiaoshuai, Wu Chenglin, Qiu Jingfei, Ji Rongrong
conference: Arxiv
year: 2019
bibkey: chen2019hadamard
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/1910.09182"}
tags: ['ARXIV', 'Image Retrieval', 'Supervised']
---
As an approximate nearest neighbor search technique, hashing has been widely applied in large-scale image retrieval due to its excellent efficiency. Most supervised deep hashing methods have similar loss designs with embedding learning, while quantizing the continuous high-dim feature into compact binary space. We argue that the existing deep hashing schemes are defective in two issues that seriously affect the performance, i.e., bit independence and bit balance. The former refers to hash codes of different classes should be independent of each other, while the latter means each bit should have a balanced distribution of +1s and -1s. In this paper, we propose a novel supervised deep hashing method, termed Hadamard Codebook based Deep Hashing (HCDH), which solves the above two problems in a unified formulation. Specifically, we utilize an off-the-shelf algorithm to generate a binary Hadamard codebook to satisfy the requirement of bit independence and bit balance, which subsequently serves as the desired outputs of the hash functions learning. We also introduce a projection matrix to solve the inconsistency between the order of Hadamard matrix and the number of classes. Besides, the proposed HCDH further exploits the supervised labels by constructing a classifier on top of the outputs of hash functions. Extensive experiments demonstrate that HCDH can yield discriminative and balanced binary codes, which well outperforms many state-of-the-arts on three widely-used benchmarks.