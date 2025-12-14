---
layout: publication
title: On The Estimation Of Image-matching Uncertainty In Visual Place Recognition
authors: Mubariz Zaffar, Liangliang Nan, Julian F. P. Kooij
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: zaffar2024on
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.00546'}]
tags: [Evaluation, CVPR, Image Retrieval]
short_authors: Mubariz Zaffar, Liangliang Nan, Julian F. P. Kooij
---
In Visual Place Recognition (VPR) the pose of a query image is estimated by
comparing the image to a map of reference images with known reference poses. As
is typical for image retrieval problems, a feature extractor maps the query and
reference images to a feature space, where a nearest neighbor search is then
performed. However, till recently little attention has been given to
quantifying the confidence that a retrieved reference image is a correct match.
Highly certain but incorrect retrieval can lead to catastrophic failure of
VPR-based localization pipelines. This work compares for the first time the
main approaches for estimating the image-matching uncertainty, including the
traditional retrieval-based uncertainty estimation, more recent data-driven
aleatoric uncertainty estimation, and the compute-intensive geometric
verification. We further formulate a simple baseline method, ``SUE'', which
unlike the other methods considers the freely-available poses of the reference
images in the map. Our experiments reveal that a simple L2-distance between the
query and reference descriptors is already a better estimate of image-matching
uncertainty than current data-driven approaches. SUE outperforms the other
efficient uncertainty estimation methods, and its uncertainty estimates
complement the computationally expensive geometric verification approach.
Future works for uncertainty estimation in VPR should consider the baselines
discussed in this work.