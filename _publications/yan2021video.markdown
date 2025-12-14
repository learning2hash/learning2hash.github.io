---
layout: publication
title: Video-text Pre-training With Learned Regions
authors: Rui Yan, Mike Zheng Shou, Yixiao Ge, Alex Jinpeng Wang, Xudong Lin, Guanyu
  Cai, Jinhui Tang
conference: Arxiv
year: 2021
bibkey: yan2021video
citations: 7
additional_links: [{name: Code, url: 'https://github.com/ruiyan1995/Region_Learner'},
  {name: Paper, url: 'https://arxiv.org/abs/2112.01194'}]
tags: [Text Retrieval, Evaluation, Scalability, Datasets]
short_authors: Yan et al.
---
Video-Text pre-training aims at learning transferable representations from
large-scale video-text pairs via aligning the semantics between visual and
textual information. State-of-the-art approaches extract visual features from
raw pixels in an end-to-end fashion. However, these methods operate at
frame-level directly and thus overlook the spatio-temporal structure of objects
in video, which yet has a strong synergy with nouns in textual descriptions. In
this work, we propose a simple yet effective module for video-text
representation learning, namely RegionLearner, which can take into account the
structure of objects during pre-training on large-scale video-text pairs. Given
a video, our module (1) first quantizes visual features into semantic clusters,
then (2) generates learnable masks and uses them to aggregate the features
belonging to the same semantic region, and finally (3) models the interactions
between different aggregated regions. In contrast to using off-the-shelf object
detectors, our proposed module does not require explicit supervision and is
much more computationally efficient. We pre-train the proposed approach on the
public WebVid2M and CC3M datasets. Extensive evaluations on four downstream
video-text retrieval benchmarks clearly demonstrate the effectiveness of our
RegionLearner. The code will be available at
https://github.com/ruiyan1995/Region_Learner.