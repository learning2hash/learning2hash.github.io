---
layout: publication
title: 'Deep Spatial Feature Reconstruction For Partial Person Re-identification:
  Alignment-free Approach'
authors: Lingxiao He, Jian Liang, Haiqing Li, Zhenan Sun
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: he2018deep
citations: 303
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.00881'}]
tags: ["CVPR"]
short_authors: He et al.
---
Partial person re-identification (re-id) is a challenging problem, where only
several partial observations (images) of people are available for matching.
However, few studies have provided flexible solutions to identifying a person
in an image containing arbitrary part of the body. In this paper, we propose a
fast and accurate matching method to address this problem. The proposed method
leverages Fully Convolutional Network (FCN) to generate fix-sized spatial
feature maps such that pixel-level features are consistent. To match a pair of
person images of different sizes, a novel method called Deep Spatial feature
Reconstruction (DSR) is further developed to avoid explicit alignment.
Specifically, DSR exploits the reconstructing error from popular dictionary
learning models to calculate the similarity between different spatial feature
maps. In that way, we expect that the proposed FCN can decrease the similarity
of coupled images from different persons and increase that from the same
person. Experimental results on two partial person datasets demonstrate the
efficiency and effectiveness of the proposed method in comparison with several
state-of-the-art partial person re-id approaches. Additionally, DSR achieves
competitive results on a benchmark person dataset Market1501 with 83.58%
Rank-1 accuracy.