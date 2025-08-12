---
layout: publication
title: Hierarchical Gaussian Descriptors With Application To Person Re-identification
authors: Tetsu Matsukawa, Takahiro Okabe, Einoshin Suzuki, Yoichi Sato
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2019
bibkey: matsukawa2017hierarchical
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1706.04318'}]
tags: []
short_authors: Matsukawa et al.
---
Describing the color and textural information of a person image is one of the
most crucial aspects of person re-identification (re-id). In this paper, we
present novel meta-descriptors based on a hierarchical distribution of pixel
features. Although hierarchical covariance descriptors have been successfully
applied to image classification, the mean information of pixel features, which
is absent from the covariance, tends to be the major discriminative information
for person re-id. To solve this problem, we describe a local region in an image
via hierarchical Gaussian distribution in which both means and covariances are
included in their parameters. More specifically, the region is modeled as a set
of multiple Gaussian distributions in which each Gaussian represents the
appearance of a local patch. The characteristics of the set of Gaussians are
again described by another Gaussian distribution. In both steps, we embed the
parameters of the Gaussian into a point of Symmetric Positive Definite (SPD)
matrix manifold. By changing the way to handle mean information in this
embedding, we develop two hierarchical Gaussian descriptors. Additionally, we
develop feature norm normalization methods with the ability to alleviate the
biased trends that exist on the descriptors. The experimental results conducted
on five public datasets indicate that the proposed descriptors achieve
remarkably high performance on person re-id.