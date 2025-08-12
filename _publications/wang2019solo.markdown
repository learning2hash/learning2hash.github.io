---
layout: publication
title: 'SOLO: Segmenting Objects By Locations'
authors: Xinlong Wang, Tao Kong, Chunhua Shen, Yuning Jiang, Lei Li
conference: Lecture Notes in Computer Science
year: 2020
bibkey: wang2019solo
citations: 663
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.04488'}]
tags: []
short_authors: Wang et al.
---
We present a new, embarrassingly simple approach to instance segmentation in
images. Compared to many other dense prediction tasks, e.g., semantic
segmentation, it is the arbitrary number of instances that have made instance
segmentation much more challenging. In order to predict a mask for each
instance, mainstream approaches either follow the 'detect-thensegment' strategy
as used by Mask R-CNN, or predict category masks first then use clustering
techniques to group pixels into individual instances. We view the task of
instance segmentation from a completely new perspective by introducing the
notion of "instance categories", which assigns categories to each pixel within
an instance according to the instance's location and size, thus nicely
converting instance mask segmentation into a classification-solvable problem.
Now instance segmentation is decomposed into two classification tasks. We
demonstrate a much simpler and flexible instance segmentation framework with
strong performance, achieving on par accuracy with Mask R-CNN and outperforming
recent singleshot instance segmenters in accuracy. We hope that this very
simple and strong framework can serve as a baseline for many instance-level
recognition tasks besides instance segmentation.