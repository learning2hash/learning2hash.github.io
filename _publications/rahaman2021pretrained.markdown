---
layout: publication
title: Pretrained Equivariant Features Improve Unsupervised Landmark Discovery
authors: Rahul Rahaman, Atin Ghosh, Alexandre H. Thiery
conference: 2022 26th International Conference on Pattern Recognition (ICPR)
year: 2022
bibkey: rahaman2021pretrained
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.02925'}]
tags: ["Unsupervised"]
short_authors: Rahul Rahaman, Atin Ghosh, Alexandre H. Thiery
---
Locating semantically meaningful landmark points is a crucial component of a
large number of computer vision pipelines. Because of the small number of
available datasets with ground truth landmark annotations, it is important to
design robust unsupervised and semi-supervised methods for landmark detection.
  Many of the recent unsupervised learning methods rely on the equivariance
properties of landmarks to synthetic image deformations. Our work focuses on
such widely used methods and sheds light on its core problem, its inability to
produce equivariant intermediate convolutional features. This finding leads us
to formulate a two-step unsupervised approach that overcomes this challenge by
first learning powerful pixel-based features and then use the pre-trained
features to learn a landmark detector by the traditional equivariance method.
Our method produces state-of-the-art results in several challenging landmark
detection datasets such as the BBC Pose dataset and the Cat-Head dataset. It
performs comparably on a range of other benchmarks.