---
layout: publication
title: 'Hsolo: Homography From A Single Affine Aware Correspondence'
authors: Antonio Gonzales, Cara Monical, Tony Perkins
conference: Arxiv
year: 2020
bibkey: gonzales2020hsolo
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.05004'}]
tags: ["Evaluation"]
short_authors: Antonio Gonzales, Cara Monical, Tony Perkins
---
The performance of existing robust homography estimation algorithms is highly
dependent on the inlier rate of feature point correspondences. In this paper,
we present a novel procedure for homography estimation that is particularly
well suited for inlier-poor domains. By utilizing the scale and rotation
byproducts created by affine aware feature detectors such as SIFT and SURF, we
obtain an initial homography estimate from a single correspondence pair. This
estimate allows us to filter the correspondences to an inlier-rich subset for
use with a robust estimator. Especially at low inlier rates, our novel
algorithm provides dramatic performance improvements.