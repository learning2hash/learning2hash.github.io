---
layout: publication
title: Multiple Riemannian Manifold-valued Descriptors Based Image Set Classification
  With Multi-kernel Metric Learning
authors: Rui Wang, Xiaojun Wu, Josef Kittler
conference: IEEE Transactions on Big Data
year: 2020
bibkey: wang2019multiple
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.01950'}]
tags: ["Distance Metric Learning"]
short_authors: Rui Wang, Xiaojun Wu, Josef Kittler
---
The importance of wild video based image set recognition is becoming
monotonically increasing. However, the contents of these collected videos are
often complicated, and how to efficiently perform set modeling and feature
extraction is a big challenge for set-based classification algorithms. In
recent years, some proposed image set classification methods have made a
considerable advance by modeling the original image set with covariance matrix,
linear subspace, or Gaussian distribution. As a matter of fact, most of them
just adopt a single geometric model to describe each given image set, which may
lose some other useful information for classification. To tackle this problem,
we propose a novel algorithm to model each image set from a multi-geometric
perspective. Specifically, the covariance matrix, linear subspace, and Gaussian
distribution are applied for set representation simultaneously. In order to
fuse these multiple heterogeneous Riemannian manifoldvalued features, the
well-equipped Riemannian kernel functions are first utilized to map them into
high dimensional Hilbert spaces. Then, a multi-kernel metric learning framework
is devised to embed the learned hybrid kernels into a lower dimensional common
subspace for classification. We conduct experiments on four widely used
datasets corresponding to four different classification tasks: video-based face
recognition, set-based object categorization, video-based emotion recognition,
and dynamic scene classification, to evaluate the classification performance of
the proposed algorithm. Extensive experimental results justify its superiority
over the state-of-the-art.