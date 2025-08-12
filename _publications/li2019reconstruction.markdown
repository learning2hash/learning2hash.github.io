---
layout: publication
title: Reconstruction Regularized Deep Metric Learning For Multi-label Image Classification
authors: Changsheng Li, Chong Liu, Lixin Duan, Peng Gao, Kai Zheng
conference: IEEE Transactions on Neural Networks and Learning Systems
year: 2019
bibkey: li2019reconstruction
citations: 33
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.13547'}]
tags: ["Distance Metric Learning"]
short_authors: Li et al.
---
In this paper, we present a novel deep metric learning method to tackle the
multi-label image classification problem. In order to better learn the
correlations among images features, as well as labels, we attempt to explore a
latent space, where images and labels are embedded via two unique deep neural
networks, respectively. To capture the relationships between image features and
labels, we aim to learn a *two-way* deep distance metric over the
embedding space from two different views, i.e., the distance between one image
and its labels is not only smaller than those distances between the image and
its labels' nearest neighbors, but also smaller than the distances between the
labels and other images corresponding to the labels' nearest neighbors.
Moreover, a reconstruction module for recovering correct labels is incorporated
into the whole framework as a regularization term, such that the label
embedding space is more representative. Our model can be trained in an
end-to-end manner. Experimental results on publicly available image datasets
corroborate the efficacy of our method compared with the state-of-the-arts.