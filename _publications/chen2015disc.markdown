---
layout: publication
title: 'DISC: Deep Image Saliency Computing Via Progressive Representation Learning'
authors: Tianshui Chen, Liang Lin, Lingbo Liu, Xiaonan Luo, Xuelong Li
conference: IEEE Transactions on Neural Networks and Learning Systems
year: 2016
bibkey: chen2015disc
citations: 160
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.04192'}]
tags: []
short_authors: Chen et al.
---
Salient object detection increasingly receives attention as an important
component or step in several pattern recognition and image processing tasks.
Although a variety of powerful saliency models have been intensively proposed,
they usually involve heavy feature (or model) engineering based on priors (or
assumptions) about the properties of objects and backgrounds. Inspired by the
effectiveness of recently developed feature learning, we provide a novel Deep
Image Saliency Computing (DISC) framework for fine-grained image saliency
computing. In particular, we model the image saliency from both the coarse- and
fine-level observations, and utilize the deep convolutional neural network
(CNN) to learn the saliency representation in a progressive manner.
Specifically, our saliency model is built upon two stacked CNNs. The first CNN
generates a coarse-level saliency map by taking the overall image as the input,
roughly identifying saliency regions in the global context. Furthermore, we
integrate superpixel-based local context information in the first CNN to refine
the coarse-level saliency map. Guided by the coarse saliency map, the second
CNN focuses on the local context to produce fine-grained and accurate saliency
map while preserving object details. For a testing image, the two CNNs
collaboratively conduct the saliency computing in one shot. Our DISC framework
is capable of uniformly highlighting the objects-of-interest from complex
background while preserving well object details. Extensive experiments on
several standard benchmarks suggest that DISC outperforms other
state-of-the-art methods and it also generalizes well across datasets without
additional training. The executable version of DISC is available online:
http://vision.sysu.edu.cn/projects/DISC.