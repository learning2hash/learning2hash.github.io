---
layout: publication
title: Improved Visual Localization Via Graph Smoothing
authors: Carlos Lassance, Yasir Latif, Ravi Garg, Vincent Gripon, Ian Reid
conference: Arxiv
year: 2019
bibkey: lassance2019improved
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.02961'}]
tags: ["Evaluation", "Graph Based ANN", "Image Retrieval"]
short_authors: Lassance et al.
---
Vision based localization is the problem of inferring the pose of the camera
given a single image. One solution to this problem is to learn a deep neural
network to infer the pose of a query image after learning on a dataset of
images with known poses. Another more commonly used approach rely on image
retrieval where the query image is compared against the database of images and
its pose is inferred with the help of the retrieved images. The latter approach
assumes that images taken from the same places consists of the same landmarks
and, thus would have similar feature representations. These representation can
be learned using full supervision to be robust to different variations in
capture conditions like time of the day and weather. In this work, we introduce
a framework to enhance the performance of these retrieval based localization
methods by taking into account the additional information including GPS
coordinates and temporal neighbourhood of the images provided by the
acquisition process in addition to the descriptor similarity of pairs of images
in the reference or query database which is used traditionally for
localization. Our method constructs a graph based on this additional
information and use it for robust retrieval by smoothing the feature
representation of reference and/or query images. We show that the proposed
method is able to significantly improve the localization accuracy on two large
scale datasets over the baselines.