---
layout: publication
title: 'Spaceedit: Learning A Unified Editing Space For Open-domain Image Editing'
authors: Jing Shi, Ning Xu, Haitian Zheng, Alex Smith, Jiebo Luo, Chenliang Xu
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: shi2021spaceedit
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.00180'}]
tags: ["CVPR", "Tools & Libraries"]
short_authors: Shi et al.
---
Recently, large pretrained models (e.g., BERT, StyleGAN, CLIP) have shown
great knowledge transfer and generalization capability on various downstream
tasks within their domains. Inspired by these efforts, in this paper we propose
a unified model for open-domain image editing focusing on color and tone
adjustment of open-domain images while keeping their original content and
structure. Our model learns a unified editing space that is more semantic,
intuitive, and easy to manipulate than the operation space (e.g., contrast,
brightness, color curve) used in many existing photo editing softwares. Our
model belongs to the image-to-image translation framework which consists of an
image encoder and decoder, and is trained on pairs of before- and after-images
to produce multimodal outputs. We show that by inverting image pairs into
latent codes of the learned editing space, our model can be leveraged for
various downstream editing tasks such as language-guided image editing,
personalized editing, editing-style clustering, retrieval, etc. We extensively
study the unique properties of the editing space in experiments and demonstrate
superior performance on the aforementioned tasks.