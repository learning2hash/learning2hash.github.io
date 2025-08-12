---
layout: publication
title: Faster And Accurate Classification For JPEG2000 Compressed Images In Networked
  Applications
authors: Lahiru D. Chamain, Zhi Ding
conference: Arxiv
year: 2019
bibkey: chamain2019faster
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.05638'}]
tags: ["Evaluation"]
short_authors: Lahiru D. Chamain, Zhi Ding
---
JPEG2000 (j2k) is a highly popular format for image and video
compression.With the rapidly growing applications of cloud based image
classification, most existing j2k-compatible schemes would stream compressed
color images from the source before reconstruction at the processing center as
inputs to deep CNNs. We propose to remove the computationally costly
reconstruction step by training a deep CNN image classifier using the CDF 9/7
Discrete Wavelet Transformed (DWT) coefficients directly extracted from
j2k-compressed images. We demonstrate additional computation savings by
utilizing shallower CNN to achieve classification of good accuracy in the DWT
domain. Furthermore, we show that traditional augmentation transforms such as
flipping/shifting are ineffective in the DWT domain and present different
augmentation transformations to achieve more accurate classification without
any additional cost. This way, faster and more accurate classification is
possible for j2k encoded images without image reconstruction. Through
experiments on CIFAR-10 and Tiny ImageNet data sets, we show that the
performance of the proposed solution is consistent for image transmission over
limited channel bandwidth.