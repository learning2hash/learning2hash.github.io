---
layout: publication
title: 'Cross-modal Similarity Learning : A Low Rank Bilinear Formulation'
authors: Cuicui Kang, Shengcai Liao, Yonghao He, Jian Wang, Wenjia Niu, Shiming Xiang,
  Chunhong Pan
conference: Arxiv
year: 2014
bibkey: kang2014cross
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1411.4738'}]
tags: ["Distance Metric Learning", "Evaluation"]
short_authors: Kang et al.
---
The cross-media retrieval problem has received much attention in recent years
due to the rapid increasing of multimedia data on the Internet. A new approach
to the problem has been raised which intends to match features of different
modalities directly. In this research, there are two critical issues: how to
get rid of the heterogeneity between different modalities and how to match the
cross-modal features of different dimensions. Recently metric learning methods
show a good capability in learning a distance metric to explore the
relationship between data points. However, the traditional metric learning
algorithms only focus on single-modal features, which suffer difficulties in
addressing the cross-modal features of different dimensions. In this paper, we
propose a cross-modal similarity learning algorithm for the cross-modal feature
matching. The proposed method takes a bilinear formulation, and with the
nuclear-norm penalization, it achieves low-rank representation. Accordingly,
the accelerated proximal gradient algorithm is successfully imported to find
the optimal solution with a fast convergence rate O(1/t^2). Experiments on
three well known image-text cross-media retrieval databases show that the
proposed method achieves the best performance compared to the state-of-the-art
algorithms.