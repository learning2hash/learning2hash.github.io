---
layout: publication
title: 'Multi-dataset Pretraining: A Unified Model For Semantic Segmentation'
authors: Bowen Shi, Xiaopeng Zhang, Haohang Xu, Wenrui Dai, Junni Zou, Hongkai Xiong,
  Qi Tian
conference: Arxiv
year: 2021
bibkey: shi2021multi
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.04121'}]
tags: ["Datasets"]
short_authors: Shi et al.
---
Collecting annotated data for semantic segmentation is time-consuming and
hard to scale up. In this paper, we for the first time propose a unified
framework, termed as Multi-Dataset Pretraining, to take full advantage of the
fragmented annotations of different datasets. The highlight is that the
annotations from different domains can be efficiently reused and consistently
boost performance for each specific domain. This is achieved by first
pretraining the network via the proposed pixel-to-prototype contrastive loss
over multiple datasets regardless of their taxonomy labels, and followed by
fine-tuning the pretrained model over specific dataset as usual. In order to
better model the relationship among images and classes from different datasets,
we extend the pixel level embeddings via cross dataset mixing and propose a
pixel-to-class sparse coding strategy that explicitly models the pixel-class
similarity over the manifold embedding space. In this way, we are able to
increase intra-class compactness and inter-class separability, as well as
considering inter-class similarity across different datasets for better
transferability. Experiments conducted on several benchmarks demonstrate its
superior performance. Notably, MDP consistently outperforms the pretrained
models over ImageNet by a considerable margin, while only using less than 10%
samples for pretraining.