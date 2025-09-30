---
layout: publication
title: Hierarchical Attention Fusion For Geo-localization
authors: Liqi Yan, Yiming Cui, Yingjie Chen, Dongfang Liu
conference: ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2021
bibkey: yan2021hierarchical
citations: 32
additional_links: [{name: Code, url: 'https://github.com/YanLiqi/HAF'}, {name: Paper,
    url: 'https://arxiv.org/abs/2102.09186'}]
tags: ["Evaluation", "ICASSP", "Image Retrieval", "Scalability", "Self-Supervised", "Supervised"]
short_authors: Yan et al.
---
Geo-localization is a critical task in computer vision. In this work, we cast
the geo-localization as a 2D image retrieval task. Current state-of-the-art
methods for 2D geo-localization are not robust to locate a scene with drastic
scale variations because they only exploit features from one semantic level for
image representations. To address this limitation, we introduce a hierarchical
attention fusion network using multi-scale features for geo-localization. We
extract the hierarchical feature maps from a convolutional neural network (CNN)
and organically fuse the extracted features for image representations. Our
training is self-supervised using adaptive weights to control the attention of
feature emphasis from each hierarchical level. Evaluation results on the image
retrieval and the large-scale geo-localization benchmarks indicate that our
method outperforms the existing state-of-the-art methods. Code is available
here: https://github.com/YanLiqi/HAF.