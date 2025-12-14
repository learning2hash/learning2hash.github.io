---
layout: publication
title: Image Super-resolution Via Feature-augmented Random Forest
authors: Hailiang Li, Kin-Man Lam, Miaohui Wang
conference: Arxiv
year: 2017
bibkey: li2017image
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.05248'}]
tags: [Evaluation, Supervised, Image Retrieval, Neural Hashing, Datasets, Unsupervised,
  Hashing Methods, Locality Sensitive Hashing]
short_authors: Hailiang Li, Kin-Man Lam, Miaohui Wang
---
Recent random-forest (RF)-based image super-resolution approaches inherit
some properties from dictionary-learning-based algorithms, but the
effectiveness of the properties in RF is overlooked in the literature. In this
paper, we present a novel feature-augmented random forest (FARF) for image
super-resolution, where the conventional gradient-based features are augmented
with gradient magnitudes and different feature recipes are formulated on
different stages in an RF. The advantages of our method are that, firstly, the
dictionary-learning-based features are enhanced by adding gradient magnitudes,
based on the observation that the non-linear gradient magnitude are with highly
discriminative property. Secondly, generalized locality-sensitive hashing (LSH)
is used to replace principal component analysis (PCA) for feature
dimensionality reduction and original high-dimensional features are employed,
instead of the compressed ones, for the leaf-nodes' regressors, since
regressors can benefit from higher dimensional features. This
original-compressed coupled feature sets scheme unifies the unsupervised LSH
evaluation on both image super-resolution and content-based image retrieval
(CBIR). Finally, we present a generalized weighted ridge regression (GWRR)
model for the leaf-nodes' regressors. Experiment results on several public
benchmark datasets show that our FARF method can achieve an average gain of
about 0.3 dB, compared to traditional RF-based methods. Furthermore, a
fine-tuned FARF model can compare to or (in many cases) outperform some recent
stateof-the-art deep-learning-based algorithms.