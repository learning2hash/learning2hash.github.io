---
layout: publication
title: A Discriminatively Learned CNN Embedding For Person Re-identification
authors: Zhedong Zheng, Liang Zheng, Yi Yang
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2017
bibkey: zheng2016a
citations: 495
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1611.05666'}]
tags: ["Evaluation", "Image Retrieval"]
short_authors: Zhedong Zheng, Liang Zheng, Yi Yang
---
We revisit two popular convolutional neural networks (CNN) in person
re-identification (re-ID), i.e, verification and classification models. The two
models have their respective advantages and limitations due to different loss
functions. In this paper, we shed light on how to combine the two models to
learn more discriminative pedestrian descriptors. Specifically, we propose a
new siamese network that simultaneously computes identification loss and
verification loss. Given a pair of training images, the network predicts the
identities of the two images and whether they belong to the same identity. Our
network learns a discriminative embedding and a similarity measurement at the
same time, thus making full usage of the annotations. Albeit simple, the
learned embedding improves the state-of-the-art performance on two public
person re-ID benchmarks. Further, we show our architecture can also be applied
in image retrieval.