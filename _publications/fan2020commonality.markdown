---
layout: publication
title: Commonality-parsing Network Across Shape And Appearance For Partially Supervised
  Instance Segmentation
authors: Qi Fan, Lei Ke, Wenjie Pei, Chi-Keung Tang, Yu-Wing Tai
conference: Lecture Notes in Computer Science
year: 2020
bibkey: fan2020commonality
citations: 25
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.12387'}]
tags: ["Supervised"]
short_authors: Fan et al.
---
Partially supervised instance segmentation aims to perform learning on
limited mask-annotated categories of data thus eliminating expensive and
exhaustive mask annotation. The learned models are expected to be generalizable
to novel categories. Existing methods either learn a transfer function from
detection to segmentation, or cluster shape priors for segmenting novel
categories. We propose to learn the underlying class-agnostic commonalities
that can be generalized from mask-annotated categories to novel categories.
Specifically, we parse two types of commonalities: 1) shape commonalities which
are learned by performing supervised learning on instance boundary prediction;
and 2) appearance commonalities which are captured by modeling pairwise
affinities among pixels of feature maps to optimize the separability between
instance and the background. Incorporating both the shape and appearance
commonalities, our model significantly outperforms the state-of-the-art methods
on both partially supervised setting and few-shot setting for instance
segmentation on COCO dataset.