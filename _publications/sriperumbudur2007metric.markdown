---
layout: publication
title: Metric Embedding For Nearest Neighbor Classification
authors: Sriperumbudur Bharath K., Lanckriet Gert R. G.
conference: Proceedings IEEE Conference on Computer Vision and Pattern Recognition.
  CVPR 2000 (Cat. No.PR00662)
year: 2007
bibkey: sriperumbudur2007metric
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/0706.3499'}]
tags: [DATASETS, Distance Metric Learning, CVPR, Alt, Tools & Libraries, Evaluation]
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