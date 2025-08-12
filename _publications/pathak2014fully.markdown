---
layout: publication
title: Fully Convolutional Multi-class Multiple Instance Learning
authors: Deepak Pathak, Evan Shelhamer, Jonathan Long, Trevor Darrell
conference: Arxiv
year: 2014
bibkey: pathak2014fully
citations: 281
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1412.7144'}]
tags: []
short_authors: Pathak et al.
---
Multiple instance learning (MIL) can reduce the need for costly annotation in
tasks such as semantic segmentation by weakening the required degree of
supervision. We propose a novel MIL formulation of multi-class semantic
segmentation learning by a fully convolutional network. In this setting, we
seek to learn a semantic segmentation model from just weak image-level labels.
The model is trained end-to-end to jointly optimize the representation while
disambiguating the pixel-image label assignment. Fully convolutional training
accepts inputs of any size, does not need object proposal pre-processing, and
offers a pixelwise loss map for selecting latent instances. Our multi-class MIL
loss exploits the further supervision given by images with multiple labels. We
evaluate this approach through preliminary experiments on the PASCAL VOC
segmentation challenge.