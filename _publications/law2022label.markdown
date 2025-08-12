---
layout: publication
title: Label-free Synthetic Pretraining Of Object Detectors
authors: Hei Law, Jia Deng
conference: Arxiv
year: 2022
bibkey: law2022label
citations: 1
additional_links: [{name: Code, url: 'https://github.com/princeton-vl/SOLID'}, {name: Paper,
    url: 'https://arxiv.org/abs/2208.04268'}]
tags: []
short_authors: Hei Law, Jia Deng
---
We propose a new approach, Synthetic Optimized Layout with Instance Detection
(SOLID), to pretrain object detectors with synthetic images. Our "SOLID"
approach consists of two main components: (1) generating synthetic images using
a collection of unlabelled 3D models with optimized scene arrangement; (2)
pretraining an object detector on "instance detection" task - given a query
image depicting an object, detecting all instances of the exact same object in
a target image. Our approach does not need any semantic labels for pretraining
and allows the use of arbitrary, diverse 3D models. Experiments on COCO show
that with optimized data generation and a proper pretraining task, synthetic
data can be highly effective data for pretraining object detectors. In
particular, pretraining on rendered images achieves performance competitive
with pretraining on real images while using significantly less computing
resources. Code is available at https://github.com/princeton-vl/SOLID.