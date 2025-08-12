---
layout: publication
title: Learning From Multi-domain Artistic Images For Arbitrary Style Transfer
authors: Zheng Xu, Michael Wilber, Chen Fang, Aaron Hertzmann, Hailin Jin
conference: Arxiv
year: 2019
bibkey: xu2018learning
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1805.09987'}]
tags: []
short_authors: Xu et al.
---
We propose a fast feed-forward network for arbitrary style transfer, which
can generate stylized image for previously unseen content and style image
pairs. Besides the traditional content and style representation based on deep
features and statistics for textures, we use adversarial networks to regularize
the generation of stylized images. Our adversarial network learns the intrinsic
property of image styles from large-scale multi-domain artistic images. The
adversarial training is challenging because both the input and output of our
generator are diverse multi-domain images. We use a conditional generator that
stylized content by shifting the statistics of deep features, and a conditional
discriminator based on the coarse category of styles. Moreover, we propose a
mask module to spatially decide the stylization level and stabilize adversarial
training by avoiding mode collapse. As a side effect, our trained discriminator
can be applied to rank and select representative stylized images. We
qualitatively and quantitatively evaluate the proposed method, and compare with
recent style transfer methods. We release our code and model at
https://github.com/nightldj/behance_release.