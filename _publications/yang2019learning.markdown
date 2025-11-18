---
layout: publication
title: Learning Shared Semantic Space With Correlation Alignment For Cross-modal Event
  Retrieval
authors: Zhenguo Yang, Zehang Lin, Peipei Kang, Jianming Lv, Qing Li, Wenyin Liu
conference: ACM Transactions on Multimedia Computing, Communications, and Applications
year: 2019
bibkey: yang2019learning
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.04268'}]
tags: ["Datasets"]
short_authors: Yang et al.
---
In this paper, we propose to learn shared semantic space with correlation
alignment (\(\{S\}^\{3\}CA\)) for multimodal data representations, which aligns
nonlinear correlations of multimodal data distributions in deep neural networks
designed for heterogeneous data. In the context of cross-modal (event)
retrieval, we design a neural network with convolutional layers and
fully-connected layers to extract features for images, including images on
Flickr-like social media. Simultaneously, we exploit a fully-connected neural
network to extract semantic features for texts, including news articles from
news media. In particular, nonlinear correlations of layer activations in the
two neural networks are aligned with correlation alignment during the joint
training of the networks. Furthermore, we project the multimodal data into a
shared semantic space for cross-modal (event) retrieval, where the distances
between heterogeneous data samples can be measured directly. In addition, we
contribute a Wiki-Flickr Event dataset, where the multimodal data samples are
not describing each other in pairs like the existing paired datasets, but all
of them are describing semantic events. Extensive experiments conducted on both
paired and unpaired datasets manifest the effectiveness of \(\{S\}^\{3\}CA\),
outperforming the state-of-the-art methods.