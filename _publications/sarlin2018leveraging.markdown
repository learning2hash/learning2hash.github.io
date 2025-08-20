---
layout: publication
title: Leveraging Deep Visual Descriptors For Hierarchical Efficient Localization
authors: "Paul-Edouard Sarlin, Fr\xE9d\xE9ric Debraine, Marcin Dymczyk, Roland Siegwart,\
  \ Cesar Cadena"
conference: Arxiv
year: 2018
bibkey: sarlin2018leveraging
citations: 51
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.01019'}]
tags: [Efficiency, Robustness, Scalability, Evaluation, Neural Hashing]
short_authors: Sarlin et al.
---
Many robotics applications require precise pose estimates despite operating
in large and changing environments. This can be addressed by visual
localization, using a pre-computed 3D model of the surroundings. The pose
estimation then amounts to finding correspondences between 2D keypoints in a
query image and 3D points in the model using local descriptors. However,
computational power is often limited on robotic platforms, making this task
challenging in large-scale environments. Binary feature descriptors
significantly speed up this 2D-3D matching, and have become popular in the
robotics community, but also strongly impair the robustness to perceptual
aliasing and changes in viewpoint, illumination and scene structure. In this
work, we propose to leverage recent advances in deep learning to perform an
efficient hierarchical localization. We first localize at the map level using
learned image-wide global descriptors, and subsequently estimate a precise pose
from 2D-3D matches computed in the candidate places only. This restricts the
local search and thus allows to efficiently exploit powerful non-binary
descriptors usually dismissed on resource-constrained devices. Our approach
results in state-of-the-art localization performance while running in real-time
on a popular mobile platform, enabling new prospects for robotics research.