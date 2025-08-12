---
layout: publication
title: High Efficiency Compression For Object Detection
authors: Hyomin Choi, Ivan V. Bajic
conference: 2018 IEEE International Conference on Acoustics, Speech and Signal Processing
  (ICASSP)
year: 2018
bibkey: choi2017high
citations: 43
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.11151'}]
tags: ["Efficiency"]
short_authors: Hyomin Choi, Ivan V. Bajic
---
Image and video compression has traditionally been tailored to human vision.
However, modern applications such as visual analytics and surveillance rely on
computers seeing and analyzing the images before (or instead of) humans. For
these applications, it is important to adjust compression to computer vision.
In this paper we present a bit allocation and rate control strategy that is
tailored to object detection. Using the initial convolutional layers of a
state-of-the-art object detector, we create an importance map that can guide
bit allocation to areas that are important for object detection. The proposed
method enables bit rate savings of 7% or more compared to default HEVC, at the
equivalent object detection rate.