---
layout: publication
title: Signature Of Geometric Centroids For 3D Local Shape Description And Partial
  Shape Matching
authors: Keke Tang, Peng Song, Xiaoping Chen
conference: Lecture Notes in Computer Science
year: 2017
bibkey: tang2016signature
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.08408'}]
tags: []
short_authors: Keke Tang, Peng Song, Xiaoping Chen
---
Depth scans acquired from different views may contain nuisances such as
noise, occlusion, and varying point density. We propose a novel Signature of
Geometric Centroids descriptor, supporting direct shape matching on the scans,
without requiring any preprocessing such as scan denoising or converting into a
mesh. First, we construct the descriptor by voxelizing the local shape within a
uniquely defined local reference frame and concatenating geometric centroid and
point density features extracted from each voxel. Second, we compare two
descriptors by employing only corresponding voxels that are both non-empty,
thus supporting matching incomplete local shape such as those close to scan
boundary. Third, we propose a descriptor saliency measure and compute it from a
descriptor-graph to improve shape matching performance. We demonstrate the
descriptor's robustness and effectiveness for shape matching by comparing it
with three state-of-the-art descriptors, and applying it to object/scene
reconstruction and 3D object recognition.