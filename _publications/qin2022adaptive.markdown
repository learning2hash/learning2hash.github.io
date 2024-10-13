---
layout: publication
title: Adaptive And Dynamic Multi-resolution Hashing For Pairwise Summations
authors: Qin Lianke, Reddy Aravind, Song Zhao, Xu Zhaozhuo, Zhuo Danyang
conference: "Arxiv"
year: 2022
bibkey: qin2022adaptive
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2212.11408"}
tags: ['ARXIV', 'Independent']
---
In this paper, we propose Adam-Hash: an adaptive and dynamic multi-resolution hashing data-structure for fast pairwise summation estimation. Given a data-set \(X \subset \textbackslash\mathbb\{R\}^d\), a binary function \(f:\textbackslash\mathbb\{R\}^d\times \textbackslash\mathbb\{R\}^d\to \textbackslash\mathbb\{R\}\), and a point \(y \in \textbackslash\mathbb\{R\}^d\), the Pairwise Summation Estimate \(\mathrm\{PSE\}\_X(y) := \textbackslash\frac\{1\}\{\|X\|\} \textbackslash\sum\_\{x \in X\} f(x,y)\). For any given data-set \(X\), we need to design a data-structure such that given any query point \(y \in \textbackslash\mathbb\{R\}^d\), the data-structure approximately estimates \(\mathrm\{PSE\}\_X(y)\) in time that is sub-linear in \(\|X\|\). Prior works on this problem have focused exclusively on the case where the data-set is static, and the queries are independent. In this paper, we design a hashing-based PSE data-structure which works for the more practical \textbackslash\textit\{dynamic\} setting in which insertions, deletions, and replacements of points are allowed. Moreover, our proposed Adam-Hash is also robust to adaptive PSE queries, where an adversary can choose query \(q\_j \in \textbackslash\mathbb\{R\}^d\) depending on the output from previous queries \(q\_1, q\_2, \dots, q\_\{j-1\}\).
