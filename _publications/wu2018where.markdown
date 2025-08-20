---
layout: publication
title: 'Where-and-when To Look: Deep Siamese Attention Networks For Video-based Person
  Re-identification'
authors: Lin Wu, Yang Wang, Junbin Gao, Xue Li
conference: IEEE Transactions on Multimedia
year: 2018
bibkey: wu2018where
citations: 235
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.01911'}]
tags: [Evaluation, Distance Metric Learning, Datasets]
short_authors: Wu et al.
---
Video-based person re-identification (re-id) is a central application in
surveillance systems with significant concern in security. Matching persons
across disjoint camera views in their video fragments is inherently challenging
due to the large visual variations and uncontrolled frame rates. There are two
steps crucial to person re-id, namely discriminative feature learning and
metric learning. However, existing approaches consider the two steps
independently, and they do not make full use of the temporal and spatial
information in videos. In this paper, we propose a Siamese attention
architecture that jointly learns spatiotemporal video representations and their
similarity metrics. The network extracts local convolutional features from
regions of each frame, and enhance their discriminative capability by focusing
on distinct regions when measuring the similarity with another pedestrian
video. The attention mechanism is embedded into spatial gated recurrent units
to selectively propagate relevant features and memorize their spatial
dependencies through the network. The model essentially learns which parts
(*where*) from which frames (*when*) are relevant and distinctive for
matching persons and attaches higher importance therein. The proposed Siamese
model is end-to-end trainable to jointly learn comparable hidden
representations for paired pedestrian videos and their similarity value.
Extensive experiments on three benchmark datasets show the effectiveness of
each component of the proposed deep network while outperforming
state-of-the-art methods.