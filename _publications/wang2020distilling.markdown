---
layout: publication
title: Distilling Knowledge By Mimicking Features
authors: Wang Guo-hua, Ge Yifan, Wu Jianxin
conference: "Arxiv"
year: 2020
bibkey: wang2020distilling
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2011.01424"}
tags: ['ARXIV', 'Independent', 'LSH']
---
Knowledge distillation (KD) is a popular method to train efficient networks
("student") with the help of high-capacity networks ("teacher"). Traditional
methods use the teacher's soft logits as extra supervision to train the student
network. In this paper, we argue that it is more advantageous to make the
student mimic the teacher's features in the penultimate layer. Not only the
student can directly learn more effective information from the teacher feature,
feature mimicking can also be applied for teachers trained without a softmax
layer. Experiments show that it can achieve higher accuracy than traditional
KD. To further facilitate feature mimicking, we decompose a feature vector into
the magnitude and the direction. We argue that the teacher should give more
freedom to the student feature's magnitude, and let the student pay more
attention on mimicking the feature direction. To meet this requirement, we
propose a loss term based on locality-sensitive hashing (LSH). With the help of
this new loss, our method indeed mimics feature directions more accurately,
relaxes constraints on feature magnitudes, and achieves state-of-the-art
distillation accuracy. We provide theoretical analyses of how LSH facilitates
feature direction mimicking, and further extend feature mimicking to
multi-label recognition and object detection.
