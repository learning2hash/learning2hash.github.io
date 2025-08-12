---
layout: publication
title: Reconciliation Of Statistical And Spatial Sparsity For Robust Image And Image-set
  Classification
authors: Hao Cheng, Kim-Hui Yap, Bihan Wen
conference: Arxiv
year: 2021
bibkey: cheng2021reconciliation
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.00256'}]
tags: []
short_authors: Hao Cheng, Kim-Hui Yap, Bihan Wen
---
Recent image classification algorithms, by learning deep features from
large-scale datasets, have achieved significantly better results comparing to
the classic feature-based approaches. However, there are still various
challenges of image classifications in practice, such as classifying noisy
image or image-set queries and training deep image classification models over
the limited-scale dataset. Instead of applying generic deep features, the
model-based approaches can be more effective and data-efficient for robust
image and image-set classification tasks, as various image priors are exploited
for modeling the inter- and intra-set data variations while preventing
over-fitting. In this work, we propose a novel Joint Statistical and Spatial
Sparse representation, dubbed \textit\{J3S\}, to model the image or image-set
data for classification, by reconciling both their local patch structures and
global Gaussian distribution mapped into Riemannian manifold. To the best of
our knowledge, no work to date utilized both global statistics and local patch
structures jointly via joint sparse representation. We propose to solve the
joint sparse coding problem based on the J3S model, by coupling the local and
global image representations using joint sparsity. The learned J3S models are
used for robust image and image-set classification. Experiments show that the
proposed J3S-based image classification scheme outperforms the popular or
state-of-the-art competing methods over FMD, UIUC, ETH-80 and YTC databases.