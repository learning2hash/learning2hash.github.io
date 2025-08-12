---
layout: publication
title: Hierarchical Spatial-aware Siamese Network For Thermal Infrared Object Tracking
authors: Xin Li, Qiao Liu, Nana Fan, Zhenyu He, Hongzhi Wang
conference: Knowledge-Based Systems
year: 2018
bibkey: li2017hierarchical
citations: 116
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.09539'}]
tags: []
short_authors: Li et al.
---
Most thermal infrared (TIR) tracking methods are discriminative, treating the
tracking problem as a classification task. However, the objective of the
classifier (label prediction) is not coupled to the objective of the tracker
(location estimation). The classification task focuses on the between-class
difference of the arbitrary objects, while the tracking task mainly deals with
the within-class difference of the same objects. In this paper, we cast the TIR
tracking problem as a similarity verification task, which is coupled well to
the objective of the tracking task. We propose a TIR tracker via a Hierarchical
Spatial-aware Siamese Convolutional Neural Network (CNN), named HSSNet. To
obtain both spatial and semantic features of the TIR object, we design a
Siamese CNN that coalesces the multiple hierarchical convolutional layers.
Then, we propose a spatial-aware network to enhance the discriminative ability
of the coalesced hierarchical feature. Subsequently, we train this network end
to end on a large visible video detection dataset to learn the similarity
between paired objects before we transfer the network into the TIR domain.
Next, this pre-trained Siamese network is used to evaluate the similarity
between the target template and target candidates. Finally, we locate the
candidate that is most similar to the tracked target. Extensive experimental
results on the benchmarks VOT-TIR 2015 and VOT-TIR 2016 show that our proposed
method achieves favourable performance compared to the state-of-the-art
methods.