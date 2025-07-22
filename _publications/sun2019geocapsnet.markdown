---
layout: publication
title: 'Geocapsnet: Aerial To Ground View Image Geo-localization Using Capsule Network'
authors: Sun Bin, Chen Chen, Zhu Yingying, Jiang Jianmin
conference: Arxiv
year: 2019
bibkey: sun2019geocapsnet
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.06281'}]
tags: ["Evaluation", "Distance-Metric-Learning", "Image-Retrieval", "Datasets"]
short_authors: Sun et al.
---
The task of cross-view image geo-localization aims to determine the
geo-location (GPS coordinates) of a query ground-view image by matching it with
the GPS-tagged aerial (satellite) images in a reference dataset. Due to the
dramatic changes of viewpoint, matching the cross-view images is challenging.
In this paper, we propose the GeoCapsNet based on the capsule network for
ground-to-aerial image geo-localization. The network first extracts features
from both ground-view and aerial images via standard convolution layers and the
capsule layers further encode the features to model the spatial feature
hierarchies and enhance the representation power. Moreover, we introduce a
simple and effective weighted soft-margin triplet loss with online batch hard
sample mining, which can greatly improve image retrieval accuracy. Experimental
results show that our GeoCapsNet significantly outperforms the state-of-the-art
approaches on two benchmark datasets.