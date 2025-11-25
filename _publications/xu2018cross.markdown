---
layout: publication
title: Cross-paced Representation Learning With Partial Curricula For Sketch-based
  Image Retrieval
authors: Dan Xu, Xavier Alameda-Pineda, Jingkuan Song, Elisa Ricci, Nicu Sebe
conference: IEEE Transactions on Image Processing
year: 2018
bibkey: xu2018cross
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.01504'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Xu et al.
---
In this paper we address the problem of learning robust cross-domain
representations for sketch-based image retrieval (SBIR). While most SBIR
approaches focus on extracting low- and mid-level descriptors for direct
feature matching, recent works have shown the benefit of learning coupled
feature representations to describe data from two related sources. However,
cross-domain representation learning methods are typically cast into non-convex
minimization problems that are difficult to optimize, leading to unsatisfactory
performance. Inspired by self-paced learning, a learning methodology designed
to overcome convergence issues related to local optima by exploiting the
samples in a meaningful order (i.e. easy to hard), we introduce the cross-paced
partial curriculum learning (CPPCL) framework. Compared with existing
self-paced learning methods which only consider a single modality and cannot
deal with prior knowledge, CPPCL is specifically designed to assess the
learning pace by jointly handling data from dual sources and modality-specific
prior information provided in the form of partial curricula. Additionally,
thanks to the learned dictionaries, we demonstrate that the proposed CPPCL
embeds robust coupled representations for SBIR. Our approach is extensively
evaluated on four publicly available datasets (i.e. CUFS, Flickr15K, QueenMary
SBIR and TU-Berlin Extension datasets), showing superior performance over
competing SBIR methods.