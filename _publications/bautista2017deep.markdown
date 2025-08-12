---
layout: publication
title: Deep Unsupervised Similarity Learning Using Partially Ordered Sets
authors: "Miguel A Bautista, Artsiom Sanakoyeu, Bj\xF6rn Ommer"
conference: 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2017
bibkey: bautista2017deep
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.02268'}]
tags: ["CVPR", "Unsupervised"]
short_authors: "Miguel A Bautista, Artsiom Sanakoyeu, Bj\xF6rn Ommer"
---
Unsupervised learning of visual similarities is of paramount importance to
computer vision, particularly due to lacking training data for fine-grained
similarities. Deep learning of similarities is often based on relationships
between pairs or triplets of samples. Many of these relations are unreliable
and mutually contradicting, implying inconsistencies when trained without
supervision information that relates different tuples or triplets to each
other. To overcome this problem, we use local estimates of reliable
(dis-)similarities to initially group samples into compact surrogate classes
and use local partial orders of samples to classes to link classes to each
other. Similarity learning is then formulated as a partial ordering task with
soft correspondences of all samples to classes. Adopting a strategy of
self-supervision, a CNN is trained to optimally represent samples in a mutually
consistent manner while updating the classes. The similarity learning and
grouping procedure are integrated in a single model and optimized jointly. The
proposed unsupervised approach shows competitive performance on detailed pose
estimation and object classification.