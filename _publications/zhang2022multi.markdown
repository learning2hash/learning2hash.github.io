---
layout: publication
title: Multi-level Second-order Few-shot Learning
authors: Hongguang Zhang, Hongdong Li, Piotr Koniusz
conference: IEEE Transactions on Multimedia
year: 2022
bibkey: zhang2022multi
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.05916'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Hongguang Zhang, Hongdong Li, Piotr Koniusz
---
We propose a Multi-level Second-order (MlSo) few-shot learning network for
supervised or unsupervised few-shot image classification and few-shot action
recognition. We leverage so-called power-normalized second-order base learner
streams combined with features that express multiple levels of visual
abstraction, and we use self-supervised discriminating mechanisms. As
Second-order Pooling (SoP) is popular in image recognition, we employ its basic
element-wise variant in our pipeline. The goal of multi-level feature design is
to extract feature representations at different layer-wise levels of CNN,
realizing several levels of visual abstraction to achieve robust few-shot
learning. As SoP can handle convolutional feature maps of varying spatial
sizes, we also introduce image inputs at multiple spatial scales into MlSo. To
exploit the discriminative information from multi-level and multi-scale
features, we develop a Feature Matching (FM) module that reweights their
respective branches. We also introduce a self-supervised step, which is a
discriminator of the spatial level and the scale of abstraction. Our pipeline
is trained in an end-to-end manner. With a simple architecture, we demonstrate
respectable results on standard datasets such as Omniglot, mini-ImageNet,
tiered-ImageNet, Open MIC, fine-grained datasets such as CUB Birds, Stanford
Dogs and Cars, and action recognition datasets such as HMDB51, UCF101, and
mini-MIT.