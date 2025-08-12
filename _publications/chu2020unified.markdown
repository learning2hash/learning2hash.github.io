---
layout: publication
title: A Unified Mixture-view Framework For Unsupervised Representation Learning
authors: Xiangxiang Chu, Xiaohang Zhan, Bo Zhang
conference: Arxiv
year: 2020
bibkey: chu2020unified
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.13356'}]
tags: ["Self-Supervised", "Unsupervised"]
short_authors: Xiangxiang Chu, Xiaohang Zhan, Bo Zhang
---
Recent unsupervised contrastive representation learning follows a Single
Instance Multi-view (SIM) paradigm where positive pairs are usually constructed
with intra-image data augmentation. In this paper, we propose an effective
approach called Beyond Single Instance Multi-view (BSIM). Specifically, we
impose more accurate instance discrimination capability by measuring the joint
similarity between two randomly sampled instances and their mixture, namely
spurious-positive pairs. We believe that learning joint similarity helps to
improve the performance when encoded features are distributed more evenly in
the latent space. We apply it as an orthogonal improvement for unsupervised
contrastive representation learning, including current outstanding methods
SimCLR, MoCo, and BYOL. We evaluate our learned representations on many
downstream benchmarks like linear classification on ImageNet-1k and PASCAL VOC
2007, object detection on MS COCO 2017 and VOC, etc. We obtain substantial
gains with a large margin almost on all these tasks compared with prior arts.