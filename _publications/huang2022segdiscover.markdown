---
layout: publication
title: 'Segdiscover: Visual Concept Discovery Via Unsupervised Semantic Segmentation'
authors: Haiyang Huang, Zhi Chen, Cynthia Rudin
conference: Arxiv
year: 2022
bibkey: huang2022segdiscover
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.10926'}]
tags: ["Unsupervised"]
short_authors: Haiyang Huang, Zhi Chen, Cynthia Rudin
---
Visual concept discovery has long been deemed important to improve
interpretability of neural networks, because a bank of semantically meaningful
concepts would provide us with a starting point for building machine learning
models that exhibit intelligible reasoning process. Previous methods have
disadvantages: either they rely on labelled support sets that incorporate human
biases for objects that are "useful," or they fail to identify multiple
concepts that occur within a single image. We reframe the concept discovery
task as an unsupervised semantic segmentation problem, and present SegDiscover,
a novel framework that discovers semantically meaningful visual concepts from
imagery datasets with complex scenes without supervision. Our method contains
three important pieces: generating concept primitives from raw images,
discovering concepts by clustering in the latent space of a self-supervised
pretrained encoder, and concept refinement via neural network smoothing.
Experimental results provide evidence that our method can discover multiple
concepts within a single image and outperforms state-of-the-art unsupervised
methods on complex datasets such as Cityscapes and COCO-Stuff. Our method can
be further used as a neural network explanation tool by comparing results
obtained by different encoders.