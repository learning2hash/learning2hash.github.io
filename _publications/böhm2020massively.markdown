---
layout: publication
title: Massively Parallel Graph Drawing And Representation Learning
authors: Böhm Christian, Plant Claudia
conference: "IEEE BigData"
year: 2020
bibkey: böhm2020massively
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2011.03479"}
tags: ['Graph', 'Independent']
---
To fully exploit the performance potential of modern multi-core processors, machine learning and data mining algorithms for big data must be parallelized in multiple ways. Today's CPUs consist of multiple cores, each following an independent thread of control, and each equipped with multiple arithmetic units which can perform the same operation on a vector of multiple data objects. Graph embedding, i.e. converting the vertices of a graph into numerical vectors is a data mining task of high importance and is useful for graph drawing (low-dimensional vectors) and graph representation learning (high-dimensional vectors). In this paper, we propose MulticoreGEMPE (Graph Embedding by Minimizing the Predictive Entropy), an information-theoretic method which can generate low and high-dimensional vectors. MulticoreGEMPE applies MIMD (Multiple Instructions Multiple Data, using OpenMP) and SIMD (Single Instructions Multiple Data, using AVX-512) parallelism. We propose general ideas applicable in other graph-based algorithms like \emph&amp;\#123;vectorized hashing&amp;\#125; and \emph&amp;\#123;vectorized reduction&amp;\#125;. Our experimental evaluation demonstrates the superiority of our approach.
