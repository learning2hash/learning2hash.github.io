---
layout: publication
title: Nearest-neighbours Estimators For Conditional Mutual Information
authors: Jake Witter, Conor Houghton
conference: Arxiv
year: 2024
bibkey: witter2024nearest
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.00556'}]
tags: ["Distance Metric Learning"]
short_authors: Jake Witter, Conor Houghton
---
The conditional mutual information quantifies the conditional dependence of
two random variables. It has numerous applications; it forms, for example, part
of the definition of transfer entropy, a common measure of the causal
relationship between time series. It does, however, require a lot of data to
estimate accurately and suffers the curse of dimensionality, limiting its
application in machine learning and data science. However, the
Kozachenko-Leonenko approach can address this problem: it is possible, in this
approach to define a nearest-neighbour estimator which depends only on the
distance between data points and not on the dimension of the data. Furthermore,
the bias can be calculated analytically for this estimator. Here this estimator
is described and is tested on simulated data.