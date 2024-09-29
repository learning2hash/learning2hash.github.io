---
layout: publication
title: Mihash Online Hashing With Mutual Information
authors: Cakir Fatih, He Kun, Bargal Sarah Adel, Sclaroff Stan
conference: "Arxiv"
year: 2017
bibkey: cakir2017mihash
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1703.08919"}
tags: ['ARXIV', 'Image Retrieval', 'Independent', 'Streaming Data']
---
Learning45;based hashing methods are widely used for nearest neighbor retrieval and recently online hashing methods have demonstrated good performance45;complexity trade45;offs by learning hash functions from streaming data. In this paper we first address a key challenge for online hashing the binary codes for indexed data must be recomputed to keep pace with updates to the hash functions. We propose an efficient quality measure for hash functions based on an information45;theoretic quantity mutual information and use it successfully as a criterion to eliminate unnecessary hash table updates. Next we also show how to optimize the mutual information objective using stochastic gradient descent. We thus develop a novel hashing method MIHash that can be used in both online and batch settings. Experiments on image retrieval benchmarks (including a 2.5M image dataset) confirm the effectiveness of our formulation both in reducing hash table recomputations and in learning high45;quality hash functions.
