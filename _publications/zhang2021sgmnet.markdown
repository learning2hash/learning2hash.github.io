---
layout: publication
title: 'Sgmnet: Scene Graph Matching Network For Few-shot Remote Sensing Scene Classification'
authors: Baoquan Zhang, Shanshan Feng, Xutao Li, Yunming Ye, Rui Ye
conference: IEEE Transactions on Geoscience and Remote Sensing
year: 2022
bibkey: zhang2021sgmnet
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.04494'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Zhang et al.
---
Few-Shot Remote Sensing Scene Classification (FSRSSC) is an important task,
which aims to recognize novel scene classes with few examples. Recently,
several studies attempt to address the FSRSSC problem by following few-shot
natural image classification methods. These existing methods have made
promising progress and achieved superior performance. However, they all
overlook two unique characteristics of remote sensing images: (i) object
co-occurrence that multiple objects tend to appear together in a scene image
and (ii) object spatial correlation that these co-occurrence objects are
distributed in the scene image following some spatial structure patterns. Such
unique characteristics are very beneficial for FSRSSC, which can effectively
alleviate the scarcity issue of labeled remote sensing images since they can
provide more refined descriptions for each scene class. To fully exploit these
characteristics, we propose a novel scene graph matching-based meta-learning
framework for FSRSSC, called SGMNet. In this framework, a scene graph
construction module is carefully designed to represent each test remote sensing
image or each scene class as a scene graph, where the nodes reflect these
co-occurrence objects meanwhile the edges capture the spatial correlations
between these co-occurrence objects. Then, a scene graph matching module is
further developed to evaluate the similarity score between each test remote
sensing image and each scene class. Finally, based on the similarity scores, we
perform the scene class prediction via a nearest neighbor classifier. We
conduct extensive experiments on UCMerced LandUse, WHU19, AID, and
NWPU-RESISC45 datasets. The experimental results show that our method obtains
superior performance over the previous state-of-the-art methods.