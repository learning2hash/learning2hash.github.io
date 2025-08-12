---
layout: publication
title: 'IMP: Instance Mask Projection For High Accuracy Semantic Segmentation Of Things'
authors: Cheng-Yang Fu, Tamara L. Berg, Alexander C. Berg
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: fu2019imp
citations: 21
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.06597'}]
tags: ["ICCV"]
short_authors: Cheng-Yang Fu, Tamara L. Berg, Alexander C. Berg
---
In this work, we present a new operator, called Instance Mask Projection
(IMP), which projects a predicted Instance Segmentation as a new feature for
semantic segmentation. It also supports back propagation so is trainable
end-to-end. Our experiments show the effectiveness of IMP on both Clothing
Parsing (with complex layering, large deformations, and non-convex objects),
and on Street Scene Segmentation (with many overlapping instances and small
objects). On the Varied Clothing Parsing dataset (VCP), we show instance mask
projection can improve 3 points on mIOU from a state-of-the-art Panoptic FPN
segmentation approach. On the ModaNet clothing parsing dataset, we show a
dramatic improvement of 20.4% absolutely compared to existing baseline semantic
segmentation results. In addition, the instance mask projection operator works
well on other (non-clothing) datasets, providing an improvement of 3 points in
mIOU on Thing classes of Cityscapes, a self-driving dataset, on top of a
state-of-the-art approach.