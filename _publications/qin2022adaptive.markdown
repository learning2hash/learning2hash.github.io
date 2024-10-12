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
In this paper, we propose Adam-Hash: an adaptive and dynamic multi-resolution hashing data-structure for fast pairwise summation estimation. Given a data-set \(X \subset \mathbb\&amp;\#123;R\&amp;\#125;^d\), a binary function $f:\mathbb&amp;\#123;R&amp;\#125;^d\times \mathbb&amp;\#123;R&amp;\#125;^d\to \mathbb&amp;\#123;R&amp;\#125;\(, and a point \)y \in \mathbb&amp;\#123;R&amp;\#125;^d$, the Pairwise Summation Estimate \(\mathrm\&amp;\#123;PSE\&amp;\#125;\_X(y) := \frac\&amp;\#123;1\&amp;\#125;\&amp;\#123;|X|\&amp;\#125; \sum\_\&amp;\#123;x \in X\&amp;\#125; f(x,y)\). For any given data-set \(X\), we need to design a data-structure such that given any query point \(y \in \mathbb\&amp;\#123;R\&amp;\#125;^d\), the data-structure approximately estimates \(\mathrm\&amp;\#123;PSE\&amp;\#125;\_X(y)\) in time that is sub-linear in \(|X|\). Prior works on this problem have focused exclusively on the case where the data-set is static, and the queries are independent. In this paper, we design a hashing-based PSE data-structure which works for the more practical \textit&amp;\#123;dynamic&amp;\#125; setting in which insertions, deletions, and replacements of points are allowed. Moreover, our proposed Adam-Hash is also robust to adaptive PSE queries, where an adversary can choose query \(q\_j \in \mathbb\&amp;\#123;R\&amp;\#125;^d\) depending on the output from previous queries \(q\_1, q\_2, \dots, q\_\&amp;\#123;j-1\&amp;\#125;\).
