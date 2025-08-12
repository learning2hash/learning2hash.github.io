---
layout: publication
title: Semantic Segmentation With Scarce Data
authors: Isay Katsman, Rohun Tripathi, Andreas Veit, Serge Belongie
conference: Arxiv
year: 2018
bibkey: katsman2018semantic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1807.00911'}]
tags: ["Datasets"]
short_authors: Katsman et al.
---
Semantic segmentation is a challenging vision problem that usually
necessitates the collection of large amounts of finely annotated data, which is
often quite expensive to obtain. Coarsely annotated data provides an
interesting alternative as it is usually substantially more cheap. In this
work, we present a method to leverage coarsely annotated data along with fine
supervision to produce better segmentation results than would be obtained when
training using only the fine data. We validate our approach by simulating a
scarce data setting with less than 200 low resolution images from the
Cityscapes dataset and show that our method substantially outperforms solely
training on the fine annotation data by an average of 15.52% mIoU and
outperforms the coarse mask by an average of 5.28% mIoU.