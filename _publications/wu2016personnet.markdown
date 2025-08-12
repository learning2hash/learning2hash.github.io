---
layout: publication
title: 'Personnet: Person Re-identification With Deep Convolutional Neural Networks'
authors: Lin Wu, Chunhua Shen, Anton van Den Hengel
conference: Arxiv
year: 2016
bibkey: wu2016personnet
citations: 208
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.07255'}]
tags: []
short_authors: Lin Wu, Chunhua Shen, Anton van Den Hengel
---
In this paper, we propose a deep end-to-end neu- ral network to
simultaneously learn high-level features and a corresponding similarity metric
for person re-identification. The network takes a pair of raw RGB images as
input, and outputs a similarity value indicating whether the two input images
depict the same person. A layer of computing neighborhood range differences
across two input images is employed to capture local relationship between
patches. This operation is to seek a robust feature from input images. By
increasing the depth to 10 weight layers and using very small (3\(\times\)3)
convolution filters, our architecture achieves a remarkable improvement on the
prior-art configurations. Meanwhile, an adaptive Root- Mean-Square (RMSProp)
gradient decent algorithm is integrated into our architecture, which is
beneficial to deep nets. Our method consistently outperforms state-of-the-art
on two large datasets (CUHK03 and Market-1501), and a medium-sized data set
(CUHK01).