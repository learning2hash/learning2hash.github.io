---
layout: publication
title: Improved Few-shot Visual Classification
authors: Peyman Bateni, Raghav Goyal, Vaden Masrani, Frank Wood, Leonid Sigal
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: bateni2019improved
citations: 185
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.03432'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Bateni et al.
---
Few-shot learning is a fundamental task in computer vision that carries the
promise of alleviating the need for exhaustively labeled data. Most few-shot
learning approaches to date have focused on progressively more complex neural
feature extractors and classifier adaptation strategies, as well as the
refinement of the task definition itself. In this paper, we explore the
hypothesis that a simple class-covariance-based distance metric, namely the
Mahalanobis distance, adopted into a state of the art few-shot learning
approach (CNAPS) can, in and of itself, lead to a significant performance
improvement. We also discover that it is possible to learn adaptive feature
extractors that allow useful estimation of the high dimensional feature
covariances required by this metric from surprisingly few samples. The result
of our work is a new "Simple CNAPS" architecture which has up to 9.2% fewer
trainable parameters than CNAPS and performs up to 6.1% better than state of
the art on the standard few-shot image classification benchmark dataset.