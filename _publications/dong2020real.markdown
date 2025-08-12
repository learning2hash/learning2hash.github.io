---
layout: publication
title: Real-time High-performance Semantic Image Segmentation Of Urban Street Scenes
authors: Genshun Dong, Yan Yan, Chunhua Shen, Hanzi Wang
conference: IEEE Transactions on Intelligent Transportation Systems
year: 2020
bibkey: dong2020real
citations: 114
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.08736'}]
tags: ["Efficiency"]
short_authors: Dong et al.
---
Deep Convolutional Neural Networks (DCNNs) have recently shown outstanding
performance in semantic image segmentation. However, state-of-the-art
DCNN-based semantic segmentation methods usually suffer from high computational
complexity due to the use of complex network architectures. This greatly limits
their applications in the real-world scenarios that require real-time
processing. In this paper, we propose a real-time high-performance DCNN-based
method for robust semantic segmentation of urban street scenes, which achieves
a good trade-off between accuracy and speed. Specifically, a Lightweight
Baseline Network with Atrous convolution and Attention (LBN-AA) is firstly used
as our baseline network to efficiently obtain dense feature maps. Then, the
Distinctive Atrous Spatial Pyramid Pooling (DASPP), which exploits the
different sizes of pooling operations to encode the rich and distinctive
semantic information, is developed to detect objects at multiple scales.
Meanwhile, a Spatial detail-Preserving Network (SPN) with shallow convolutional
layers is designed to generate high-resolution feature maps preserving the
detailed spatial information. Finally, a simple but practical Feature Fusion
Network (FFN) is used to effectively combine both shallow and deep features
from the semantic branch (DASPP) and the spatial branch (SPN), respectively.
Extensive experimental results show that the proposed method respectively
achieves the accuracy of 73.6% and 68.0% mean Intersection over Union (mIoU)
with the inference speed of 51.0 fps and 39.3 fps on the challenging Cityscapes
and CamVid test datasets (by only using a single NVIDIA TITAN X card). This
demonstrates that the proposed method offers excellent performance at the
real-time speed for semantic segmentation of urban street scenes.