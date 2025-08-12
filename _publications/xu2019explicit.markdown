---
layout: publication
title: Explicit Shape Encoding For Real-time Instance Segmentation
authors: Wenqiang Xu, Haiyang Wang, Fubo Qi, Cewu Lu
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: xu2019explicit
citations: 101
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.04067'}]
tags: ["ICCV"]
short_authors: Xu et al.
---
In this paper, we propose a novel top-down instance segmentation framework
based on explicit shape encoding, named \textbf\{ESE-Seg\}. It largely reduces
the computational consumption of the instance segmentation by explicitly
decoding the multiple object shapes with tensor operations, thus performs the
instance segmentation at almost the same speed as the object detection. ESE-Seg
is based on a novel shape signature Inner-center Radius (IR), Chebyshev
polynomial fitting and the strong modern object detectors. ESE-Seg with YOLOv3
outperforms the Mask R-CNN on Pascal VOC 2012 at mAP\(^r\)@0.5 while 7 times
faster.