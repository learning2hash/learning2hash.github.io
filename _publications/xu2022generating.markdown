---
layout: publication
title: Generating Representative Samples For Few-shot Classification
authors: Jingyi Xu, Hieu Le
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: xu2022generating
citations: 66
additional_links: [{name: Code, url: 'https://github.com/cvlab-stonybrook/fsl-rsvae'},
  {name: Paper, url: 'https://arxiv.org/abs/2205.02918'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Jingyi Xu, Hieu Le
---
Few-shot learning (FSL) aims to learn new categories with a few visual
samples per class. Few-shot class representations are often biased due to data
scarcity. To mitigate this issue, we propose to generate visual samples based
on semantic embeddings using a conditional variational autoencoder (CVAE)
model. We train this CVAE model on base classes and use it to generate features
for novel classes. More importantly, we guide this VAE to strictly generate
representative samples by removing non-representative samples from the base
training set when training the CVAE model. We show that this training scheme
enhances the representativeness of the generated samples and therefore,
improves the few-shot classification results. Experimental results show that
our method improves three FSL baseline methods by substantial margins,
achieving state-of-the-art few-shot classification performance on miniImageNet
and tieredImageNet datasets for both 1-shot and 5-shot settings. Code is
available at: https://github.com/cvlab-stonybrook/fsl-rsvae.