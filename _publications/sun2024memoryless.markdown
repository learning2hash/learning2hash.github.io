---
layout: publication
title: Memoryless Multimodal Anomaly Detection Via Student-teacher Network And Signed
  Distance Learning
authors: Zhongbin Sun, Xiaolong Li, Yiran Li, Yue Ma
conference: Arxiv
year: 2024
bibkey: sun2024memoryless
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.05378'}]
tags: []
short_authors: Sun et al.
---
Unsupervised anomaly detection is a challenging computer vision task, in
which 2D-based anomaly detection methods have been extensively studied.
However, multimodal anomaly detection based on RGB images and 3D point clouds
requires further investigation. The existing methods are mainly inspired by
memory bank based methods commonly used in 2D-based anomaly detection, which
may cost extra memory for storing mutimodal features. In present study, a novel
memoryless method MDSS is proposed for multimodal anomaly detection, which
employs a light-weighted student-teacher network and a signed distance function
to learn from RGB images and 3D point clouds respectively, and complements the
anomaly information from the two modalities. Specifically, a student-teacher
network is trained with normal RGB images and masks generated from point clouds
by a dynamic loss, and the anomaly score map could be obtained from the
discrepancy between the output of student and teacher. Furthermore, the signed
distance function learns from normal point clouds to predict the signed
distances between points and surface, and the obtained signed distances are
used to generate anomaly score map. Subsequently, the anomaly score maps are
aligned to generate the final anomaly score map for detection. The experimental
results indicate that MDSS is comparable but more stable than the SOTA memory
bank based method Shape-guided, and furthermore performs better than other
baseline methods.