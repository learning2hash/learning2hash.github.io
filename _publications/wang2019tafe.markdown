---
layout: publication
title: 'Tafe-net: Task-aware Feature Embeddings For Low Shot Learning'
authors: Xin Wang, Fisher Yu, Ruth Wang, Trevor Darrell, Joseph E. Gonzalez
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: wang2019tafe
citations: 113
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.05967'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Wang et al.
---
Learning good feature embeddings for images often requires substantial
training data. As a consequence, in settings where training data is limited
(e.g., few-shot and zero-shot learning), we are typically forced to use a
generic feature embedding across various tasks. Ideally, we want to construct
feature embeddings that are tuned for the given task. In this work, we propose
Task-Aware Feature Embedding Networks (TAFE-Nets) to learn how to adapt the
image representation to a new task in a meta learning fashion. Our network is
composed of a meta learner and a prediction network. Based on a task input, the
meta learner generates parameters for the feature layers in the prediction
network so that the feature embedding can be accurately adjusted for that task.
We show that TAFE-Net is highly effective in generalizing to new tasks or
concepts and evaluate the TAFE-Net on a range of benchmarks in zero-shot and
few-shot learning. Our model matches or exceeds the state-of-the-art on all
tasks. In particular, our approach improves the prediction accuracy of unseen
attribute-object pairs by 4 to 15 points on the challenging visual
attribute-object composition task.