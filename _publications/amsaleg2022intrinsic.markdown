---
layout: publication
title: 'Intrinsic Dimensionality Estimation Within Tight Localities: A Theoretical
  And Experimental Analysis'
authors: Amsaleg et al.
conference: Proceedings of the 2019 SIAM International Conference on Data Mining
year: 2022
bibkey: amsaleg2022intrinsic
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.14475'}]
tags: [Similarity Search]
---
Accurate estimation of Intrinsic Dimensionality (ID) is of crucial importance
in many data mining and machine learning tasks, including dimensionality
reduction, outlier detection, similarity search and subspace clustering.
However, since their convergence generally requires sample sizes (that is,
neighborhood sizes) on the order of hundreds of points, existing ID estimation
methods may have only limited usefulness for applications in which the data
consists of many natural groups of small size. In this paper, we propose a
local ID estimation strategy stable even for `tight' localities consisting of
as few as 20 sample points. The estimator applies MLE techniques over all
available pairwise distances among the members of the sample, based on a recent
extreme-value-theoretic model of intrinsic dimensionality, the Local Intrinsic
Dimension (LID). Our experimental results show that our proposed estimation
technique can achieve notably smaller variance, while maintaining comparable
levels of bias, at much smaller sample sizes than state-of-the-art estimators.