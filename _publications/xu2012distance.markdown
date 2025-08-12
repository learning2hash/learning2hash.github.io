---
layout: publication
title: Distance Metric Learning For Kernel Machines
authors: Zhixiang Xu, Kilian Q. Weinberger, Olivier Chapelle
conference: Arxiv
year: 2012
bibkey: xu2012distance
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1208.3422'}]
tags: ["Distance Metric Learning"]
short_authors: Zhixiang Xu, Kilian Q. Weinberger, Olivier Chapelle
---
Recent work in metric learning has significantly improved the
state-of-the-art in k-nearest neighbor classification. Support vector machines
(SVM), particularly with RBF kernels, are amongst the most popular
classification algorithms that uses distance metrics to compare examples. This
paper provides an empirical analysis of the efficacy of three of the most
popular Mahalanobis metric learning algorithms as pre-processing for SVM
training. We show that none of these algorithms generate metrics that lead to
particularly satisfying improvements for SVM-RBF classification. As a remedy we
introduce support vector metric learning (SVML), a novel algorithm that
seamlessly combines the learning of a Mahalanobis metric with the training of
the RBF-SVM parameters. We demonstrate the capabilities of SVML on nine
benchmark data sets of varying sizes and difficulties. In our study, SVML
outperforms all alternative state-of-the-art metric learning algorithms in
terms of accuracy and establishes itself as a serious alternative to the
standard Euclidean metric with model selection by cross validation.