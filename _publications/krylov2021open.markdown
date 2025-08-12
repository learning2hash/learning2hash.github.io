---
layout: publication
title: Open Images V5 Text Annotation And Yet Another Mask Text Spotter
authors: Ilya Krylov, Sergei Nosov, Vladislav Sovrasov
conference: Arxiv
year: 2021
bibkey: krylov2021open
citations: 8
additional_links: [{name: Code, url: 'https://github.com/openvinotoolkit/training_extensions'},
  {name: Paper, url: 'https://arxiv.org/abs/2106.12326'}]
tags: ["Datasets"]
short_authors: Ilya Krylov, Sergei Nosov, Vladislav Sovrasov
---
A large scale human-labeled dataset plays an important role in creating high
quality deep learning models. In this paper we present text annotation for Open
Images V5 dataset. To our knowledge it is the largest among publicly available
manually created text annotations. Having this annotation we trained a simple
Mask-RCNN-based network, referred as Yet Another Mask Text Spotter (YAMTS),
which achieves competitive performance or even outperforms current
state-of-the-art approaches in some cases on ICDAR2013, ICDAR2015 and
Total-Text datasets. Code for text spotting model available online at:
https://github.com/openvinotoolkit/training_extensions. The model can be
exported to OpenVINO-format and run on Intel CPUs.