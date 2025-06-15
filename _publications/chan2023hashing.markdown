---
layout: publication
title: Hashing Neural Video Decomposition With Multiplicative Residuals In Space-time
authors: Chan Cheng-hung, Yuan Cheng-yang, Sun Cheng, Chen Hwann-tzong
conference: "Arxiv"
year: 2023
citations: 0
bibkey: chan2023hashing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2309.14022"}
tags: ['ARXIV']
---
We present a video decomposition method that facilitates layer-based editing
of videos with spatiotemporally varying lighting and motion effects. Our neural
model decomposes an input video into multiple layered representations, each
comprising a 2D texture map, a mask for the original video, and a
multiplicative residual characterizing the spatiotemporal variations in
lighting conditions. A single edit on the texture maps can be propagated to the
corresponding locations in the entire video frames while preserving other
contents' consistencies. Our method efficiently learns the layer-based neural
representations of a 1080p video in 25s per frame via coordinate hashing and
allows real-time rendering of the edited result at 71 fps on a single GPU.
Qualitatively, we run our method on various videos to show its effectiveness in
generating high-quality editing effects. Quantitatively, we propose to adopt
feature-tracking evaluation metrics for objectively assessing the consistency
of video editing. Project page: https://lightbulb12294.github.io/hashing-nvd/
