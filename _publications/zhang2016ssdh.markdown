---
layout: publication
title: SSDH Semi45;supervised Deep Hashing For Large Scale Image Retrieval
authors: Zhang Jian, Peng Yuxin
conference: "Arxiv"
year: 2016
bibkey: zhang2016ssdh
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1607.08477"}
tags: ['ARXIV', 'Graph', 'Image Retrieval', 'Supervised']
---
Hashing methods have been widely used for efficient similarity retrieval on large scale image database. Traditional hashing methods learn hash functions to generate binary codes from hand45;crafted features which achieve limited accuracy since the hand45;crafted features cannot optimally represent the image content and preserve the semantic similarity. Recently several deep hashing methods have shown better performance because the deep architectures generate more discriminative feature representations. However these deep hashing methods are mainly designed for supervised scenarios which only exploit the semantic similarity information but ignore the underlying data structures. In this paper we propose the semi45;supervised deep hashing (SSDH) approach to perform more effective hash function learning by simultaneously preserving semantic similarity and underlying data structures. The main contributions are as follows (1) We propose a semi45;supervised loss to jointly minimize the empirical error on labeled data as well as the embedding error on both labeled and unlabeled data which can preserve the semantic similarity and capture the meaningful neighbors on the underlying data structures for effective hashing. (2) A semi45;supervised deep hashing network is designed to extensively exploit both labeled and unlabeled data in which we propose an online graph construction method to benefit from the evolving deep features during training to better capture semantic neighbors. To the best of our knowledge the proposed deep network is the first deep hashing method that can perform hash code learning and feature learning simultaneously in a semi45;supervised fashion. Experimental results on 5 widely45;used datasets show that our proposed approach outperforms the state45;of45;the45;art hashing methods.
