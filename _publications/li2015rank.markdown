---
layout: publication
title: "Rank Subspace Learning for Compact Hash Codes"
authors: Li Kai, Qi Guojun, Ye Jun, Hua Kien A.
conference: Arxiv
year: 2015
bibkey: li2015rank
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1503.05951"}
tags: ['ARXIV', 'Quantisation', 'Supervised', 'Unsupervised']
---
The era of Big Data has spawned unprecedented interests in developing hashing
algorithms for efficient storage and fast nearest neighbor search. Most existing
work learn hash functions that are numeric quantizations of feature values in
projected feature space. In this work, we propose a novel hash learning
framework that encodes feature's rank orders instead of numeric values in a
number of optimal low-dimensional ranking subspaces. We formulate the ranking
subspace learning problem as the optimization of a piece-wise linear convex-
concave function and present two versions of our algorithm: one with independent
optimization of each hash bit and the other exploiting a sequential learning
framework. Our work is a generalization of the Winner-Take-All (WTA) hash family
and naturally enjoys all the numeric stability benefits of rank correlation
measures while being optimized to achieve high precision at very short code
length. We compare with several state-of-the-art hashing algorithms in both
supervised and unsupervised domain, showing superior performance in a number of
data sets.
