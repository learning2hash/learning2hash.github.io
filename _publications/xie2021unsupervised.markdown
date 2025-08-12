---
layout: publication
title: Unsupervised Video Person Re-identification Via Noise And Hard Frame Aware
  Clustering
authors: Pengyu Xie, Xin Xu, Zheng Wang, Toshihiko Yamasaki
conference: 2021 IEEE International Conference on Multimedia and Expo (ICME)
year: 2021
bibkey: xie2021unsupervised
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.05441'}]
tags: ["Unsupervised"]
short_authors: Xie et al.
---
Unsupervised video-based person re-identification (re-ID) methods extract
richer features from video tracklets than image-based ones. The
state-of-the-art methods utilize clustering to obtain pseudo-labels and train
the models iteratively. However, they underestimate the influence of two kinds
of frames in the tracklet: 1) noise frames caused by detection errors or heavy
occlusions exist in the tracklet, which may be allocated with unreliable labels
during clustering; 2) the tracklet also contains hard frames caused by pose
changes or partial occlusions, which are difficult to distinguish but
informative. This paper proposes a Noise and Hard frame Aware Clustering (NHAC)
method. NHAC consists of a graph trimming module and a node re-sampling module.
The graph trimming module obtains stable graphs by removing noise frame nodes
to improve the clustering accuracy. The node re-sampling module enhances the
training of hard frame nodes to learn rich tracklet information. Experiments
conducted on two video-based datasets demonstrate the effectiveness of the
proposed NHAC under the unsupervised re-ID setting.