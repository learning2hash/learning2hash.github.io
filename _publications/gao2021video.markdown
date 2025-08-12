---
layout: publication
title: Video Relation Detection Via Tracklet Based Visual Transformer
authors: Kaifeng Gao, Long Chen, Yifeng Huang, Jun Xiao
conference: Proceedings of the 29th ACM International Conference on Multimedia
year: 2021
bibkey: gao2021video
citations: 28
additional_links: [{name: Code, url: 'https://github.com/Dawn-LX/VidVRD-tracklets'},
  {name: Paper, url: 'https://arxiv.org/abs/2108.08669'}]
tags: ["Transformer Based ANN", "Video Retrieval"]
short_authors: Gao et al.
---
Video Visual Relation Detection (VidVRD), has received significant attention
of our community over recent years. In this paper, we apply the
state-of-the-art video object tracklet detection pipeline MEGA and deepSORT to
generate tracklet proposals. Then we perform VidVRD in a tracklet-based manner
without any pre-cutting operations. Specifically, we design a tracklet-based
visual Transformer. It contains a temporal-aware decoder which performs feature
interactions between the tracklets and learnable predicate query embeddings,
and finally predicts the relations. Experimental results strongly demonstrate
the superiority of our method, which outperforms other methods by a large
margin on the Video Relation Understanding (VRU) Grand Challenge in ACM
Multimedia 2021. Codes are released at
https://github.com/Dawn-LX/VidVRD-tracklets.