---
layout: publication
title: 'Cipr: An Efficient Framework With Cross-instance Positive Relations For Generalized
  Category Discovery'
authors: Shaozhe Hao, Kai Han, Kwan-Yee K. Wong
conference: Arxiv
year: 2023
bibkey: hao2023cipr
citations: 2
additional_links: [{name: Code, url: 'https://github.com/haoosz/CiPR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2304.06928'}]
tags: []
short_authors: Shaozhe Hao, Kai Han, Kwan-Yee K. Wong
---
We tackle the issue of generalized category discovery (GCD). GCD considers
the open-world problem of automatically clustering a partially labelled
dataset, in which the unlabelled data may contain instances from both novel
categories and labelled classes. In this paper, we address the GCD problem with
an unknown category number for the unlabelled data. We propose a framework,
named CiPR, to bootstrap the representation by exploiting Cross-instance
Positive Relations in the partially labelled data for contrastive learning,
which have been neglected in existing methods. To obtain reliable
cross-instance relations to facilitate representation learning, we introduce a
semi-supervised hierarchical clustering algorithm, named selective neighbor
clustering (SNC), which can produce a clustering hierarchy directly from the
connected components of a graph constructed from selective neighbors. We
further present a method to estimate the unknown class number using SNC with a
joint reference score that considers clustering indexes of both labelled and
unlabelled data, and extend SNC to allow label assignment for the unlabelled
instances with a given class number. We thoroughly evaluate our framework on
public generic image recognition datasets and challenging fine-grained
datasets, and establish a new state-of-the-art. Code:
https://github.com/haoosz/CiPR