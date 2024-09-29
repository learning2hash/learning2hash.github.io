---
layout: publication
title: Fast K45;nn Search
authors: Hyvönen Ville, Pitkänen Teemu, Tasoulis Sotiris, Jääsaari Elias, Tuomainen Risto, Wang Liang, Corander Jukka, Roos Teemu
conference: "IEEE International Conference on Big Data"
year: 2015
bibkey: hyvönen2015fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1509.06957"}
tags: ['ICML', 'Independent']
---
Efficient index structures for fast approximate nearest neighbor queries are required in many applications such as recommendation systems. In high45;dimensional spaces many conventional methods suffer from excessive usage of memory and slow response times. We propose a method where multiple random projection trees are combined by a novel voting scheme. The key idea is to exploit the redundancy in a large number of candidate sets obtained by independently generated random projections in order to reduce the number of expensive exact distance evaluations. The method is straightforward to implement using sparse projections which leads to a reduced memory footprint and fast index construction. Furthermore it enables grouping of the required computations into big matrix multiplications which leads to additional savings due to cache effects and low45;level parallelization. We demonstrate by extensive experiments on a wide variety of data sets that the method is faster than existing partitioning tree or hashing based approaches making it the fastest available technique on high accuracy levels.
