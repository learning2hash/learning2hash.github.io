---
layout: publication
title: 'Deep Metric Learning Meets Deep Clustering: An Novel Unsupervised Approach
  For Feature Embedding'
authors: Binh X. Nguyen, Binh D. Nguyen, Gustavo Carneiro, Erman Tjiputra, Quang D.
  Tran, Thanh-Toan Do
conference: Arxiv
year: 2020
bibkey: nguyen2020deep
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.04091'}]
tags: ["Distance Metric Learning", "Unsupervised"]
short_authors: Nguyen et al.
---
Unsupervised Deep Distance Metric Learning (UDML) aims to learn sample
similarities in the embedding space from an unlabeled dataset. Traditional UDML
methods usually use the triplet loss or pairwise loss which requires the mining
of positive and negative samples w.r.t. anchor data points. This is, however,
challenging in an unsupervised setting as the label information is not
available. In this paper, we propose a new UDML method that overcomes that
challenge. In particular, we propose to use a deep clustering loss to learn
centroids, i.e., pseudo labels, that represent semantic classes. During
learning, these centroids are also used to reconstruct the input samples. It
hence ensures the representativeness of centroids - each centroid represents
visually similar samples. Therefore, the centroids give information about
positive (visually similar) and negative (visually dissimilar) samples. Based
on pseudo labels, we propose a novel unsupervised metric loss which enforces
the positive concentration and negative separation of samples in the embedding
space. Experimental results on benchmarking datasets show that the proposed
approach outperforms other UDML methods.