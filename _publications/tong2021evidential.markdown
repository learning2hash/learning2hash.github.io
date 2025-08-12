---
layout: publication
title: Evidential Fully Convolutional Network For Semantic Segmentation
authors: "Zheng Tong, Philippe Xu, Thierry Den\u0153ux"
conference: Applied Intelligence
year: 2021
bibkey: tong2021evidential
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.13544'}]
tags: []
short_authors: "Zheng Tong, Philippe Xu, Thierry Den\u0153ux"
---
We propose a hybrid architecture composed of a fully convolutional network
(FCN) and a Dempster-Shafer layer for image semantic segmentation. In the
so-called evidential FCN (E-FCN), an encoder-decoder architecture first
extracts pixel-wise feature maps from an input image. A Dempster-Shafer layer
then computes mass functions at each pixel location based on distances to
prototypes. Finally, a utility layer performs semantic segmentation from mass
functions and allows for imprecise classification of ambiguous pixels and
outliers. We propose an end-to-end learning strategy for jointly updating the
network parameters, which can make use of soft (imprecise) labels. Experiments
using three databases (Pascal VOC 2011, MIT-scene Parsing and SIFT Flow) show
that the proposed combination improves the accuracy and calibration of semantic
segmentation by assigning confusing pixels to multi-class sets.