---
layout: publication
title: 'TCLR: Temporal Contrastive Learning For Video Representation'
authors: Ishan Dave, Rohit Gupta, Mamshad Nayeem Rizve, Mubarak Shah
conference: Computer Vision and Image Understanding
year: 2021
bibkey: dave2021tclr
citations: 139
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.07974'}]
tags: ["Datasets", "Distance Metric Learning", "Self-Supervised", "Supervised", "Video Retrieval"]
short_authors: Dave et al.
---
Contrastive learning has nearly closed the gap between supervised and
self-supervised learning of image representations, and has also been explored
for videos. However, prior work on contrastive learning for video data has not
explored the effect of explicitly encouraging the features to be distinct
across the temporal dimension. We develop a new temporal contrastive learning
framework consisting of two novel losses to improve upon existing contrastive
self-supervised video representation learning methods. The local-local temporal
contrastive loss adds the task of discriminating between non-overlapping clips
from the same video, whereas the global-local temporal contrastive aims to
discriminate between timesteps of the feature map of an input clip in order to
increase the temporal diversity of the learned features. Our proposed temporal
contrastive learning framework achieves significant improvement over the
state-of-the-art results in various downstream video understanding tasks such
as action recognition, limited-label action classification, and
nearest-neighbor video retrieval on multiple video datasets and backbones. We
also demonstrate significant improvement in fine-grained action classification
for visually similar classes. With the commonly used 3D ResNet-18 architecture
with UCF101 pretraining, we achieve 82.4% (+5.1% increase over the previous
best) top-1 accuracy on UCF101 and 52.9% (+5.4% increase) on HMDB51 action
classification, and 56.2% (+11.7% increase) Top-1 Recall on UCF101 nearest
neighbor video retrieval. Code released at github.com/DAVEISHAN/TCLR.