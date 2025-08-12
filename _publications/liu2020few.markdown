---
layout: publication
title: Few-shot Open-set Recognition Using Meta-learning
authors: Bo Liu, Hao Kang, Haoxiang Li, Gang Hua, Nuno Vasconcelos
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: liu2020few
citations: 85
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.13713'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Liu et al.
---
The problem of open-set recognition is considered. While previous approaches
only consider this problem in the context of large-scale classifier training,
we seek a unified solution for this and the low-shot classification setting. It
is argued that the classic softmax classifier is a poor solution for open-set
recognition, since it tends to overfit on the training classes. Randomization
is then proposed as a solution to this problem. This suggests the use of
meta-learning techniques, commonly used for few-shot classification, for the
solution of open-set recognition. A new oPen sEt mEta LEaRning (PEELER)
algorithm is then introduced. This combines the random selection of a set of
novel classes per episode, a loss that maximizes the posterior entropy for
examples of those classes, and a new metric learning formulation based on the
Mahalanobis distance. Experimental results show that PEELER achieves state of
the art open set recognition performance for both few-shot and large-scale
recognition. On CIFAR and miniImageNet, it achieves substantial gains in
seen/unseen class detection AUROC for a given seen-class classification
accuracy.