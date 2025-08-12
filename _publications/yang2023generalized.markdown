---
layout: publication
title: Generalized Category Discovery With Clustering Assignment Consistency
authors: Xiangli Yang, Xinglin Pan, Irwin King, Zenglin Xu
conference: Lecture Notes in Computer Science
year: 2023
bibkey: yang2023generalized
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.19210'}]
tags: []
short_authors: Yang et al.
---
Generalized category discovery (GCD) is a recently proposed open-world task.
Given a set of images consisting of labeled and unlabeled instances, the goal
of GCD is to automatically cluster the unlabeled samples using information
transferred from the labeled dataset. The unlabeled dataset comprises both
known and novel classes. The main challenge is that unlabeled novel class
samples and unlabeled known class samples are mixed together in the unlabeled
dataset. To address the GCD without knowing the class number of unlabeled
dataset, we propose a co-training-based framework that encourages clustering
consistency. Specifically, we first introduce weak and strong augmentation
transformations to generate two sufficiently different views for the same
sample. Then, based on the co-training assumption, we propose a consistency
representation learning strategy, which encourages consistency between
feature-prototype similarity and clustering assignment. Finally, we use the
discriminative embeddings learned from the semi-supervised representation
learning process to construct an original sparse network and use a community
detection method to obtain the clustering results and the number of categories
simultaneously. Extensive experiments show that our method achieves
state-of-the-art performance on three generic benchmarks and three fine-grained
visual recognition datasets. Especially in the ImageNet-100 data set, our
method significantly exceeds the best baseline by 15.5% and 7.0% on the
\texttt\{Novel\} and \texttt\{All\} classes, respectively.