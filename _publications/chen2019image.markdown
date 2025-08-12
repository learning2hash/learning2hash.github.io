---
layout: publication
title: Image Deformation Meta-networks For One-shot Learning
authors: Zitian Chen, Yanwei Fu, Yu-Xiong Wang, Lin Ma, Wei Liu, Martial Hebert
conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2019
bibkey: chen2019image
citations: 231
additional_links: [{name: Code, url: 'https://github.com/tankche1/IDeMe-Net'}, {name: Paper,
    url: 'https://arxiv.org/abs/1905.11641'}]
tags: ["CVPR"]
short_authors: Chen et al.
---
Humans can robustly learn novel visual concepts even when images undergo
various deformations and lose certain information. Mimicking the same behavior
and synthesizing deformed instances of new concepts may help visual recognition
systems perform better one-shot learning, i.e., learning concepts from one or
few examples. Our key insight is that, while the deformed images may not be
visually realistic, they still maintain critical semantic information and
contribute significantly to formulating classifier decision boundaries.
Inspired by the recent progress of meta-learning, we combine a meta-learner
with an image deformation sub-network that produces additional training
examples, and optimize both models in an end-to-end manner. The deformation
sub-network learns to deform images by fusing a pair of images --- a probe
image that keeps the visual content and a gallery image that diversifies the
deformations. We demonstrate results on the widely used one-shot learning
benchmarks (miniImageNet and ImageNet 1K Challenge datasets), which
significantly outperform state-of-the-art approaches. Code is available at
https://github.com/tankche1/IDeMe-Net.