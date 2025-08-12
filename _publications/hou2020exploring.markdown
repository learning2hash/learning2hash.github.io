---
layout: publication
title: Exploring Data-efficient 3D Scene Understanding With Contrastive Scene Contexts
authors: "Ji Hou, Benjamin Graham, Matthias Nie\xDFner, Saining Xie"
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: hou2020exploring
citations: 202
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.09165'}]
tags: ["CVPR"]
short_authors: Hou et al.
---
The rapid progress in 3D scene understanding has come with growing demand for
data; however, collecting and annotating 3D scenes (e.g. point clouds) are
notoriously hard. For example, the number of scenes (e.g. indoor rooms) that
can be accessed and scanned might be limited; even given sufficient data,
acquiring 3D labels (e.g. instance masks) requires intensive human labor. In
this paper, we explore data-efficient learning for 3D point cloud. As a first
step towards this direction, we propose Contrastive Scene Contexts, a 3D
pre-training method that makes use of both point-level correspondences and
spatial contexts in a scene. Our method achieves state-of-the-art results on a
suite of benchmarks where training data or labels are scarce. Our study reveals
that exhaustive labelling of 3D point clouds might be unnecessary; and
remarkably, on ScanNet, even using 0.1% of point labels, we still achieve 89%
(instance segmentation) and 96% (semantic segmentation) of the baseline
performance that uses full annotations.