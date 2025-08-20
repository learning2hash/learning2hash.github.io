---
layout: publication
title: Matching Neuromorphic Events And Color Images Via Adversarial Learning
authors: Fang Xu, Shijie Lin, Wen Yang, Lei Yu, Dengxin Dai, Gui-Song Xia
conference: Arxiv
year: 2020
bibkey: xu2020matching
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.00636'}]
tags: [Efficiency, Robustness, Memory Efficiency, Datasets, Image Retrieval]
short_authors: Xu et al.
---
The event camera has appealing properties: high dynamic range, low latency,
low power consumption and low memory usage, and thus provides complementariness
to conventional frame-based cameras. It only captures the dynamics of a scene
and is able to capture almost "continuous" motion. However, different from
frame-based camera that reflects the whole appearance as scenes are, the event
camera casts away the detailed characteristics of objects, such as texture and
color. To take advantages of both modalities, the event camera and frame-based
camera are combined together for various machine vision tasks. Then the
cross-modal matching between neuromorphic events and color images plays a vital
and essential role. In this paper, we propose the Event-Based Image Retrieval
(EBIR) problem to exploit the cross-modal matching task. Given an event stream
depicting a particular object as query, the aim is to retrieve color images
containing the same object. This problem is challenging because there exists a
large modality gap between neuromorphic events and color images. We address the
EBIR problem by proposing neuromorphic Events-Color image Feature Learning
(ECFL). Particularly, the adversarial learning is employed to jointly model
neuromorphic events and color images into a common embedding space. We also
contribute to the community N-UKbench and EC180 dataset to promote the
development of EBIR problem. Extensive experiments on our datasets show that
the proposed method is superior in learning effective modality-invariant
representation to link two different modalities.