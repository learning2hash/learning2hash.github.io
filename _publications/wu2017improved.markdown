---
layout: publication
title: Improved Consistent Weighted Sampling Revisited
authors: Wu et al.
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2017
bibkey: wu2017improved
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.01172'}]
tags: []
---
Min-Hash is a popular technique for efficiently estimating the Jaccard
similarity of binary sets. Consistent Weighted Sampling (CWS) generalizes the
Min-Hash scheme to sketch weighted sets and has drawn increasing interest from
the community. Due to its constant-time complexity independent of the values of
the weights, Improved CWS (ICWS) is considered as the state-of-the-art CWS
algorithm. In this paper, we revisit ICWS and analyze its underlying mechanism
to show that there actually exists dependence between the two components of the
hash-code produced by ICWS, which violates the condition of independence. To
remedy the problem, we propose an Improved ICWS (I\\(^2\\)CWS) algorithm which not
only shares the same theoretical computational complexity as ICWS but also
abides by the required conditions of the CWS scheme. The experimental results
on a number of synthetic data sets and real-world text data sets demonstrate
that our I\\(^2\\)CWS algorithm can estimate the Jaccard similarity more
accurately, and also compete with or outperform the compared methods, including
ICWS, in classification and top-\\(K\\) retrieval, after relieving the underlying
dependence.