---
layout: publication
title: Dag-recurrent Neural Networks For Scene Labeling
authors: Bing Shuai, Zhen Zuo, Gang Wang, Bing Wang
conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2016
bibkey: shuai2015dag
citations: 148
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1509.00552'}]
tags: ["CVPR"]
short_authors: Shuai et al.
---
In image labeling, local representations for image units are usually
generated from their surrounding image patches, thus long-range contextual
information is not effectively encoded. In this paper, we introduce recurrent
neural networks (RNNs) to address this issue. Specifically, directed acyclic
graph RNNs (DAG-RNNs) are proposed to process DAG-structured images, which
enables the network to model long-range semantic dependencies among image
units. Our DAG-RNNs are capable of tremendously enhancing the discriminative
power of local representations, which significantly benefits the local
classification. Meanwhile, we propose a novel class weighting function that
attends to rare classes, which phenomenally boosts the recognition accuracy for
non-frequent classes. Integrating with convolution and deconvolution layers,
our DAG-RNNs achieve new state-of-the-art results on the challenging SiftFlow,
CamVid and Barcelona benchmarks.