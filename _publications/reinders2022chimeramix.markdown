---
layout: publication
title: 'Chimeramix: Image Classification On Small Datasets Via Masked Feature Mixing'
authors: Christoph Reinders, Frederik Schubert, Bodo Rosenhahn
conference: Proceedings of the Thirty-First International Joint Conference on Artificial
  Intelligence
year: 2022
bibkey: reinders2022chimeramix
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.11616'}]
tags: ["Datasets", "Evaluation"]
short_authors: Christoph Reinders, Frederik Schubert, Bodo Rosenhahn
---
Deep convolutional neural networks require large amounts of labeled data
samples. For many real-world applications, this is a major limitation which is
commonly treated by augmentation methods. In this work, we address the problem
of learning deep neural networks on small datasets. Our proposed architecture
called ChimeraMix learns a data augmentation by generating compositions of
instances. The generative model encodes images in pairs, combines the features
guided by a mask, and creates new samples. For evaluation, all methods are
trained from scratch without any additional data. Several experiments on
benchmark datasets, e.g. ciFAIR-10, STL-10, and ciFAIR-100, demonstrate the
superior performance of ChimeraMix compared to current state-of-the-art methods
for classification on small datasets.