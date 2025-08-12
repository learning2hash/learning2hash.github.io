---
layout: publication
title: Learning Granularity-aware Convolutional Neural Network For Fine-grained Visual
  Classification
authors: Jianwei Song, Ruoyu Yang
conference: Arxiv
year: 2021
bibkey: song2021learning
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.02788'}]
tags: []
short_authors: Jianwei Song, Ruoyu Yang
---
Locating discriminative parts plays a key role in fine-grained visual
classification due to the high similarities between different objects. Recent
works based on convolutional neural networks utilize the feature maps taken
from the last convolutional layer to mine discriminative regions. However, the
last convolutional layer tends to focus on the whole object due to the large
receptive field, which leads to a reduced ability to spot the differences. To
address this issue, we propose a novel Granularity-Aware Convolutional Neural
Network (GA-CNN) that progressively explores discriminative features.
Specifically, GA-CNN utilizes the differences of the receptive fields at
different layers to learn multi-granularity features, and it exploits larger
granularity information based on the smaller granularity information found at
the previous stages. To further boost the performance, we introduce an
object-attentive module that can effectively localize the object given a raw
image. GA-CNN does not need bounding boxes/part annotations and can be trained
end-to-end. Extensive experimental results show that our approach achieves
state-of-the-art performances on three benchmark datasets.