---
layout: publication
title: Scale Match For Tiny Person Detection
authors: Xuehui Yu, Yuqi Gong, Nan Jiang, Qixiang Ye, Zhenjun Han
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2020
bibkey: yu2019scale
citations: 249
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.10664'}]
tags: ["Scalability"]
short_authors: Yu et al.
---
Visual object detection has achieved unprecedented ad-vance with the rise of
deep convolutional neural networks.However, detecting tiny objects (for example
tiny per-sons less than 20 pixels) in large-scale images remainsnot well
investigated. The extremely small objects raisea grand challenge about feature
representation while themassive and complex backgrounds aggregate the risk
offalse alarms. In this paper, we introduce a new benchmark,referred to as
TinyPerson, opening up a promising directionfor tiny object detection in a long
distance and with mas-sive backgrounds. We experimentally find that the scale
mis-match between the dataset for network pre-training and thedataset for
detector learning could deteriorate the featurerepresentation and the
detectors. Accordingly, we proposea simple yet effective Scale Match approach
to align theobject scales between the two datasets for favorable tiny-object
representation. Experiments show the significantperformance gain of our
proposed approach over state-of-the-art detectors, and the challenging aspects
of TinyPersonrelated to real-world scenarios. The TinyPerson benchmarkand the
code for our approach will be publicly
available(https://github.com/ucas-vg/TinyBenchmark).(Attention: evaluation
rules of AP have updated in benchmark after this paper accepted, So this paper
use old rules. we will keep old rules of AP in benchmark, but we recommand the
new and we will use the new in latter research.)