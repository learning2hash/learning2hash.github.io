---
layout: publication
title: Image-based Geolocalization By Ground-to-2.5d Map Matching
authors: Mengjie Zhou, Liu Liu, Yiran Zhong, Andrew Calway
conference: Arxiv
year: 2023
bibkey: zhou2023image
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.05993'}]
tags: []
short_authors: Zhou et al.
---
We study the image-based geolocalization problem, aiming to localize
ground-view query images on cartographic maps. Current methods often utilize
cross-view localization techniques to match ground-view query images with 2D
maps. However, the performance of these methods is unsatisfactory due to
significant cross-view appearance differences. In this paper, we lift
cross-view matching to a 2.5D space, where heights of structures (e.g., trees
and buildings) provide geometric information to guide the cross-view matching.
We propose a new approach to learning representative embeddings from
multi-modal data. Specifically, we establish a projection relationship between
2.5D space and 2D aerial-view space. The projection is further used to combine
multi-modal features from the 2.5D and 2D maps using an effective
pixel-to-point fusion method. By encoding crucial geometric cues, our method
learns discriminative location embeddings for matching panoramic images and
maps. Additionally, we construct the first large-scale ground-to-2.5D map
geolocalization dataset to validate our method and facilitate future research.
Both single-image based and route based localization experiments are conducted
to test our method. Extensive experiments demonstrate that the proposed method
achieves significantly higher localization accuracy and faster convergence than
previous 2D map-based approaches.