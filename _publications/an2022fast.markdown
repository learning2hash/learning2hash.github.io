---
layout: publication
title: Fast and Incremental Loop Closure Detection with Deep Features and Proximity
  Graphs
authors: An et al.
conference: Journal of Field Robotics
year: 2022
bibkey: an2022fast
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.11703'}]
tags: ["Graph-Based-ANN"]
---
In recent years, the robotics community has extensively examined methods
concerning the place recognition task within the scope of simultaneous
localization and mapping applications.This article proposes an appearance-based
loop closure detection pipeline named ``FILD++" (Fast and Incremental Loop
closure Detection).First, the system is fed by consecutive images and, via
passing them twice through a single convolutional neural network, global and
local deep features are extracted.Subsequently, a hierarchical navigable
small-world graph incrementally constructs a visual database representing the
robot's traversed path based on the computed global features.Finally, a query
image, grabbed each time step, is set to retrieve similar locations on the
traversed route.An image-to-image pairing follows, which exploits local
features to evaluate the spatial information. Thus, in the proposed article, we
propose a single network for global and local feature extraction in contrast to
our previous work (FILD), while an exhaustive search for the verification
process is adopted over the generated deep local features avoiding the
utilization of hash codes. Exhaustive experiments on eleven publicly available
datasets exhibit the system's high performance (achieving the highest recall
score on eight of them) and low execution times (22.05 ms on average in New
College, which is the largest one containing 52480 images) compared to other
state-of-the-art approaches.