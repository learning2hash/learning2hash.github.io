---
layout: publication
title: "End-to-end Binary Representation Learning via Direct Binary Embedding"
authors: Liu Liu, Rahimpour Alireza, Taalimi Ali, Qi Hairong
conference: Arxiv
year: 2017
bibkey: liu2017end
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1703.04960"}
tags: ['ARXIV', 'CNN', 'Image Retrieval', 'Quantisation']
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
