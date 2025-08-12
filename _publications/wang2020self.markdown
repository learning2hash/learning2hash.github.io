---
layout: publication
title: Self-supervising Action Recognition By Statistical Moment And Subspace Descriptors
authors: Lei Wang, Piotr Koniusz
conference: Proceedings of the 29th ACM International Conference on Multimedia
year: 2021
bibkey: wang2020self
citations: 43
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.04627'}]
tags: []
short_authors: Lei Wang, Piotr Koniusz
---
In this paper, we build on a concept of self-supervision by taking RGB frames
as input to learn to predict both action concepts and auxiliary descriptors
e.g., object descriptors. So-called hallucination streams are trained to
predict auxiliary cues, simultaneously fed into classification layers, and then
hallucinated at the testing stage to aid network. We design and hallucinate two
descriptors, one leveraging four popular object detectors applied to training
videos, and the other leveraging image- and video-level saliency detectors. The
first descriptor encodes the detector- and ImageNet-wise class prediction
scores, confidence scores, and spatial locations of bounding boxes and frame
indexes to capture the spatio-temporal distribution of features per video.
Another descriptor encodes spatio-angular gradient distributions of saliency
maps and intensity patterns. Inspired by the characteristic function of the
probability distribution, we capture four statistical moments on the above
intermediate descriptors. As numbers of coefficients in the mean, covariance,
coskewness and cokurtotsis grow linearly, quadratically, cubically and
quartically w.r.t. the dimension of feature vectors, we describe the covariance
matrix by its leading n' eigenvectors (so-called subspace) and we capture
skewness/kurtosis rather than costly coskewness/cokurtosis. We obtain state of
the art on five popular datasets such as Charades and EPIC-Kitchens.