---
layout: publication
title: Metric Embedding For Nearest Neighbor Classification
authors: Bharath K. Sriperumbudur, Gert R. G. Lanckriet
conference: Arxiv
year: 2007
bibkey: sriperumbudur2007metric
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0706.3499'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation", "Tools & Libraries"]
short_authors: Bharath K. Sriperumbudur, Gert R. G. Lanckriet
---
The distance metric plays an important role in nearest neighbor (NN)
classification. Usually the Euclidean distance metric is assumed or a
Mahalanobis distance metric is optimized to improve the NN performance. In this
paper, we study the problem of embedding arbitrary metric spaces into a
Euclidean space with the goal to improve the accuracy of the NN classifier. We
propose a solution by appealing to the framework of regularization in a
reproducing kernel Hilbert space and prove a representer-like theorem for NN
classification. The embedding function is then determined by solving a
semidefinite program which has an interesting connection to the soft-margin
linear binary support vector machine classifier. Although the main focus of
this paper is to present a general, theoretical framework for metric embedding
in a NN setting, we demonstrate the performance of the proposed method on some
benchmark datasets and show that it performs better than the Mahalanobis metric
learning algorithm in terms of leave-one-out and generalization errors.