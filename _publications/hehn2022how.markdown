---
layout: publication
title: How Do Cross-view And Cross-modal Alignment Affect Representations In Contrastive
  Learning?
authors: Thomas M. Hehn, Julian F. P. Kooij, Dariu M. Gavrila
conference: Arxiv
year: 2022
bibkey: hehn2022how
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.13309'}]
tags: []
short_authors: Thomas M. Hehn, Julian F. P. Kooij, Dariu M. Gavrila
---
Various state-of-the-art self-supervised visual representation learning
approaches take advantage of data from multiple sensors by aligning the feature
representations across views and/or modalities. In this work, we investigate
how aligning representations affects the visual features obtained from
cross-view and cross-modal contrastive learning on images and point clouds. On
five real-world datasets and on five tasks, we train and evaluate 108 models
based on four pretraining variations. We find that cross-modal representation
alignment discards complementary visual information, such as color and texture,
and instead emphasizes redundant depth cues. The depth cues obtained from
pretraining improve downstream depth prediction performance. Also overall,
cross-modal alignment leads to more robust encoders than pre-training by
cross-view alignment, especially on depth prediction, instance segmentation,
and object detection.