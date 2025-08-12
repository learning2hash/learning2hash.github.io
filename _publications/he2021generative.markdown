---
layout: publication
title: Generative Zero-shot Network Quantization
authors: Xiangyu He, Qinghao Hu, Peisong Wang, Jian Cheng
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2021
bibkey: he2021generative
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.08430'}]
tags: ["CVPR", "Few Shot & Zero Shot", "Quantization"]
short_authors: He et al.
---
Convolutional neural networks are able to learn realistic image priors from
numerous training samples in low-level image generation and restoration. We
show that, for high-level image recognition tasks, we can further reconstruct
"realistic" images of each category by leveraging intrinsic Batch Normalization
(BN) statistics without any training data. Inspired by the popular VAE/GAN
methods, we regard the zero-shot optimization process of synthetic images as
generative modeling to match the distribution of BN statistics. The generated
images serve as a calibration set for the following zero-shot network
quantizations. Our method meets the needs for quantizing models based on
sensitive information, \textit\{e.g.,\} due to privacy concerns, no data is
available. Extensive experiments on benchmark datasets show that, with the help
of generated data, our approach consistently outperforms existing data-free
quantization methods.