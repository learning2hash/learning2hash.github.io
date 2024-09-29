---
layout: publication
title: Training Logistic Regression And SVM On 200GB Data Using B45;bit Minwise Hashing And Comparisons With Vowpal Wabbit (VW)
authors: Li Ping, Shrivastava Anshumali, Konig Christian
conference: "Arxiv"
year: 2011
bibkey: li2011training
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1108.3072"}
tags: ['ARXIV', 'Supervised']
---
We generated a dataset of 200 GB with 10^9 features to test our recent b45;bit minwise hashing algorithms for training very large45;scale logistic regression and SVM. The results confirm our prior work that compared with the VW hashing algorithm (which has the same variance as random projections) b45;bit minwise hashing is substantially more accurate at the same storage. For example with merely 30 hashed values per data point b45;bit minwise hashing can achieve similar accuracies as VW with 2^14 hashed values per data point. We demonstrate that the preprocessing cost of b45;bit minwise hashing is roughly on the same order of magnitude as the data loading time. Furthermore by using a GPU the preprocessing cost can be reduced to a small fraction of the data loading time. Minwise hashing has been widely used in industry at least in the context of search. One reason for its popularity is that one can efficiently simulate permutations by (e.g.) universal hashing. In other words there is no need to store the permutation matrix. In this paper we empirically verify this practice by demonstrating that even using the simplest 245;universal hashing does not degrade the learning performance.
