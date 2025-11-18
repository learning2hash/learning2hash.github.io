---
layout: publication
title: Learning Sequence Descriptor Based On Spatio-temporal Attention For Visual
  Place Recognition
authors: Junqiao Zhao, Fenglin Zhang, Yingfeng Cai, Gengxuan Tian, Wenjie Mu, Chen
  Ye, Tiantian Feng
conference: IEEE Robotics and Automation Letters
year: 2023
bibkey: zhao2023learning
citations: 7
additional_links: [{name: Code, url: 'https://github.com/tiev-tongji/Spatio-Temporal-SeqVPR'},
  {name: Paper, url: 'https://arxiv.org/abs/2305.11467'}]
tags: ["Datasets", "Evaluation", "Robustness"]
short_authors: Zhao et al.
---
Visual Place Recognition (VPR) aims to retrieve frames from a geotagged
database that are located at the same place as the query frame. To improve the
robustness of VPR in perceptually aliasing scenarios, sequence-based VPR
methods are proposed. These methods are either based on matching between frame
sequences or extracting sequence descriptors for direct retrieval. However, the
former is usually based on the assumption of constant velocity, which is
difficult to hold in practice, and is computationally expensive and subject to
sequence length. Although the latter overcomes these problems, existing
sequence descriptors are constructed by aggregating features of multiple frames
only, without interaction on temporal information, and thus cannot obtain
descriptors with spatio-temporal discrimination.In this paper, we propose a
sequence descriptor that effectively incorporates spatio-temporal information.
Specifically, spatial attention within the same frame is utilized to learn
spatial feature patterns, while attention in corresponding local regions of
different frames is utilized to learn the persistence or change of features
over time. We use a sliding window to control the temporal range of attention
and use relative positional encoding to construct sequential relationships
between different features. This allows our descriptors to capture the
intrinsic dynamics in a sequence of frames.Comprehensive experiments on
challenging benchmark datasets show that the proposed approach outperforms
recent state-of-the-art methods.The code is available at
https://github.com/tiev-tongji/Spatio-Temporal-SeqVPR.