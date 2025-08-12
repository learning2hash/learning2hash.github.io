---
layout: publication
title: Do We Need Binary Features For 3D Reconstruction?
authors: Bin Fan, Qingqun Kong, Wei Sui, Zhiheng Wang, Xinchao Wang, Shiming Xiang,
  Chunhong Pan, Pascal Fua
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2016
bibkey: fan2016do
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.04502'}]
tags: ["CVPR"]
short_authors: Fan et al.
---
Binary features have been incrementally popular in the past few years due to
their low memory footprints and the efficient computation of Hamming distance
between binary descriptors. They have been shown with promising results on some
real time applications, e.g., SLAM, where the matching operations are relative
few. However, in computer vision, there are many applications such as 3D
reconstruction requiring lots of matching operations between local features.
Therefore, a natural question is that is the binary feature still a promising
solution to this kind of applications? To get the answer, this paper conducts a
comparative study of binary features and their matching methods on the context
of 3D reconstruction in a recently proposed large scale mutliview stereo
dataset. Our evaluations reveal that not all binary features are capable of
this task. Most of them are inferior to the classical SIFT based method in
terms of reconstruction accuracy and completeness with a not significant better
computational performance.