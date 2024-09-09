---
layout: publication
title: "Unsupervised Domain-adaptive Hash for Networks"
authors: He Tao, Gao Lianli, Song Jingkuan, Li Yuan-Fang
conference: "Arxiv"
year: 2021
bibkey: he2021unsupervised
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2108.09136"}
tags: ['ARXIV', 'Supervised', 'TIP', 'Unsupervised']
---
Abundant real-world data can be naturally represented by large-scale networks,
which demands efficient and effective learning algorithms. At the same time,
labels may only be available for some networks, which demands these algorithms
to be able to adapt to unlabeled networks. Domain-adaptive hash learning has
enjoyed considerable success in the computer vision community in many practical
tasks due to its lower cost in both retrieval time and storage footprint.
However, it has not been applied to multiple-domain networks. In this work, we
bridge this gap by developing an unsupervised domain-adaptive hash learning
method for networks, dubbed UDAH. Specifically, we develop four {task-specific
yet correlated} components: (1) network structure preservation via a hard
groupwise contrastive loss, (2) relaxation-free supervised hashing, (3) cross-
domain intersected discriminators, and (4) semantic center alignment. We conduct
a wide range of experiments to evaluate the effectiveness and efficiency of our
method on a range of tasks including link prediction, node classification, and
neighbor recommendation. Our evaluation results demonstrate that our model
achieves better performance than the state-of-the-art conventional discrete
embedding methods over all the tasks.
