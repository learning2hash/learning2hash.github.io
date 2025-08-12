---
layout: publication
title: 'From Keypoints To Object Landmarks Via Self-training Correspondence: A Novel
  Approach To Unsupervised Landmark Discovery'
authors: Dimitrios Mallis, Enrique Sanchez, Matt Bell, Georgios Tzimiropoulos
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2023
bibkey: mallis2022keypoints
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.15895'}]
tags: ["Self-Supervised"]
short_authors: Mallis et al.
---
This paper proposes a novel paradigm for the unsupervised learning of object
landmark detectors. Contrary to existing methods that build on auxiliary tasks
such as image generation or equivariance, we propose a self-training approach
where, departing from generic keypoints, a landmark detector and descriptor is
trained to improve itself, tuning the keypoints into distinctive landmarks. To
this end, we propose an iterative algorithm that alternates between producing
new pseudo-labels through feature clustering and learning distinctive features
for each pseudo-class through contrastive learning. With a shared backbone for
the landmark detector and descriptor, the keypoint locations progressively
converge to stable landmarks, filtering those less stable. Compared to previous
works, our approach can learn points that are more flexible in terms of
capturing large viewpoint changes. We validate our method on a variety of
difficult datasets, including LS3D, BBCPose, Human3.6M and PennAction,
achieving new state of the art results.