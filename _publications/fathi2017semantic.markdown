---
layout: publication
title: Semantic Instance Segmentation Via Deep Metric Learning
authors: Alireza Fathi, Zbigniew Wojna, Vivek Rathod, Peng Wang, Hyun Oh Song, Sergio
  Guadarrama, Kevin P. Murphy
conference: Arxiv
year: 2017
bibkey: fathi2017semantic
citations: 231
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.10277'}]
tags: ["Distance Metric Learning"]
short_authors: Fathi et al.
---
We propose a new method for semantic instance segmentation, by first
computing how likely two pixels are to belong to the same object, and then by
grouping similar pixels together. Our similarity metric is based on a deep,
fully convolutional embedding model. Our grouping method is based on selecting
all points that are sufficiently similar to a set of "seed points", chosen from
a deep, fully convolutional scoring model. We show competitive results on the
Pascal VOC instance segmentation benchmark.