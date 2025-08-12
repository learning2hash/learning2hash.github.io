---
layout: publication
title: Locality-aware Rotated Ship Detection In High-resolution Remote Sensing Imagery
  Based On Multi-scale Convolutional Network
authors: Lingyi Liu, Yunpeng Bai, Ying Li
conference: Arxiv
year: 2020
bibkey: liu2020locality
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.12326'}]
tags: []
short_authors: Lingyi Liu, Yunpeng Bai, Ying Li
---
Ship detection has been an active and vital topic in the field of remote
sensing for a decade, but it is still a challenging problem due to the large
scale variations, the high aspect ratios, the intensive arrangement, and the
background clutter disturbance. In this letter, we propose a locality-aware
rotated ship detection (LARSD) framework based on a multi-scale convolutional
neural network (CNN) to tackle these issues. The proposed framework applies a
UNet-like multi-scale CNN to generate multi-scale feature maps with high-level
semantic information in high resolution. Then, a rotated anchor-based
regression is applied for directly predicting the probability, the edge
distances, and the angle of ships. Finally, a locality-aware score alignment is
proposed to fix the mismatch between classification results and location
results caused by the independence of each subnet. Furthermore, to enlarge the
datasets of ship detection, we build a new high-resolution ship detection
(HRSD) dataset, where 2499 images and 9269 instances were collected from Google
Earth with different resolutions. Experiments based on public dataset HRSC2016
and our HRSD dataset demonstrate that our detection method achieves
state-of-the-art performance.