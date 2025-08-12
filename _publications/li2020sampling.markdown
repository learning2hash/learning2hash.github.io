---
layout: publication
title: On Sampling Top-k Recommendation Evaluation
authors: Dong Li, Ruoming Jin, Jing Gao, Zhi Liu
conference: Proceedings of the 26th ACM SIGKDD International Conference on Knowledge
  Discovery &amp; Data Mining
year: 2020
bibkey: li2020sampling
citations: 33
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.10621'}]
tags: ["Evaluation", "KDD", "Recommender Systems"]
short_authors: Li et al.
---
Recently, Rendle has warned that the use of sampling-based top-\(k\) metrics
might not suffice. This throws a number of recent studies on deep
learning-based recommendation algorithms, and classic non-deep-learning
algorithms using such a metric, into jeopardy. In this work, we thoroughly
investigate the relationship between the sampling and global top-\(K\) Hit-Ratio
(HR, or Recall), originally proposed by Koren[2] and extensively used by
others. By formulating the problem of aligning sampling top-\(k\) (\(SHR@k\)) and
global top-\(K\) (\(HR@K\)) Hit-Ratios through a mapping function \(f\), so that
\(SHR@k\approx HR@f(k)\), we demonstrate both theoretically and experimentally
that the sampling top-\(k\) Hit-Ratio provides an accurate approximation of its
global (exact) counterpart, and can consistently predict the correct winners
(the same as indicate by their corresponding global Hit-Ratios).