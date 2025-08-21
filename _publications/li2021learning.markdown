---
layout: publication
title: Learning Semantic-aligned Feature Representation For Text-based Person Search
authors: Shiping Li, Min Cao, Min Zhang
conference: ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech
  and Signal Processing (ICASSP)
year: 2022
bibkey: li2021learning
citations: 47
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.06714'}]
tags: ["Datasets", "ICASSP"]
short_authors: Shiping Li, Min Cao, Min Zhang
---
Text-based person search aims to retrieve images of a certain pedestrian by a
textual description. The key challenge of this task is to eliminate the
inter-modality gap and achieve the feature alignment across modalities. In this
paper, we propose a semantic-aligned embedding method for text-based person
search, in which the feature alignment across modalities is achieved by
automatically learning the semantic-aligned visual features and textual
features. First, we introduce two Transformer-based backbones to encode robust
feature representations of the images and texts. Second, we design a
semantic-aligned feature aggregation network to adaptively select and aggregate
features with the same semantics into part-aware features, which is achieved by
a multi-head attention module constrained by a cross-modality part alignment
loss and a diversity loss. Experimental results on the CUHK-PEDES and Flickr30K
datasets show that our method achieves state-of-the-art performances.