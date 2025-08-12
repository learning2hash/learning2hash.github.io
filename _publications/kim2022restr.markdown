---
layout: publication
title: 'Restr: Convolution-free Referring Image Segmentation Using Transformers'
authors: Namyup Kim, Dongwon Kim, Cuiling Lan, Wenjun Zeng, Suha Kwak
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: kim2022restr
citations: 104
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.16768'}]
tags: ["CVPR"]
short_authors: Kim et al.
---
Referring image segmentation is an advanced semantic segmentation task where
target is not a predefined class but is described in natural language. Most of
existing methods for this task rely heavily on convolutional neural networks,
which however have trouble capturing long-range dependencies between entities
in the language expression and are not flexible enough for modeling
interactions between the two different modalities. To address these issues, we
present the first convolution-free model for referring image segmentation using
transformers, dubbed ReSTR. Since it extracts features of both modalities
through transformer encoders, it can capture long-range dependencies between
entities within each modality. Also, ReSTR fuses features of the two modalities
by a self-attention encoder, which enables flexible and adaptive interactions
between the two modalities in the fusion process. The fused features are fed to
a segmentation module, which works adaptively according to the image and
language expression in hand. ReSTR is evaluated and compared with previous work
on all public benchmarks, where it outperforms all existing models.