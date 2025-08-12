---
layout: publication
title: 'Fcpose: Fully Convolutional Multi-person Pose Estimation With Dynamic Instance-aware
  Convolutions'
authors: Weian Mao, Zhi Tian, Xinlong Wang, Chunhua Shen
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: mao2021fcpose
citations: 58
additional_links: [{name: Code, url: 'https://git.io/AdelaiDet'}, {name: Paper, url: 'https://arxiv.org/abs/2105.14185'}]
tags: ["CVPR"]
short_authors: Mao et al.
---
We propose a fully convolutional multi-person pose estimation framework using
dynamic instance-aware convolutions, termed FCPose. Different from existing
methods, which often require ROI (Region of Interest) operations and/or
grouping post-processing, FCPose eliminates the ROIs and grouping
post-processing with dynamic instance-aware keypoint estimation heads. The
dynamic keypoint heads are conditioned on each instance (person), and can
encode the instance concept in the dynamically-generated weights of their
filters. Moreover, with the strong representation capacity of dynamic
convolutions, the keypoint heads in FCPose are designed to be very compact,
resulting in fast inference and making FCPose have almost constant inference
time regardless of the number of persons in the image. For example, on the COCO
dataset, a real-time version of FCPose using the DLA-34 backbone infers about
4.5x faster than Mask R-CNN (ResNet-101) (41.67 FPS vs. 9.26FPS) while
achieving improved performance. FCPose also offers better speed/accuracy
trade-off than other state-of-the-art methods. Our experiment results show that
FCPose is a simple yet effective multi-person pose estimation framework. Code
is available at: https://git.io/AdelaiDet