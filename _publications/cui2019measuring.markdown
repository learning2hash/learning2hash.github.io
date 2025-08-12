---
layout: publication
title: Measuring Dataset Granularity
authors: Yin Cui, Zeqi Gu, Dhruv Mahajan, Laurens van Der Maaten, Serge Belongie,
  Ser-Nam Lim
conference: Arxiv
year: 2019
bibkey: cui2019measuring
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1912.10154'}]
tags: ["Datasets"]
short_authors: Cui et al.
---
Despite the increasing visibility of fine-grained recognition in our field,
"fine-grained'' has thus far lacked a precise definition. In this work,
building upon clustering theory, we pursue a framework for measuring dataset
granularity. We argue that dataset granularity should depend not only on the
data samples and their labels, but also on the distance function we choose. We
propose an axiomatic framework to capture desired properties for a dataset
granularity measure and provide examples of measures that satisfy these
properties. We assess each measure via experiments on datasets with
hierarchical labels of varying granularity. When measuring granularity in
commonly used datasets with our measure, we find that certain datasets that are
widely considered fine-grained in fact contain subsets of considerable size
that are substantially more coarse-grained than datasets generally regarded as
coarse-grained. We also investigate the interplay between dataset granularity
with a variety of factors and find that fine-grained datasets are more
difficult to learn from, more difficult to transfer to, more difficult to
perform few-shot learning with, and more vulnerable to adversarial attacks.