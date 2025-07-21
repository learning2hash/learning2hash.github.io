---
layout: publication
title: Geometric Image Correspondence Verification by Dense Pixel Matching
authors: Laskar et al.
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: laskar2020geometric
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.06882'}]
tags: []
---
This paper addresses the problem of determining dense pixel correspondences
between two images and its application to geometric correspondence verification
in image retrieval. The main contribution is a geometric correspondence
verification approach for re-ranking a shortlist of retrieved database images
based on their dense pair-wise matching with the query image at a pixel level.
We determine a set of cyclically consistent dense pixel matches between the
pair of images and evaluate local similarity of matched pixels using neural
network based image descriptors. Final re-ranking is based on a novel
similarity function, which fuses the local similarity metric with a global
similarity metric and a geometric consistency measure computed for the matched
pixels. For dense matching our approach utilizes a modified version of a
recently proposed dense geometric correspondence network (DGC-Net), which we
also improve by optimizing the architecture. The proposed model and similarity
metric compare favourably to the state-of-the-art image retrieval methods. In
addition, we apply our method to the problem of long-term visual localization
demonstrating promising results and generalization across datasets.