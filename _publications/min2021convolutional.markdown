---
layout: publication
title: Convolutional Hough Matching Networks
authors: Juhong Min, Minsu Cho
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: min2021convolutional
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.16831'}]
tags: ["CVPR"]
short_authors: Juhong Min, Minsu Cho
---
Despite advances in feature representation, leveraging geometric relations is
crucial for establishing reliable visual correspondences under large variations
of images. In this work we introduce a Hough transform perspective on
convolutional matching and propose an effective geometric matching algorithm,
dubbed Convolutional Hough Matching (CHM). The method distributes similarities
of candidate matches over a geometric transformation space and evaluate them in
a convolutional manner. We cast it into a trainable neural layer with a
semi-isotropic high-dimensional kernel, which learns non-rigid matching with a
small number of interpretable parameters. To validate the effect, we develop
the neural network with CHM layers that perform convolutional matching in the
space of translation and scaling. Our method sets a new state of the art on
standard benchmarks for semantic visual correspondence, proving its strong
robustness to challenging intra-class variations.