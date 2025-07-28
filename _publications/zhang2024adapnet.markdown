---
layout: publication
title: 'Adapnet: Adaptive Noise-based Network For Low-quality Image Retrieval'
authors: Sihe Zhang, Qingdong He, Jinlong Peng, Yuxi Li, Zhengkai Jiang, Jiafu Wu,
  Mingmin Chi, Yabiao Wang, Chengjie Wang
conference: Arxiv
year: 2024
bibkey: zhang2024adapnet
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.17718'}]
tags: ["Hybrid ANN Methods", "Image Retrieval"]
short_authors: Zhang et al.
---
Image retrieval aims to identify visually similar images within a database
using a given query image. Traditional methods typically employ both global and
local features extracted from images for matching, and may also apply
re-ranking techniques to enhance accuracy. However, these methods often fail to
account for the noise present in query images, which can stem from natural or
human-induced factors, thereby negatively impacting retrieval performance. To
mitigate this issue, we introduce a novel setting for low-quality image
retrieval, and propose an Adaptive Noise-Based Network (AdapNet) to learn
robust abstract representations. Specifically, we devise a quality compensation
block trained to compensate for various low-quality factors in input images.
Besides, we introduce an innovative adaptive noise-based loss function, which
dynamically adjusts its focus on the gradient in accordance with image quality,
thereby augmenting the learning of unknown noisy samples during training and
enhancing intra-class compactness. To assess the performance, we construct two
datasets with low-quality queries, which is built by applying various types of
noise on clean query images on the standard Revisited Oxford and Revisited
Paris datasets. Comprehensive experimental results illustrate that AdapNet
surpasses state-of-the-art methods on the Noise Revisited Oxford and Noise
Revisited Paris benchmarks, while maintaining competitive performance on
high-quality datasets. The code and constructed datasets will be made
available.