---
layout: publication
title: End-to-end Binary Representation Learning Via Direct Binary Embedding
authors: Liu Liu, Alireza Rahimpour, Ali Taalimi, Hairong Qi
conference: 2017 IEEE International Conference on Image Processing (ICIP)
year: 2017
bibkey: liu2017end
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.04960'}]
tags: [Compact Codes, Image Retrieval, Quantization, Scalability, Hashing Methods]
short_authors: Liu et al.
---
Learning binary representation is essential to large-scale computer vision
tasks. Most existing algorithms require a separate quantization constraint to
learn effective hashing functions. In this work, we present Direct Binary
Embedding (DBE), a simple yet very effective algorithm to learn binary
representation in an end-to-end fashion. By appending an ingeniously designed
DBE layer to the deep convolutional neural network (DCNN), DBE learns binary
code directly from the continuous DBE layer activation without quantization
error. By employing the deep residual network (ResNet) as DCNN component, DBE
captures rich semantics from images. Furthermore, in the effort of handling
multilabel images, we design a joint cross entropy loss that includes both
softmax cross entropy and weighted binary cross entropy in consideration of the
correlation and independence of labels, respectively. Extensive experiments
demonstrate the significant superiority of DBE over state-of-the-art methods on
tasks of natural object recognition, image retrieval and image annotation.