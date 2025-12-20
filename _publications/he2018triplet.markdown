---
layout: publication
title: Triplet-center Loss For Multi-view 3D Object Retrieval
authors: Xinwei He, Yang Zhou, Zhichao Zhou, Song Bai, Xiang Bai
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: he2018triplet
citations: 360
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.06189'}]
tags: ["CVPR", "Distance Metric Learning", "Evaluation", "Neural Hashing"]
short_authors: He et al.
---
Most existing 3D object recognition algorithms focus on leveraging the strong
discriminative power of deep learning models with softmax loss for the
classification of 3D data, while learning discriminative features with deep
metric learning for 3D object retrieval is more or less neglected. In the
paper, we study variants of deep metric learning losses for 3D object
retrieval, which did not receive enough attention from this area. First , two
kinds of representative losses, triplet loss and center loss, are introduced
which could learn more discriminative features than traditional classification
loss. Then, we propose a novel loss named triplet-center loss, which can
further enhance the discriminative power of the features. The proposed
triplet-center loss learns a center for each class and requires that the
distances between samples and centers from the same class are closer than those
from different classes. Extensive experimental results on two popular 3D object
retrieval benchmarks and two widely-adopted sketch-based 3D shape retrieval
benchmarks consistently demonstrate the effectiveness of our proposed loss, and
significant improvements have been achieved compared with the
state-of-the-arts.