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
In this paper, we propose Adam-Hash: an adaptive and dynamic multi-resolution hashing data-structure for fast pairwise summation estimation. Given a data-set \\(X \subset \mathbb&#123;R&#125;^d\\), a binary function $f:\mathbb{R}^d\times \mathbb{R}^d\to \mathbb{R}\\(, and a point \\)y \in \mathbb{R}^d$, the Pairwise Summation Estimate \\(\mathrm&#123;PSE&#125;_X(y) := \frac&#123;1&#125;&#123;|X|&#125; \sum_&#123;x \in X&#125; f(x,y)\\). For any given data-set \\(X\\), we need to design a data-structure such that given any query point \\(y \in \mathbb&#123;R&#125;^d\\), the data-structure approximately estimates \\(\mathrm&#123;PSE&#125;_X(y)\\) in time that is sub-linear in \\(|X|\\). Prior works on this problem have focused exclusively on the case where the data-set is static, and the queries are independent. In this paper, we design a hashing-based PSE data-structure which works for the more practical \textit{dynamic} setting in which insertions, deletions, and replacements of points are allowed. Moreover, our proposed Adam-Hash is also robust to adaptive PSE queries, where an adversary can choose query \\(q_j \in \mathbb&#123;R&#125;^d\\) depending on the output from previous queries \\(q_1, q_2, \dots, q_&#123;j-1&#125;\\).
