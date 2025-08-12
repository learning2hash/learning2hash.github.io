---
layout: publication
title: The Inaturalist Species Classification And Detection Dataset
authors: Grant van Horn, Oisin Mac Aodha, Yang Song, Yin Cui, Chen Sun, Alex Shepard,
  Hartwig Adam, Pietro Perona, Serge Belongie
conference: 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition
year: 2018
bibkey: vanhorn2017inaturalist
citations: 1125
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.06642'}]
tags: ["CVPR", "Datasets"]
short_authors: Horn et al.
---
Existing image classification datasets used in computer vision tend to have a
uniform distribution of images across object categories. In contrast, the
natural world is heavily imbalanced, as some species are more abundant and
easier to photograph than others. To encourage further progress in challenging
real world conditions we present the iNaturalist species classification and
detection dataset, consisting of 859,000 images from over 5,000 different
species of plants and animals. It features visually similar species, captured
in a wide variety of situations, from all over the world. Images were collected
with different camera types, have varying image quality, feature a large class
imbalance, and have been verified by multiple citizen scientists. We discuss
the collection of the dataset and present extensive baseline experiments using
state-of-the-art computer vision classification and detection models. Results
show that current non-ensemble based methods achieve only 67% top one
classification accuracy, illustrating the difficulty of the dataset.
Specifically, we observe poor results for classes with small numbers of
training examples suggesting more attention is needed in low-shot learning.