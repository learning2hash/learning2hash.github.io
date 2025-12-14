---
layout: publication
title: Learning To Guide Local Feature Matches
authors: "Fran\xE7ois Darmon, Mathieu Aubry, Pascal Monasse"
conference: 2020 International Conference on 3D Vision (3DV)
year: 2020
bibkey: darmon2020learning
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.10959'}]
tags: [Evaluation, Datasets]
short_authors: "Fran\xE7ois Darmon, Mathieu Aubry, Pascal Monasse"
---
We tackle the problem of finding accurate and robust keypoint correspondences
between images. We propose a learning-based approach to guide local feature
matches via a learned approximate image matching. Our approach can boost the
results of SIFT to a level similar to state-of-the-art deep descriptors, such
as Superpoint, ContextDesc, or D2-Net and can improve performance for these
descriptors. We introduce and study different levels of supervision to learn
coarse correspondences. In particular, we show that weak supervision from
epipolar geometry leads to performances higher than the stronger but more
biased point level supervision and is a clear improvement over weak image level
supervision. We demonstrate the benefits of our approach in a variety of
conditions by evaluating our guided keypoint correspondences for localization
of internet images on the YFCC100M dataset and indoor images on theSUN3D
dataset, for robust localization on the Aachen day-night benchmark and for 3D
reconstruction in challenging conditions using the LTLL historical image data.