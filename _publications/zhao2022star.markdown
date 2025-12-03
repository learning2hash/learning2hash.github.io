---
layout: publication
title: 'STAR-GNN: Spatial-temporal Video Representation For Content-based Retrieval'
authors: Guoping Zhao, Bingqing Zhang, Mingyu Zhang, Yaxian Li, Jiajun Liu, Ji-Rong
  Wen
conference: 2022 IEEE International Conference on Multimedia and Expo (ICME)
year: 2022
bibkey: zhao2022star
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.06966'}]
tags: ["Distance Metric Learning", "Evaluation", "Tools & Libraries", "Video Retrieval"]
short_authors: Zhao et al.
---
We propose a video feature representation learning framework called STAR-GNN,
which applies a pluggable graph neural network component on a multi-scale
lattice feature graph. The essence of STAR-GNN is to exploit both the temporal
dynamics and spatial contents as well as visual connections between regions at
different scales in the frames. It models a video with a lattice feature graph
in which the nodes represent regions of different granularity, with weighted
edges that represent the spatial and temporal links. The contextual nodes are
aggregated simultaneously by graph neural networks with parameters trained with
retrieval triplet loss. In the experiments, we show that STAR-GNN effectively
implements a dynamic attention mechanism on video frame sequences, resulting in
the emphasis for dynamic and semantically rich content in the video, and is
robust to noise and redundancies. Empirical results show that STAR-GNN achieves
state-of-the-art performance for Content-Based Video Retrieval.