---
layout: publication
title: 'Teachclip: Multi-grained Teaching For Efficient Text-to-video Retrieval'
authors: Kaibin Tian, Ruixiang Zhao, Hu Hu, Runquan Xie, Fengzong Lian, Zhanhui Kang,
  Xirong Li
conference: Arxiv
year: 2023
bibkey: tian2023teachclip
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.01217'}]
tags: ["Scalability", "Video Retrieval"]
short_authors: Tian et al.
---
For text-to-video retrieval (T2VR), which aims to retrieve unlabeled videos
by ad-hoc textual queries, CLIP-based methods are dominating. Compared to
CLIP4Clip which is efficient and compact, the state-of-the-art models tend to
compute video-text similarity by fine-grained cross-modal feature interaction
and matching, putting their scalability for large-scale T2VR into doubt. For
efficient T2VR, we propose TeachCLIP with multi-grained teaching to let a
CLIP4Clip based student network learn from more advanced yet computationally
heavy models such as X-CLIP, TS2-Net and X-Pool . To improve the student's
learning capability, we add an Attentional frame-Feature Aggregation (AFA)
block, which by design adds no extra storage/computation overhead at the
retrieval stage. While attentive weights produced by AFA are commonly used for
combining frame-level features, we propose a novel use of the weights to let
them imitate frame-text relevance estimated by the teacher network. As such,
AFA provides a fine-grained learning (teaching) channel for the student
(teacher). Extensive experiments on multiple public datasets justify the
viability of the proposed method.