---
layout: publication
title: Multiple-environment Self-adaptive Network For Aerial-view Geo-localization
authors: Tingyu Wang, Zhedong Zheng, Yaoqi Sun, Chenggang Yan, Yi Yang, Tat-Seng Chua
conference: Arxiv
year: 2022
bibkey: wang2022multiple
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.08381'}]
tags: [Evaluation, Image Retrieval]
short_authors: Wang et al.
---
Aerial-view geo-localization tends to determine an unknown position through
matching the drone-view image with the geo-tagged satellite-view image. This
task is mostly regarded as an image retrieval problem. The key underpinning
this task is to design a series of deep neural networks to learn discriminative
image descriptors. However, existing methods meet large performance drops under
realistic weather, such as rain and fog, since they do not take the domain
shift between the training data and multiple test environments into
consideration. To minor this domain gap, we propose a Multiple-environment
Self-adaptive Network (MuSe-Net) to dynamically adjust the domain shift caused
by environmental changing. In particular, MuSe-Net employs a two-branch neural
network containing one multiple-environment style extraction network and one
self-adaptive feature extraction network. As the name implies, the
multiple-environment style extraction network is to extract the
environment-related style information, while the self-adaptive feature
extraction network utilizes an adaptive modulation module to dynamically
minimize the environment-related style gap. Extensive experiments on two
widely-used benchmarks, i.e., University-1652 and CVUSA, demonstrate that the
proposed MuSe-Net achieves a competitive result for geo-localization in
multiple environments. Furthermore, we observe that the proposed method also
shows great potential to the unseen extreme weather, such as mixing the fog,
rain and snow.