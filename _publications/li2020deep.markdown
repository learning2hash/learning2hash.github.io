---
layout: publication
title: Deep Learning-based Image Compression With Trellis Coded Quantization
authors: Binglin Li, Mohammad Akbari, Jie Liang, Yang Wang
conference: 2020 Data Compression Conference (DCC)
year: 2020
bibkey: li2020deep
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.09417'}]
tags: ["Quantization"]
short_authors: Li et al.
---
Recently many works attempt to develop image compression models based on deep
learning architectures, where the uniform scalar quantizer (SQ) is commonly
applied to the feature maps between the encoder and decoder. In this paper, we
propose to incorporate trellis coded quantizer (TCQ) into a deep learning based
image compression framework. A soft-to-hard strategy is applied to allow for
back propagation during training. We develop a simple image compression model
that consists of three subnetworks (encoder, decoder and entropy estimation),
and optimize all of the components in an end-to-end manner. We experiment on
two high resolution image datasets and both show that our model can achieve
superior performance at low bit rates. We also show the comparisons between TCQ
and SQ based on our proposed baseline model and demonstrate the advantage of
TCQ.