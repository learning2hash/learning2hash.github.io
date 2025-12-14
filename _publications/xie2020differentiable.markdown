---
layout: publication
title: Differentiable Top-k Operator With Optimal Transport
authors: Yujia Xie, Hanjun Dai, Minshuo Chen, Bo Dai, Tuo Zhao, Hongyuan Zha, Wei
  Wei, Tomas Pfister
conference: Arxiv
year: 2020
bibkey: xie2020differentiable
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.06504'}]
tags: [Evaluation]
short_authors: Xie et al.
---
The top-k operation, i.e., finding the k largest or smallest elements from a
collection of scores, is an important model component, which is widely used in
information retrieval, machine learning, and data mining. However, if the top-k
operation is implemented in an algorithmic way, e.g., using bubble algorithm,
the resulting model cannot be trained in an end-to-end way using prevalent
gradient descent algorithms. This is because these implementations typically
involve swapping indices, whose gradient cannot be computed. Moreover, the
corresponding mapping from the input scores to the indicator vector of whether
this element belongs to the top-k set is essentially discontinuous. To address
the issue, we propose a smoothed approximation, namely the SOFT (Scalable
Optimal transport-based diFferenTiable) top-k operator. Specifically, our SOFT
top-k operator approximates the output of the top-k operation as the solution
of an Entropic Optimal Transport (EOT) problem. The gradient of the SOFT
operator can then be efficiently approximated based on the optimality
conditions of EOT problem. We apply the proposed operator to the k-nearest
neighbors and beam search algorithms, and demonstrate improved performance.