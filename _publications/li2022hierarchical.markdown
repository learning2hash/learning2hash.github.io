---
layout: publication
title: Hierarchical Compositional Representations For Few-shot Action Recognition
authors: Changzhen Li, Jie Zhang, Shuzhe Wu, Xin Jin, Shiguang Shan
conference: Computer Vision and Image Understanding
year: 2024
bibkey: li2022hierarchical
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.09424'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Li et al.
---
Recently action recognition has received more and more attention for its
comprehensive and practical applications in intelligent surveillance and
human-computer interaction. However, few-shot action recognition has not been
well explored and remains challenging because of data scarcity. In this paper,
we propose a novel hierarchical compositional representations (HCR) learning
approach for few-shot action recognition. Specifically, we divide a complicated
action into several sub-actions by carefully designed hierarchical clustering
and further decompose the sub-actions into more fine-grained spatially
attentional sub-actions (SAS-actions). Although there exist large differences
between base classes and novel classes, they can share similar patterns in
sub-actions or SAS-actions. Furthermore, we adopt the Earth Mover's Distance in
the transportation problem to measure the similarity between video samples in
terms of sub-action representations. It computes the optimal matching flows
between sub-actions as distance metric, which is favorable for comparing
fine-grained patterns. Extensive experiments show our method achieves the
state-of-the-art results on HMDB51, UCF101 and Kinetics datasets.