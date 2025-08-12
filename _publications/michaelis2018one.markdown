---
layout: publication
title: One-shot Instance Segmentation
authors: Claudio Michaelis, Ivan Ustyuzhaninov, Matthias Bethge, Alexander S. Ecker
conference: Arxiv
year: 2018
bibkey: michaelis2018one
citations: 72
additional_links: [{name: Code, url: 'https://github.com/bethgelab/siamese-mask-rcnn'},
  {name: Paper, url: 'https://arxiv.org/abs/1811.11507'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Michaelis et al.
---
We tackle the problem of one-shot instance segmentation: Given an example
image of a novel, previously unknown object category, find and segment all
objects of this category within a complex scene. To address this challenging
new task, we propose Siamese Mask R-CNN. It extends Mask R-CNN by a Siamese
backbone encoding both reference image and scene, allowing it to target
detection and segmentation towards the reference category. We demonstrate
empirical results on MS Coco highlighting challenges of the one-shot setting:
while transferring knowledge about instance segmentation to novel object
categories works very well, targeting the detection network towards the
reference category appears to be more difficult. Our work provides a first
strong baseline for one-shot instance segmentation and will hopefully inspire
further research into more powerful and flexible scene analysis algorithms.
Code is available at: https://github.com/bethgelab/siamese-mask-rcnn