---
layout: publication
title: Localizing Visual Sounds The Hard Way
authors: Honglie Chen, Weidi Xie, Triantafyllos Afouras, Arsha Nagrani, Andrea Vedaldi,
  Andrew Zisserman
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: chen2021localizing
citations: 134
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.02691'}]
tags: ["CVPR"]
short_authors: Chen et al.
---
The objective of this work is to localize sound sources that are visible in a
video without using manual annotations. Our key technical contribution is to
show that, by training the network to explicitly discriminate challenging image
fragments, even for images that do contain the object emitting the sound, we
can significantly boost the localization performance. We do so elegantly by
introducing a mechanism to mine hard samples and add them to a contrastive
learning formulation automatically. We show that our algorithm achieves
state-of-the-art performance on the popular Flickr SoundNet dataset.
Furthermore, we introduce the VGG-Sound Source (VGG-SS) benchmark, a new set of
annotations for the recently-introduced VGG-Sound dataset, where the sound
sources visible in each video clip are explicitly marked with bounding box
annotations. This dataset is 20 times larger than analogous existing ones,
contains 5K videos spanning over 200 categories, and, differently from Flickr
SoundNet, is video-based. On VGG-SS, we also show that our algorithm achieves
state-of-the-art performance against several baselines.