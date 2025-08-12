---
layout: publication
title: Multi-class Classification From Noisy-similarity-labeled Data
authors: Songhua Wu, Xiaobo Xia, Tongliang Liu, Bo Han, Mingming Gong, Nannan Wang,
  Haifeng Liu, Gang Niu
conference: Arxiv
year: 2020
bibkey: wu2020multi
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.06508'}]
tags: ["Datasets", "Evaluation"]
short_authors: Wu et al.
---
A similarity label indicates whether two instances belong to the same class
while a class label shows the class of the instance. Without class labels, a
multi-class classifier could be learned from similarity-labeled pairwise data
by meta classification learning. However, since the similarity label is less
informative than the class label, it is more likely to be noisy. Deep neural
networks can easily remember noisy data, leading to overfitting in
classification. In this paper, we propose a method for learning from only
noisy-similarity-labeled data. Specifically, to model the noise, we employ a
noise transition matrix to bridge the class-posterior probability between clean
and noisy data. We further estimate the transition matrix from only noisy data
and build a novel learning system to learn a classifier which can assign
noise-free class labels for instances. Moreover, we theoretically justify how
our proposed method generalizes for learning classifiers. Experimental results
demonstrate the superiority of the proposed method over the state-of-the-art
method on benchmark-simulated and real-world noisy-label datasets.