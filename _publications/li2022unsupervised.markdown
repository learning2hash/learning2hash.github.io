---
layout: publication
title: Unsupervised Long-term Person Re-identification With Clothes Change
authors: Mingkun Li, Shupeng Cheng, Peng Xu, Xiatian Zhu, Chun-Guang Li, Jun Guo
conference: Pattern Recognition
year: 2022
bibkey: li2022unsupervised
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.03087'}]
tags: ["Unsupervised"]
short_authors: Li et al.
---
We investigate unsupervised person re-identification (Re-ID) with clothes
change, a new challenging problem with more practical usability and scalability
to real-world deployment. Most existing re-id methods artificially assume the
clothes of every single person to be stationary across space and time. This
condition is mostly valid for short-term re-id scenarios since an average
person would often change the clothes even within a single day. To alleviate
this assumption, several recent works have introduced the clothes change facet
to re-id, with a focus on supervised learning person identity discriminative
representation with invariance to clothes changes. Taking a step further
towards this long-term re-id direction, we further eliminate the requirement of
person identity labels, as they are significantly more expensive and more
tedious to annotate in comparison to short-term person re-id datasets. Compared
to conventional unsupervised short-term re-id, this new problem is drastically
more challenging as different people may have similar clothes whilst the same
person can wear multiple suites of clothes over different locations and times
with very distinct appearance. To overcome such obstacles, we introduce a novel
Curriculum Person Clustering (CPC) method that can adaptively regulate the
unsupervised clustering criterion according to the clustering confidence.
Experiments on three long-term person re-id datasets show that our CPC
outperforms SOTA unsupervised re-id methods and even closely matches the
supervised re-id models.