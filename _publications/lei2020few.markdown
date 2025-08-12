---
layout: publication
title: Few-shot Semantic Segmentation Augmented With Image-level Weak Annotations
authors: Shuo Lei, Xuchao Zhang, Jianfeng He, Fanglan Chen, Chang-Tien Lu
conference: Arxiv
year: 2020
bibkey: lei2020few
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.01496'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Lei et al.
---
Despite the great progress made by deep neural networks in the semantic
segmentation task, traditional neural-networkbased methods typically suffer
from a shortage of large amounts of pixel-level annotations. Recent progress in
fewshot semantic segmentation tackles the issue by only a few pixel-level
annotated examples. However, these few-shot approaches cannot easily be applied
to multi-way or weak annotation settings. In this paper, we advance the
few-shot segmentation paradigm towards a scenario where image-level annotations
are available to help the training process of a few pixel-level annotations.
Our key idea is to learn a better prototype representation of the class by
fusing the knowledge from the image-level labeled data. Specifically, we
propose a new framework, called PAIA, to learn the class prototype
representation in a metric space by integrating image-level annotations.
Furthermore, by considering the uncertainty of pseudo-masks, a distilled soft
masked average pooling strategy is designed to handle distractions in
image-level annotations. Extensive empirical results on two datasets show
superior performance of PAIA.