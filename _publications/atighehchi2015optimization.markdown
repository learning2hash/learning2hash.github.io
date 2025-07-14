---
layout: publication
title: 'Optimization Of Tree Modes For Parallel Hash Functions: A Case Study'
authors: Kevin Atighehchi, Robert Rolland
conference: Arxiv
year: 2015
citations: 14
bibkey: atighehchi2015optimization
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1512.05864'}]
tags: [Hashing Methods]
---
This paper focuses on parallel hash functions based on tree modes of
operation for an inner Variable-Input-Length function. This inner function can
be either a single-block-length (SBL) and prefix-free MD hash function, or a
sponge-based hash function. We discuss the various forms of optimality that can
be obtained when designing parallel hash functions based on trees where all
leaves have the same depth. The first result is a scheme which optimizes the
tree topology in order to decrease the running time. Then, without affecting
the optimal running time we show that we can slightly change the corresponding
tree topology so as to minimize the number of required processors as well.
Consequently, the resulting scheme decreases in the first place the running
time and in the second place the number of required processors.