---
layout: publication
title: Improving Small Object Proposals For Company Logo Detection
authors: Christian Eggert, Dan Zecha, Stephan Brehm, Rainer Lienhart
conference: Proceedings of the 2017 ACM on International Conference on Multimedia
  Retrieval
year: 2017
bibkey: eggert2017improving
citations: 42
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.08881'}]
tags: ["Datasets", "Evaluation"]
short_authors: Eggert et al.
---
Many modern approaches for object detection are two-staged pipelines. The
first stage identifies regions of interest which are then classified in the
second stage. Faster R-CNN is such an approach for object detection which
combines both stages into a single pipeline. In this paper we apply Faster
R-CNN to the task of company logo detection. Motivated by its weak performance
on small object instances, we examine in detail both the proposal and the
classification stage with respect to a wide range of object sizes. We
investigate the influence of feature map resolution on the performance of those
stages.
  Based on theoretical considerations, we introduce an improved scheme for
generating anchor proposals and propose a modification to Faster R-CNN which
leverages higher-resolution feature maps for small objects. We evaluate our
approach on the FlickrLogos dataset improving the RPN performance from 0.52 to
0.71 (MABO) and the detection performance from 0.52 to 0.67 (mAP).