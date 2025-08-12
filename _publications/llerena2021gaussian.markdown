---
layout: publication
title: Gaussian Bounding Boxes And Probabilistic Intersection-over-union For Object
  Detection
authors: Jeffri M. Llerena, Luis Felipe Zeni, Lucas N. Kristen, Claudio Jung
conference: IEEE Transactions on Image Processing 33 2024 671 - 681
year: 2021
bibkey: llerena2021gaussian
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.06072'}]
tags: []
short_authors: Llerena et al.
---
Most object detection methods use bounding boxes to encode and represent the
object shape and location. In this work, we explore a fuzzy representation of
object regions using Gaussian distributions, which provides an implicit binary
representation as (potentially rotated) ellipses. We also present a similarity
measure for the Gaussian distributions based on the Hellinger Distance, which
can be viewed as a Probabilistic Intersection-over-Union (ProbIoU). Our
experimental results show that the proposed Gaussian representations are closer
to annotated segmentation masks in publicly available datasets, and that loss
functions based on ProbIoU can be successfully used to regress the parameters
of the Gaussian representation. Furthermore, we present a simple mapping scheme
from traditional (or rotated) bounding boxes to Gaussian representations,
allowing the proposed ProbIoU-based losses to be seamlessly integrated into any
object detector.