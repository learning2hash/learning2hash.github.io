---
layout: publication
title: 'Torchreid: A Library For Deep Learning Person Re-identification In Pytorch'
authors: Kaiyang Zhou, Tao Xiang
conference: Arxiv
year: 2019
bibkey: zhou2019torchreid
citations: 105
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.10093'}]
tags: ["Tools & Libraries"]
short_authors: Kaiyang Zhou, Tao Xiang
---
Person re-identification (re-ID), which aims to re-identify people across
different camera views, has been significantly advanced by deep learning in
recent years, particularly with convolutional neural networks (CNNs). In this
paper, we present Torchreid, a software library built on PyTorch that allows
fast development and end-to-end training and evaluation of deep re-ID models.
As a general-purpose framework for person re-ID research, Torchreid provides
(1) unified data loaders that support 15 commonly used re-ID benchmark datasets
covering both image and video domains, (2) streamlined pipelines for quick
development and benchmarking of deep re-ID models, and (3) implementations of
the latest re-ID CNN architectures along with their pre-trained models to
facilitate reproducibility as well as future research. With a high-level
modularity in its design, Torchreid offers a great flexibility to allow easy
extension to new datasets, CNN models and loss functions.