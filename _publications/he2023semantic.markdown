---
layout: publication
title: Semantic-promoted Debiasing And Background Disambiguation For Zero-shot Instance
  Segmentation
authors: Shuting He, Henghui Ding, Wei Jiang
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: he2023semantic
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.13173'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Shuting He, Henghui Ding, Wei Jiang
---
Zero-shot instance segmentation aims to detect and precisely segment objects
of unseen categories without any training samples. Since the model is trained
on seen categories, there is a strong bias that the model tends to classify all
the objects into seen categories. Besides, there is a natural confusion between
background and novel objects that have never shown up in training. These two
challenges make novel objects hard to be raised in the final instance
segmentation results. It is desired to rescue novel objects from background and
dominated seen categories. To this end, we propose D\(^2\)Zero with
Semantic-Promoted Debiasing and Background Disambiguation to enhance the
performance of Zero-shot instance segmentation. Semantic-promoted debiasing
utilizes inter-class semantic relationships to involve unseen categories in
visual feature training and learns an input-conditional classifier to conduct
dynamical classification based on the input image. Background disambiguation
produces image-adaptive background representation to avoid mistaking novel
objects for background. Extensive experiments show that we significantly
outperform previous state-of-the-art methods by a large margin, e.g., 16.86%
improvement on COCO. Project page: https://henghuiding.github.io/D2Zero/