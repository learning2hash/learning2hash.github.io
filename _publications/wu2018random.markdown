---
layout: publication
title: Random Occlusion-recovery For Person Re-identification
authors: di Wu, Kun Zhang, Fei Cheng, Yang Zhao, Qi Liu, Chang-an Yuan, De-shuang
  Huang
conference: Journal of Imaging Science and Technology
year: 2019
bibkey: wu2018random
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.09970'}]
tags: ["Robustness"]
short_authors: Wu et al.
---
As a basic task of multi-camera surveillance system, person re-identification
aims to re-identify a query pedestrian observed from non-overlapping multiple
cameras or across different time with a single camera. Recently, deep
learning-based person re-identification models have achieved great success in
many benchmarks. However, these supervised models require a large amount of
labeled image data, and the process of manual labeling spends much manpower and
time. In this study, we introduce a method to automatically synthesize labeled
person images and adopt them to increase the sample number per identity for
person re-identification datasets. To be specific, we use block rectangles to
randomly occlude pedestrian images. Then, a generative adversarial network
(GAN) model is proposed to use paired occluded and original images to
synthesize the de-occluded images that similar but not identical to the
original image. Afterwards, we annotate the de-occluded images with the same
labels of their corresponding raw images and use them to augment the number of
samples per identity. Finally, we use the augmented datasets to train baseline
model. The experiment results on CUHK03, Market-1501 and DukeMTMC-reID datasets
show that the effectiveness of the proposed method.