---
layout: publication
title: Unsupervised Embedding Learning Via Invariant And Spreading Instance Feature
authors: Mang Ye, Xu Zhang, Pong C. Yuen, Shih-Fu Chang
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: ye2019unsupervised
citations: 570
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.03436'}]
tags: ["CVPR", "Distance Metric Learning", "Unsupervised"]
short_authors: Ye et al.
---
This paper studies the unsupervised embedding learning problem, which
requires an effective similarity measurement between samples in low-dimensional
embedding space. Motivated by the positive concentrated and negative separated
properties observed from category-wise supervised learning, we propose to
utilize the instance-wise supervision to approximate these properties, which
aims at learning data augmentation invariant and instance spread-out features.
To achieve this goal, we propose a novel instance based softmax embedding
method, which directly optimizes the `real' instance features on top of the
softmax function. It achieves significantly faster learning speed and higher
accuracy than all existing methods. The proposed method performs well for both
seen and unseen testing categories with cosine similarity. It also achieves
competitive performance even without pre-trained network over samples from
fine-grained categories.