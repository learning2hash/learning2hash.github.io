---
layout: publication
title: Matching Feature Sets For Few-shot Image Classification
authors: "Arman Afrasiyabi, Hugo Larochelle, Jean-Fran\xE7ois Lalonde, Christian Gagn\xE9"
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: afrasiyabi2022matching
citations: 89
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.00949'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Afrasiyabi et al.
---
In image classification, it is common practice to train deep networks to
extract a single feature vector per input image. Few-shot classification
methods also mostly follow this trend. In this work, we depart from this
established direction and instead propose to extract sets of feature vectors
for each image. We argue that a set-based representation intrinsically builds a
richer representation of images from the base classes, which can subsequently
better transfer to the few-shot classes. To do so, we propose to adapt existing
feature extractors to instead produce sets of feature vectors from images. Our
approach, dubbed SetFeat, embeds shallow self-attention mechanisms inside
existing encoder architectures. The attention modules are lightweight, and as
such our method results in encoders that have approximately the same number of
parameters as their original versions. During training and inference, a
set-to-set matching metric is used to perform image classification. The
effectiveness of our proposed architecture and metrics is demonstrated via
thorough experiments on standard few-shot datasets -- namely miniImageNet,
tieredImageNet, and CUB -- in both the 1- and 5-shot scenarios. In all cases
but one, our method outperforms the state-of-the-art.