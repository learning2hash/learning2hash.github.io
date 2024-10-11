---
layout: publication
title: Local Density Estimation In High Dimensions
authors: Wu Xian, Charikar Moses, Natchu Vishnu
conference: "Arxiv"
year: 2018
bibkey: wu2018local
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1809.07471"}
tags: ['ARXIV', 'Independent', 'LSH']
---
An important question that arises in the study of high dimensional vector representations learned from data is: given a set $\mathcal\{D\}$ of vectors and a query $q$, estimate the number of points within a specified distance threshold of $q$. We develop two estimators, LSH Count and Multi-Probe Count that use locality sensitive hashing to preprocess the data to accurately and efficiently estimate the answers to such questions via importance sampling. A key innovation is the ability to maintain a small number of hash tables via preprocessing data structures and algorithms that sample from multiple buckets in each hash table. We give bounds on the space requirements and sample complexity of our schemes, and demonstrate their effectiveness in experiments on a standard word embedding dataset.
