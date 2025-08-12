---
layout: publication
title: Intra-task Mutual Attention Based Vision Transformer For Few-shot Learning
authors: Weihao Jiang, Chang Liu, Kun He
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2025
bibkey: jiang2024intra
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.03109'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Weihao Jiang, Chang Liu, Kun He
---
Humans possess remarkable ability to accurately classify new, unseen images
after being exposed to only a few examples. Such ability stems from their
capacity to identify common features shared between new and previously seen
images while disregarding distractions such as background variations. However,
for artificial neural network models, determining the most relevant features
for distinguishing between two images with limited samples presents a
challenge. In this paper, we propose an intra-task mutual attention method for
few-shot learning, that involves splitting the support and query samples into
patches and encoding them using the pre-trained Vision Transformer (ViT)
architecture. Specifically, we swap the class (CLS) token and patch tokens
between the support and query sets to have the mutual attention, which enables
each set to focus on the most useful information. This facilitates the
strengthening of intra-class representations and promotes closer proximity
between instances of the same class. For implementation, we adopt the ViT-based
network architecture and utilize pre-trained model parameters obtained through
self-supervision. By leveraging Masked Image Modeling as a self-supervised
training task for pre-training, the pre-trained model yields semantically
meaningful representations while successfully avoiding supervision collapse. We
then employ a meta-learning method to fine-tune the last several layers and CLS
token modules. Our strategy significantly reduces the num- ber of parameters
that require fine-tuning while effectively uti- lizing the capability of
pre-trained model. Extensive experiments show that our framework is simple,
effective and computationally efficient, achieving superior performance as
compared to the state-of-the-art baselines on five popular few-shot
classification benchmarks under the 5-shot and 1-shot scenarios