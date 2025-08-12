---
layout: publication
title: Revisiting Graph Construction For Fast Image Segmentation
authors: Zizhao Zhang, Fuyong Xing, Hanzi Wang, Yan Yan, Ying Huang, Xiaoshuang Shi,
  Lin Yang
conference: Pattern Recognition
year: 2018
bibkey: zhang2017revisiting
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.05650'}]
tags: []
short_authors: Zhang et al.
---
In this paper, we propose a simple but effective method for fast image
segmentation. We re-examine the locality-preserving character of spectral
clustering by constructing a graph over image regions with both global and
local connections. Our novel approach to build graph connections relies on two
key observations: 1) local region pairs that co-occur frequently will have a
high probability to reside on a common object; 2) spatially distant regions in
a common object often exhibit similar visual saliency, which implies their
neighborship in a manifold. We present a novel energy function to efficiently
conduct graph partitioning. Based on multiple high quality partitions, we show
that the generated eigenvector histogram based representation can automatically
drive effective unary potentials for a hierarchical random field model to
produce multi-class segmentation. Sufficient experiments, on the BSDS500
benchmark, large-scale PASCAL VOC and COCO datasets, demonstrate the
competitive segmentation accuracy and significantly improved efficiency of our
proposed method compared with other state of the arts.