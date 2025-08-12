---
layout: publication
title: 'Escaping The Curse Of Dimensionality In Similarity Learning: Efficient Frank-wolfe
  Algorithm And Generalization Bounds'
authors: "Kuan Liu, Aur\xE9lien Bellet"
conference: Neurocomputing
year: 2018
bibkey: liu2018escaping
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.07789'}]
tags: ["Distance Metric Learning"]
short_authors: "Kuan Liu, Aur\xE9lien Bellet"
---
Similarity and metric learning provides a principled approach to construct a
task-specific similarity from weakly supervised data. However, these methods
are subject to the curse of dimensionality: as the number of features grows
large, poor generalization is to be expected and training becomes intractable
due to high computational and memory costs. In this paper, we propose a
similarity learning method that can efficiently deal with high-dimensional
sparse data. This is achieved through a parameterization of similarity
functions by convex combinations of sparse rank-one matrices, together with the
use of a greedy approximate Frank-Wolfe algorithm which provides an efficient
way to control the number of active features. We show that the convergence rate
of the algorithm, as well as its time and memory complexity, are independent of
the data dimension. We further provide a theoretical justification of our
modeling choices through an analysis of the generalization error, which depends
logarithmically on the sparsity of the solution rather than on the number of
features. Our experiments on datasets with up to one million features
demonstrate the ability of our approach to generalize well despite the high
dimensionality as well as its superiority compared to several competing
methods.