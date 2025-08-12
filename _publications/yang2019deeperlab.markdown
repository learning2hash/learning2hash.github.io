---
layout: publication
title: 'Deeperlab: Single-shot Image Parser'
authors: Tien-Ju Yang, Maxwell D. Collins, Yukun Zhu, Jyh-Jing Hwang, Ting Liu, Xiao
  Zhang, Vivienne Sze, George Papandreou, Liang-Chieh Chen
conference: Arxiv
year: 2019
bibkey: yang2019deeperlab
citations: 178
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.05093'}]
tags: []
short_authors: Yang et al.
---
We present a single-shot, bottom-up approach for whole image parsing. Whole
image parsing, also known as Panoptic Segmentation, generalizes the tasks of
semantic segmentation for 'stuff' classes and instance segmentation for 'thing'
classes, assigning both semantic and instance labels to every pixel in an
image. Recent approaches to whole image parsing typically employ separate
standalone modules for the constituent semantic and instance segmentation tasks
and require multiple passes of inference. Instead, the proposed DeeperLab image
parser performs whole image parsing with a significantly simpler, fully
convolutional approach that jointly addresses the semantic and instance
segmentation tasks in a single-shot manner, resulting in a streamlined system
that better lends itself to fast processing. For quantitative evaluation, we
use both the instance-based Panoptic Quality (PQ) metric and the proposed
region-based Parsing Covering (PC) metric, which better captures the image
parsing quality on 'stuff' classes and larger object instances. We report
experimental results on the challenging Mapillary Vistas dataset, in which our
single model achieves 31.95% (val) / 31.6% PQ (test) and 55.26% PC (val) with 3
frames per second (fps) on GPU or near real-time speed (22.6 fps on GPU) with
reduced accuracy.