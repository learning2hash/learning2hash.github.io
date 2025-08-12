---
layout: publication
title: Training Vision Transformers With Only 2040 Images
authors: Yun-Hao Cao, Hao Yu, Jianxin Wu
conference: Lecture Notes in Computer Science
year: 2022
bibkey: cao2022training
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.10728'}]
tags: ["Datasets"]
short_authors: Yun-Hao Cao, Hao Yu, Jianxin Wu
---
Vision Transformers (ViTs) is emerging as an alternative to convolutional
neural networks (CNNs) for visual recognition. They achieve competitive results
with CNNs but the lack of the typical convolutional inductive bias makes them
more data-hungry than common CNNs. They are often pretrained on JFT-300M or at
least ImageNet and few works study training ViTs with limited data. In this
paper, we investigate how to train ViTs with limited data (e.g., 2040 images).
We give theoretical analyses that our method (based on parametric instance
discrimination) is superior to other methods in that it can capture both
feature alignment and instance similarities. We achieve state-of-the-art
results when training from scratch on 7 small datasets under various ViT
backbones. We also investigate the transferring ability of small datasets and
find that representations learned from small datasets can even improve
large-scale ImageNet training.