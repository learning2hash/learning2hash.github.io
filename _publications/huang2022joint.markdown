---
layout: publication
title: A Joint Framework Towards Class-aware And Class-agnostic Alignment For Few-shot
  Segmentation
authors: Kai Huang, Mingfei Cheng, Yang Wang, Bochen Wang, Ye Xi, Feigege Wang, Peng
  Chen
conference: Lecture Notes in Computer Science
year: 2023
bibkey: huang2022joint
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.01310'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Huang et al.
---
Few-shot segmentation (FSS) aims to segment objects of unseen classes given
only a few annotated support images. Most existing methods simply stitch query
features with independent support prototypes and segment the query image by
feeding the mixed features to a decoder. Although significant improvements have
been achieved, existing methods are still face class biases due to class
variants and background confusion. In this paper, we propose a joint framework
that combines more valuable class-aware and class-agnostic alignment guidance
to facilitate the segmentation. Specifically, we design a hybrid alignment
module which establishes multi-scale query-support correspondences to mine the
most relevant class-aware information for each query image from the
corresponding support features. In addition, we explore utilizing base-classes
knowledge to generate class-agnostic prior mask which makes a distinction
between real background and foreground by highlighting all object regions,
especially those of unseen classes. By jointly aggregating class-aware and
class-agnostic alignment guidance, better segmentation performances are
obtained on query images. Extensive experiments on PASCAL-\\(5^i\\) and COCO-\\(20^i\\)
datasets demonstrate that our proposed joint framework performs better,
especially on the 1-shot setting.