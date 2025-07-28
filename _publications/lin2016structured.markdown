---
layout: publication
title: Structured Learning Of Binary Codes With Column Generation
authors: Guosheng Lin, Fayao Liu, Chunhua Shen, Jianxin Wu, Heng Tao Shen
conference: Arxiv
year: 2016
bibkey: lin2016structured
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.06654'}]
tags: ["Compact Codes", "Distance Metric Learning", "Hashing Methods"]
short_authors: Lin et al.
---
Hashing methods aim to learn a set of hash functions which map the original
features to compact binary codes with similarity preserving in the Hamming
space. Hashing has proven a valuable tool for large-scale information
retrieval. We propose a column generation based binary code learning framework
for data-dependent hash function learning. Given a set of triplets that encode
the pairwise similarity comparison information, our column generation based
method learns hash functions that preserve the relative comparison relations
within the large-margin learning framework. Our method iteratively learns the
best hash functions during the column generation procedure. Existing hashing
methods optimize over simple objectives such as the reconstruction error or
graph Laplacian related loss functions, instead of the performance evaluation
criteria of interest---multivariate performance measures such as the AUC and
NDCG. Our column generation based method can be further generalized from the
triplet loss to a general structured learning based framework that allows one
to directly optimize multivariate performance measures. For optimizing general
ranking measures, the resulting optimization problem can involve exponentially
or infinitely many variables and constraints, which is more challenging than
standard structured output learning. We use a combination of column generation
and cutting-plane techniques to solve the optimization problem. To speed-up the
training we further explore stage-wise training and propose to use a simplified
NDCG loss for efficient inference. We demonstrate the generality of our method
by applying it to ranking prediction and image retrieval, and show that it
outperforms a few state-of-the-art hashing methods.