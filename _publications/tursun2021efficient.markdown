---
layout: publication
title: An Efficient Framework For Zero-shot Sketch-based Image Retrieval
authors: Osman Tursun, Simon Denman, Sridha Sridharan, Ethan Goan, Clinton Fookes
conference: Pattern Recognition
year: 2022
bibkey: tursun2021efficient
citations: 51
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.04016'}]
tags: ["Image Retrieval"]
short_authors: Tursun et al.
---
Recently, Zero-shot Sketch-based Image Retrieval (ZS-SBIR) has attracted the
attention of the computer vision community due to it's real-world applications,
and the more realistic and challenging setting than found in SBIR. ZS-SBIR
inherits the main challenges of multiple computer vision problems including
content-based Image Retrieval (CBIR), zero-shot learning and domain adaptation.
The majority of previous studies using deep neural networks have achieved
improved results through either projecting sketch and images into a common
low-dimensional space or transferring knowledge from seen to unseen classes.
However, those approaches are trained with complex frameworks composed of
multiple deep convolutional neural networks (CNNs) and are dependent on
category-level word labels. This increases the requirements on training
resources and datasets. In comparison, we propose a simple and efficient
framework that does not require high computational training resources, and can
be trained on datasets without semantic categorical labels. Furthermore, at
training and inference stages our method only uses a single CNN. In this work,
a pre-trained ImageNet CNN (e.g., ResNet50) is fine-tuned with three proposed
learning objects: domain-aware quadruplet loss, semantic classification loss,
and semantic knowledge preservation loss. The domain-aware quadruplet and
semantic classification losses are introduced to learn discriminative, semantic
and domain invariant features through considering ZS-SBIR as object detection
and verification problem. ...