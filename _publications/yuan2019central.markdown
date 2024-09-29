---
layout: publication
title: Central Similarity Quantization For Efficient Image And Video Retrieval
authors: Yuan Li, Wang Tao, Zhang Xiaopeng, Tay Francis Eh, Jie Zequn, Liu Wei, Feng Jiashi
conference: "Arxiv"
year: 2019
bibkey: yuan2019central
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1908.00347"}
  - {name: "Code", url: "https://github.com/yuanli2333/Hadamard&#45;Matrix&#45;for&#45;hashing&#125;"}
tags: ['ARXIV', 'Has Code', 'Independent', 'Quantisation', 'Video Retrieval']
---
Existing data45;dependent hashing methods usually learn hash functions from pairwise or triplet data relationships which only capture the data similarity locally and often suffer from low learning efficiency and low collision rate. In this work we propose a new emph123;global125; similarity metric termed as emph123;central similarity125; with which the hash codes of similar data pairs are encouraged to approach a common center and those for dissimilar pairs to converge to different centers to improve hash learning efficiency and retrieval accuracy. We principally formulate the computation of the proposed central similarity metric by introducing a new concept i.e. emph123;hash center125; that refers to a set of data points scattered in the Hamming space with a sufficient mutual distance between each other. We then provide an efficient method to construct well separated hash centers by leveraging the Hadamard matrix and Bernoulli distributions. Finally we propose the Central Similarity Quantization (CSQ) that optimizes the central similarity between data points w.r.t. their hash centers instead of optimizing the local similarity. CSQ is generic and applicable to both image and video hashing scenarios. Extensive experiments on large45;scale image and video retrieval tasks demonstrate that CSQ can generate cohesive hash codes for similar data pairs and dispersed hash codes for dissimilar pairs achieving a noticeable boost in retrieval performance i.e. 337;45;2037; in mAP over the previous state45;of45;the45;arts. The code is at url123;https://github.com/yuanli2333/Hadamard&#45;Matrix&#45;for&#45;hashing&#125;
