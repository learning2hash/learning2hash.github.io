---
layout: publication
title: Semantic Representation And Dependency Learning For Multi-label Image Recognition
authors: Tao Pu, Mingzhan Sun, Hefeng Wu, Tianshui Chen, Ling Tian, Liang Lin
conference: Neurocomputing
year: 2023
bibkey: pu2022semantic
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.03795'}]
tags: []
short_authors: Pu et al.
---
Recently many multi-label image recognition (MLR) works have made significant
progress by introducing pre-trained object detection models to generate lots of
proposals or utilizing statistical label co-occurrence enhance the correlation
among different categories. However, these works have some limitations: (1) the
effectiveness of the network significantly depends on pre-trained object
detection models that bring expensive and unaffordable computation; (2) the
network performance degrades when there exist occasional co-occurrence objects
in images, especially for the rare categories. To address these problems, we
propose a novel and effective semantic representation and dependency learning
(SRDL) framework to learn category-specific semantic representation for each
category and capture semantic dependency among all categories. Specifically, we
design a category-specific attentional regions (CAR) module to generate
channel/spatial-wise attention matrices to guide model to focus on
semantic-aware regions. We also design an object erasing (OE) module to
implicitly learn semantic dependency among categories by erasing semantic-aware
regions to regularize the network training. Extensive experiments and
comparisons on two popular MLR benchmark datasets (i.e., MS-COCO and Pascal VOC
2007) demonstrate the effectiveness of the proposed framework over current
state-of-the-art algorithms.