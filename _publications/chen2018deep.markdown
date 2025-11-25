---
layout: publication
title: Deep Cross-modality Adaptation Via Semantics Preserving Adversarial Learning
  For Sketch-based 3D Shape Retrieval
authors: Jiaxin Chen, Yi Fang
conference: Lecture Notes in Computer Science
year: 2018
bibkey: chen2018deep
citations: 68
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.01806'}]
tags: ["Distance Metric Learning", "Multimodal Retrieval"]
short_authors: Jiaxin Chen, Yi Fang
---
Due to the large cross-modality discrepancy between 2D sketches and 3D
shapes, retrieving 3D shapes by sketches is a significantly challenging task.
To address this problem, we propose a novel framework to learn a discriminative
deep cross-modality adaptation model in this paper. Specifically, we first
separately adopt two metric networks, following two deep convolutional neural
networks (CNNs), to learn modality-specific discriminative features based on an
importance-aware metric learning method. Subsequently, we explicitly introduce
a cross-modality transformation network to compensate for the divergence
between two modalities, which can transfer features of 2D sketches to the
feature space of 3D shapes. We develop an adversarial learning based method to
train the transformation model, by simultaneously enhancing the holistic
correlations between data distributions of two modalities, and mitigating the
local semantic divergences through minimizing a cross-modality mean discrepancy
term. Experimental results on the SHREC 2013 and SHREC 2014 datasets clearly
show the superior retrieval performance of our proposed model, compared to the
state-of-the-art approaches.