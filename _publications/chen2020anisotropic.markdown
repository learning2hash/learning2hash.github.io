---
layout: publication
title: Anisotropic Stroke Control For Multiple Artists Style Transfer
authors: Xuanhong Chen, Xirui Yan, Naiyuan Liu, Ting Qiu, Bingbing Ni
conference: Proceedings of the 28th ACM International Conference on Multimedia
year: 2020
bibkey: chen2020anisotropic
citations: 11
additional_links: [{name: Code, url: 'https://github.com/neuralchen/ASMAGAN'}, {name: Paper,
    url: 'https://arxiv.org/abs/2010.08175'}]
tags: []
short_authors: Chen et al.
---
Though significant progress has been made in artistic style transfer,
semantic information is usually difficult to be preserved in a fine-grained
locally consistent manner by most existing methods, especially when multiple
artists styles are required to transfer within one single model. To circumvent
this issue, we propose a Stroke Control Multi-Artist Style Transfer framework.
On the one hand, we develop a multi-condition single-generator structure which
first performs multi-artist style transfer. On the one hand, we design an
Anisotropic Stroke Module (ASM) which realizes the dynamic adjustment of
style-stroke between the non-trivial and the trivial regions. ASM endows the
network with the ability of adaptive semantic-consistency among various styles.
On the other hand, we present an novel Multi-Scale Projection Discriminator\} to
realize the texture-level conditional generation. In contrast to the
single-scale conditional discriminator, our discriminator is able to capture
multi-scale texture clue to effectively distinguish a wide range of artistic
styles. Extensive experimental results well demonstrate the feasibility and
effectiveness of our approach. Our framework can transform a photograph into
different artistic style oil painting via only ONE single model. Furthermore,
the results are with distinctive artistic style and retain the anisotropic
semantic information. The code is already available on github:
https://github.com/neuralchen/ASMAGAN.