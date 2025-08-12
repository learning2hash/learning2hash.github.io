---
layout: publication
title: Visual Translation Embedding Network For Visual Relation Detection
authors: Hanwang Zhang, Zawlin Kyaw, Shih-Fu Chang, Tat-Seng Chua
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: zhang2017visual
citations: 549
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.08319'}]
tags: ["CVPR"]
short_authors: Zhang et al.
---
Visual relations, such as "person ride bike" and "bike next to car", offer a
comprehensive scene understanding of an image, and have already shown their
great utility in connecting computer vision and natural language. However, due
to the challenging combinatorial complexity of modeling
subject-predicate-object relation triplets, very little work has been done to
localize and predict visual relations. Inspired by the recent advances in
relational representation learning of knowledge bases and convolutional object
detection networks, we propose a Visual Translation Embedding network (VTransE)
for visual relation detection. VTransE places objects in a low-dimensional
relation space where a relation can be modeled as a simple vector translation,
i.e., subject + predicate \(\approx\) object. We propose a novel feature
extraction layer that enables object-relation knowledge transfer in a
fully-convolutional fashion that supports training and inference in a single
forward/backward pass. To the best of our knowledge, VTransE is the first
end-to-end relation detection network. We demonstrate the effectiveness of
VTransE over other state-of-the-art methods on two large-scale datasets: Visual
Relationship and Visual Genome. Note that even though VTransE is a purely
visual model, it is still competitive to the Lu's multi-modal model with
language priors.