---
layout: publication
title: Visual Descriptors For Content-based Retrieval Of Remote Sensing Images
authors: Paolo Napoletano
conference: International Journal of Remote Sensing
year: 2016
bibkey: napoletano2016visual
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1602.00970'}]
tags: ["Datasets", "Evaluation", "Image Retrieval"]
short_authors: Paolo Napoletano
---
In this paper we present an extensive evaluation of visual descriptors for
the content-based retrieval of remote sensing (RS) images. The evaluation
includes global hand-crafted, local hand-crafted, and Convolutional Neural
Network (CNNs) features coupled with four different Content-Based Image
Retrieval schemes. We conducted all the experiments on two publicly available
datasets: the 21-class UC Merced Land Use/Land Cover (LandUse) dataset and
19-class High-resolution Satellite Scene dataset (SceneSat). The content of RS
images might be quite heterogeneous, ranging from images containing fine
grained textures, to coarse grained ones or to images containing objects. It is
therefore not obvious in this domain, which descriptor should be employed to
describe images having such a variability. Results demonstrate that CNN-based
features perform better than both global and and local hand-crafted features
whatever is the retrieval scheme adopted. Features extracted from SatResNet-50,
a residual CNN suitable fine-tuned on the RS domain, shows much better
performance than a residual CNN pre-trained on multimedia scene and object
images. Features extracted from NetVLAD, a CNN that considers both CNN and
local features, works better than others CNN solutions on those images that
contain fine-grained textures and objects.