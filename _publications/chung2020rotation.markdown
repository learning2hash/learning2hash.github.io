---
layout: publication
title: Rotation Invariant Aerial Image Retrieval With Group Convolutional Metric Learning
authors: Hyunseung Chung, Woo-Jeoung Nam, Seong-Whan Lee
conference: Arxiv
year: 2020
bibkey: chung2020rotation
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.09202'}]
tags: [Evaluation, Image Retrieval, Distance Metric Learning, Datasets, Robustness]
short_authors: Hyunseung Chung, Woo-Jeoung Nam, Seong-Whan Lee
---
Remote sensing image retrieval (RSIR) is the process of ranking database
images depending on the degree of similarity compared to the query image. As
the complexity of RSIR increases due to the diversity in shooting range, angle,
and location of remote sensors, there is an increasing demand for methods to
address these issues and improve retrieval performance. In this work, we
introduce a novel method for retrieving aerial images by merging group
convolution with attention mechanism and metric learning, resulting in
robustness to rotational variations. For refinement and emphasis on important
features, we applied channel attention in each group convolution stage. By
utilizing the characteristics of group convolution and channel-wise attention,
it is possible to acknowledge the equality among rotated but identically
located images. The training procedure has two main steps: (i) training the
network with Aerial Image Dataset (AID) for classification, (ii) fine-tuning
the network with triplet-loss for retrieval with Google Earth South Korea and
NWPU-RESISC45 datasets. Results show that the proposed method performance
exceeds other state-of-the-art retrieval methods in both rotated and original
environments. Furthermore, we utilize class activation maps (CAM) to visualize
the distinct difference of main features between our method and baseline,
resulting in better adaptability in rotated environments.