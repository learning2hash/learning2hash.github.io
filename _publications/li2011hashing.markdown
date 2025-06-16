---
layout: publication
title: Hashing Algorithms For Large-scale Learning
authors: Ping Li, Anshumali Shrivastava, Joshua Moore, Arnd Christian Konig
conference: Arxiv
year: 2011
citations: 113
bibkey: li2011hashing
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1106.0967'}]
tags: [Hashing Methods, Efficient Learning]
---
In this paper, we first demonstrate that b-bit minwise hashing, whose
estimators are positive definite kernels, can be naturally integrated with
learning algorithms such as SVM and logistic regression. We adopt a simple
scheme to transform the nonlinear (resemblance) kernel into linear (inner
product) kernel; and hence large-scale problems can be solved extremely
efficiently. Our method provides a simple effective solution to large-scale
learning in massive and extremely high-dimensional datasets, especially when
data do not fit in memory.
  We then compare b-bit minwise hashing with the Vowpal Wabbit (VW) algorithm
(which is related the Count-Min (CM) sketch). Interestingly, VW has the same
variances as random projections. Our theoretical and empirical comparisons
illustrate that usually \\(b\\)-bit minwise hashing is significantly more accurate
(at the same storage) than VW (and random projections) in binary data.
Furthermore, \\(b\\)-bit minwise hashing can be combined with VW to achieve further
improvements in terms of training speed, especially when \\(b\\) is large.