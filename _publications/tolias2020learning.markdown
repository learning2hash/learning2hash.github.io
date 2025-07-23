---
layout: publication
title: Learning And Aggregating Deep Local Descriptors For Instance-level Recognition
authors: "Tolias Giorgos, Jenicek Tomas, Chum Ond\u0159ej"
conference: Lecture Notes in Computer Science
year: 2020
bibkey: tolias2020learning
citations: 82
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.13172'}]
tags: ["Distance Metric Learning", "Image Retrieval", "Similarity Search"]
short_authors: "Tolias Giorgos, Jenicek Tomas, Chum Ond\u0159ej"
---
We propose an efficient method to learn deep local descriptors for
instance-level recognition. The training only requires examples of positive and
negative image pairs and is performed as metric learning of sum-pooled global
image descriptors. At inference, the local descriptors are provided by the
activations of internal components of the network. We demonstrate why such an
approach learns local descriptors that work well for image similarity
estimation with classical efficient match kernel methods. The experimental
validation studies the trade-off between performance and memory requirements of
the state-of-the-art image search approach based on match kernels. Compared to
existing local descriptors, the proposed ones perform better in two
instance-level recognition tasks and keep memory requirements lower. We
experimentally show that global descriptors are not effective enough at large
scale and that local descriptors are essential. We achieve state-of-the-art
performance, in some cases even with a backbone network as small as ResNet18.