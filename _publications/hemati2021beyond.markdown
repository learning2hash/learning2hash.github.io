---
layout: publication
title: Beyond Neighbourhood-preserving Transformations For Quantization-based Unsupervised
  Hashing
authors: Sobhan Hemati, H. R. Tizhoosh
conference: Pattern Recognition Letters
year: 2021
bibkey: hemati2021beyond
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.00216'}]
tags: [Compact Codes, Evaluation, Supervised, Datasets, Quantization, Unsupervised,
  Hashing Methods]
short_authors: Sobhan Hemati, H. R. Tizhoosh
---
An effective unsupervised hashing algorithm leads to compact binary codes
preserving the neighborhood structure of data as much as possible. One of the
most established schemes for unsupervised hashing is to reduce the
dimensionality of data and then find a rigid (neighbourhood-preserving)
transformation that reduces the quantization error. Although employing rigid
transformations is effective, we may not reduce quantization loss to the
ultimate limits. As well, reducing dimensionality and quantization loss in two
separate steps seems to be sub-optimal. Motivated by these shortcomings, we
propose to employ both rigid and non-rigid transformations to reduce
quantization error and dimensionality simultaneously. We relax the
orthogonality constraint on the projection in a PCA-formulation and regularize
this by a quantization term. We show that both the non-rigid projection matrix
and rotation matrix contribute towards minimizing quantization loss but in
different ways. A scalable nested coordinate descent approach is proposed to
optimize this mixed-integer optimization problem. We evaluate the proposed
method on five public benchmark datasets providing almost half a million
images. Comparative results indicate that the proposed method mostly
outperforms state-of-art linear methods and competes with end-to-end deep
solutions.