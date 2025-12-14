---
layout: publication
title: 'Lit: Zero-shot Transfer With Locked-image Text Tuning'
authors: Xiaohua Zhai, Xiao Wang, Basil Mustafa, Andreas Steiner, Daniel Keysers,
  Alexander Kolesnikov, Lucas Beyer
conference: Arxiv
year: 2021
bibkey: zhai2021lit
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.07991'}]
tags: [Supervised, Unsupervised, Few-shot & Zero-shot, Datasets]
short_authors: Zhai et al.
---
This paper presents contrastive-tuning, a simple method employing contrastive
training to align image and text models while still taking advantage of their
pre-training. In our empirical study we find that locked pre-trained image
models with unlocked text models work best. We call this instance of
contrastive-tuning "Locked-image Tuning" (LiT), which just teaches a text model
to read out good representations from a pre-trained image model for new tasks.
A LiT model gains the capability of zero-shot transfer to new vision tasks,
such as image classification or retrieval. The proposed LiT is widely
applicable; it works reliably with multiple pre-training methods (supervised
and unsupervised) and across diverse architectures (ResNet, Vision Transformers
and MLP-Mixer) using three different image-text datasets. With the
transformer-based pre-trained ViT-g/14 model, the LiT model achieves 85.2%
zero-shot transfer accuracy on the ImageNet test set, and 82.5% on the
challenging out-of-distribution ObjectNet test set.