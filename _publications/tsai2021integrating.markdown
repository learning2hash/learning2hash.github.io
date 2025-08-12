---
layout: publication
title: Integrating Auxiliary Information In Self-supervised Learning
authors: Yao-Hung Hubert Tsai, Tianqin Li, Weixin Liu, Peiyuan Liao, Ruslan Salakhutdinov,
  Louis-Philippe Morency
conference: Arxiv
year: 2021
bibkey: tsai2021integrating
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.02869'}]
tags: ["Self-Supervised"]
short_authors: Tsai et al.
---
This paper presents to integrate the auxiliary information (e.g., additional
attributes for data such as the hashtags for Instagram images) in the
self-supervised learning process. We first observe that the auxiliary
information may bring us useful information about data structures: for
instance, the Instagram images with the same hashtags can be semantically
similar. Hence, to leverage the structural information from the auxiliary
information, we present to construct data clusters according to the auxiliary
information. Then, we introduce the Clustering InfoNCE (Cl-InfoNCE) objective
that learns similar representations for augmented variants of data from the
same cluster and dissimilar representations for data from different clusters.
Our approach contributes as follows: 1) Comparing to conventional
self-supervised representations, the auxiliary-information-infused
self-supervised representations bring the performance closer to the supervised
representations; 2) The presented Cl-InfoNCE can also work with unsupervised
constructed clusters (e.g., k-means clusters) and outperform strong
clustering-based self-supervised learning approaches, such as the Prototypical
Contrastive Learning (PCL) method; 3) We show that Cl-InfoNCE may be a better
approach to leverage the data clustering information, by comparing it to the
baseline approach - learning to predict the clustering assignments with
cross-entropy loss. For analysis, we connect the goodness of the learned
representations with the statistical relationships: i) the mutual information
between the labels and the clusters and ii) the conditional entropy of the
clusters given the labels.