---
layout: publication
title: Exploring The Limits Of Deep Image Clustering Using Pretrained Models
authors: Nikolas Adaloglou, Felix Michels, Hamza Kalisch, Markus Kollmann
conference: Arxiv
year: 2023
bibkey: adaloglou2023exploring
citations: 1
additional_links: [{name: Code, url: 'https://github.com/HHU-MMBS/TEMI-official-BMVC2023.'},
  {name: Paper, url: 'https://arxiv.org/abs/2303.17896'}]
tags: ["Self-Supervised"]
short_authors: Adaloglou et al.
---
We present a general methodology that learns to classify images without
labels by leveraging pretrained feature extractors. Our approach involves
self-distillation training of clustering heads based on the fact that nearest
neighbours in the pretrained feature space are likely to share the same label.
We propose a novel objective that learns associations between image features by
introducing a variant of pointwise mutual information together with instance
weighting. We demonstrate that the proposed objective is able to attenuate the
effect of false positive pairs while efficiently exploiting the structure in
the pretrained feature space. As a result, we improve the clustering accuracy
over \(k\)-means on \(17\) different pretrained models by \(6.1\)% and \(12.2\)% on
ImageNet and CIFAR100, respectively. Finally, using self-supervised vision
transformers, we achieve a clustering accuracy of \(61.6\)% on ImageNet. The
code is available at https://github.com/HHU-MMBS/TEMI-official-BMVC2023.