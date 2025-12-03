---
layout: publication
title: Temporal Context Aggregation For Video Retrieval With Contrastive Learning
authors: Jie Shao, Xin Wen, Bingchen Zhao, Xiangyang Xue
conference: Arxiv
year: 2020
bibkey: shao2020temporal
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2008.01334'}]
tags: ["Datasets", "Evaluation", "Self-Supervised", "Supervised", "Video Retrieval"]
short_authors: Shao et al.
---
The current research focus on Content-Based Video Retrieval requires
higher-level video representation describing the long-range semantic
dependencies of relevant incidents, events, etc. However, existing methods
commonly process the frames of a video as individual images or short clips,
making the modeling of long-range semantic dependencies difficult. In this
paper, we propose TCA (Temporal Context Aggregation for Video Retrieval), a
video representation learning framework that incorporates long-range temporal
information between frame-level features using the self-attention mechanism. To
train it on video retrieval datasets, we propose a supervised contrastive
learning method that performs automatic hard negative mining and utilizes the
memory bank mechanism to increase the capacity of negative samples. Extensive
experiments are conducted on multiple video retrieval tasks, such as
CC_WEB_VIDEO, FIVR-200K, and EVVE. The proposed method shows a significant
performance advantage (~17% mAP on FIVR-200K) over state-of-the-art methods
with video-level features, and deliver competitive results with 22x faster
inference time comparing with frame-level features.