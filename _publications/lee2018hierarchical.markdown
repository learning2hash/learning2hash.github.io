---
layout: publication
title: Hierarchical Novelty Detection For Visual Object Recognition
authors: Kibok Lee, Kimin Lee, Kyle Min, Yuting Zhang, Jinwoo Shin, Honglak Lee
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: lee2018hierarchical
citations: 70
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.00722'}]
tags: ["CVPR"]
short_authors: Lee et al.
---
Deep neural networks have achieved impressive success in large-scale visual
object recognition tasks with a predefined set of classes. However, recognizing
objects of novel classes unseen during training still remains challenging. The
problem of detecting such novel classes has been addressed in the literature,
but most prior works have focused on providing simple binary or regressive
decisions, e.g., the output would be "known," "novel," or corresponding
confidence intervals. In this paper, we study more informative novelty
detection schemes based on a hierarchical classification framework. For an
object of a novel class, we aim for finding its closest super class in the
hierarchical taxonomy of known classes. To this end, we propose two different
approaches termed top-down and flatten methods, and their combination as well.
The essential ingredients of our methods are confidence-calibrated classifiers,
data relabeling, and the leave-one-out strategy for modeling novel classes
under the hierarchical taxonomy. Furthermore, our method can generate a
hierarchical embedding that leads to improved generalized zero-shot learning
performance in combination with other commonly-used semantic embeddings.