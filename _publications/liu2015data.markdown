---
layout: publication
title: Data-driven Scene Understanding With Adaptively Retrieved Exemplars
authors: Xionghao Liu, Wei Yang, Liang Lin, Qing Wang, Zhaoquan Cai, Jianhuang Lai
conference: IEEE MultiMedia
year: 2015
bibkey: liu2015data
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1502.00749'}]
tags: []
short_authors: Liu et al.
---
This article investigates a data-driven approach for semantically scene
understanding, without pixelwise annotation and classifier training. Our
framework parses a target image with two steps: (i) retrieving its exemplars
(i.e. references) from an image database, where all images are unsegmented but
annotated with tags; (ii) recovering its pixel labels by propagating semantics
from the references. We present a novel framework making the two steps mutually
conditional and bootstrapped under the probabilistic Expectation-Maximization
(EM) formulation. In the first step, the references are selected by jointly
matching their appearances with the target as well as the semantics (i.e. the
assigned labels of the target and the references). We process the second step
via a combinatorial graphical representation, in which the vertices are
superpixels extracted from the target and its selected references. Then we
derive the potentials of assigning labels to one vertex of the target, which
depend upon the graph edges that connect the vertex to its spatial neighbors of
the target and to its similar vertices of the references. Besides, the proposed
framework can be naturally applied to perform image annotation on new test
images. In the experiments, we validate our approach on two public databases,
and demonstrate superior performances over the state-of-the-art methods in both
semantic segmentation and image annotation tasks.