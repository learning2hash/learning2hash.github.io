---
layout: publication
title: 'Visual Compiler: Synthesizing A Scene-specific Pedestrian Detector And Pose
  Estimator'
authors: Namhoon Lee, Xinshuo Weng, Vishnu Naresh Boddeti, Yu Zhang, Fares Beainy,
  Kris Kitani, Takeo Kanade
conference: Arxiv
year: 2016
bibkey: lee2016visual
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.05234'}]
tags: []
short_authors: Lee et al.
---
We introduce the concept of a Visual Compiler that generates a scene specific
pedestrian detector and pose estimator without any pedestrian observations.
Given a single image and auxiliary scene information in the form of camera
parameters and geometric layout of the scene, the Visual Compiler first infers
geometrically and photometrically accurate images of humans in that scene
through the use of computer graphics rendering. Using these renders we learn a
scene-and-region specific spatially-varying fully convolutional neural network,
for simultaneous detection, pose estimation and segmentation of pedestrians. We
demonstrate that when real human annotated data is scarce or non-existent, our
data generation strategy can provide an excellent solution for bootstrapping
human detection and pose estimation. Experimental results show that our
approach outperforms off-the-shelf state-of-the-art pedestrian detectors and
pose estimators that are trained on real data.