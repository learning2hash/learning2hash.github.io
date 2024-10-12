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
In this paper, we propose Adam-Hash: an adaptive and dynamic multi-resolution hashing data-structure for fast pairwise summation estimation. Given a data-set \{&#37; raw &#37;\}\\(X \subset \mathbb\{R\}^d\\)\{&#37; endraw &#37;\}, a binary function $f:\mathbb\{R\}^d\times \mathbb\{R\}^d\to \mathbb\{R\}\{&#37; raw &#37;\}\\(, and a point \\)\{&#37; endraw &#37;\}y \in \mathbb\{R\}^d$, the Pairwise Summation Estimate \{&#37; raw &#37;\}\\(\mathrm\{PSE\}\_X(y) := \frac\{1\}\{|X|\} \sum\_\{x \in X\} f(x,y)\\)\{&#37; endraw &#37;\}. For any given data-set \{&#37; raw &#37;\}\\(X\\)\{&#37; endraw &#37;\}, we need to design a data-structure such that given any query point \{&#37; raw &#37;\}\\(y \in \mathbb\{R\}^d\\)\{&#37; endraw &#37;\}, the data-structure approximately estimates \{&#37; raw &#37;\}\\(\mathrm\{PSE\}\_X(y)\\)\{&#37; endraw &#37;\} in time that is sub-linear in \{&#37; raw &#37;\}\\(|X|\\)\{&#37; endraw &#37;\}. Prior works on this problem have focused exclusively on the case where the data-set is static, and the queries are independent. In this paper, we design a hashing-based PSE data-structure which works for the more practical \textit\{dynamic\} setting in which insertions, deletions, and replacements of points are allowed. Moreover, our proposed Adam-Hash is also robust to adaptive PSE queries, where an adversary can choose query \{&#37; raw &#37;\}\\(q\_j \in \mathbb\{R\}^d\\)\{&#37; endraw &#37;\} depending on the output from previous queries \{&#37; raw &#37;\}\\(q\_1, q\_2, \dots, q\_\{j-1\}\\)\{&#37; endraw &#37;\}.
