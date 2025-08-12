---
layout: publication
title: 'Isaid: A Large-scale Dataset For Instance Segmentation In Aerial Images'
authors: Syed Waqas Zamir, Aditya Arora, Akshita Gupta, Salman Khan, Guolei Sun, Fahad
  Shahbaz Khan, Fan Zhu, Ling Shao, Gui-Song Xia, Xiang Bai
conference: Arxiv
year: 2019
bibkey: zamir2019isaid
citations: 99
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.12886'}]
tags: ["Datasets"]
short_authors: Zamir et al.
---
Existing Earth Vision datasets are either suitable for semantic segmentation
or object detection. In this work, we introduce the first benchmark dataset for
instance segmentation in aerial imagery that combines instance-level object
detection and pixel-level segmentation tasks. In comparison to instance
segmentation in natural scenes, aerial images present unique challenges e.g., a
huge number of instances per image, large object-scale variations and abundant
tiny objects. Our large-scale and densely annotated Instance Segmentation in
Aerial Images Dataset (iSAID) comes with 655,451 object instances for 15
categories across 2,806 high-resolution images. Such precise per-pixel
annotations for each instance ensure accurate localization that is essential
for detailed scene analysis. Compared to existing small-scale aerial image
based instance segmentation datasets, iSAID contains 15\(\times\) the number of
object categories and 5\(\times\) the number of instances. We benchmark our
dataset using two popular instance segmentation approaches for natural images,
namely Mask R-CNN and PANet. In our experiments we show that direct application
of off-the-shelf Mask R-CNN and PANet on aerial images provide suboptimal
instance segmentation results, thus requiring specialized solutions from the
research community. The dataset is publicly available at:
https://captain-whu.github.io/iSAID/index.html