---
layout: publication
title: Estimating Mutual Information Via Geodesic \(k\)nn
authors: Alexander Marx, Jonas Fischer
conference: Arxiv
year: 2021
bibkey: marx2021estimating
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.13883'}]
tags: []
short_authors: Alexander Marx, Jonas Fischer
---
Estimating mutual information (MI) between two continuous random variables
\(X\) and \(Y\) allows to capture non-linear dependencies between them,
non-parametrically. As such, MI estimation lies at the core of many data
science applications. Yet, robustly estimating MI for high-dimensional \(X\) and
\(Y\) is still an open research question.
  In this paper, we formulate this problem through the lens of manifold
learning. That is, we leverage the common assumption that the information of
\(X\) and \(Y\) is captured by a low-dimensional manifold embedded in the observed
high-dimensional space and transfer it to MI estimation. As an extension to
state-of-the-art \(k\)NN estimators, we propose to determine the \(k\)-nearest
neighbors via geodesic distances on this manifold rather than from the ambient
space, which allows us to estimate MI even in the high-dimensional setting. An
empirical evaluation of our method, G-KSG, against the state-of-the-art shows
that it yields good estimations of MI in classical benchmark and manifold
tasks, even for high dimensional datasets, which none of the existing methods
can provide.