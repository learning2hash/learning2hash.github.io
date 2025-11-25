---
layout: publication
title: Semi-supervised Keypoint Detector And Descriptor For Retinal Image Matching
authors: Jiazhen Liu, Xirong Li, Qijie Wei, Jie Xu, Dayong Ding
conference: Lecture Notes in Computer Science
year: 2022
bibkey: liu2022semi
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.07932'}]
tags: ["Datasets", "Distance Metric Learning", "Supervised"]
short_authors: Liu et al.
---
For retinal image matching (RIM), we propose SuperRetina, the first
end-to-end method with jointly trainable keypoint detector and descriptor.
SuperRetina is trained in a novel semi-supervised manner. A small set of
(nearly 100) images are incompletely labeled and used to supervise the network
to detect keypoints on the vascular tree. To attack the incompleteness of
manual labeling, we propose Progressive Keypoint Expansion to enrich the
keypoint labels at each training epoch. By utilizing a keypoint-based improved
triplet loss as its description loss, SuperRetina produces highly
discriminative descriptors at full input image size. Extensive experiments on
multiple real-world datasets justify the viability of SuperRetina. Even with
manual labeling replaced by auto labeling and thus making the training process
fully manual-annotation free, SuperRetina compares favorably against a number
of strong baselines for two RIM tasks, i.e. image registration and identity
verification. SuperRetina will be open source.