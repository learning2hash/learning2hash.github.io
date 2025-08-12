---
layout: publication
title: Generalized Large-scale Data Condensation Via Various Backbone And Statistical
  Matching
authors: Shitong Shao, Zeyuan Yin, Muxin Zhou, Xindong Zhang, Zhiqiang Shen
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: shao2023generalized
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.17950'}]
tags: ["CVPR", "Scalability"]
short_authors: Shao et al.
---
The lightweight "local-match-global" matching introduced by SRe2L
successfully creates a distilled dataset with comprehensive information on the
full 224x224 ImageNet-1k. However, this one-sided approach is limited to a
particular backbone, layer, and statistics, which limits the improvement of the
generalization of a distilled dataset. We suggest that sufficient and various
"local-match-global" matching are more precise and effective than a single one
and has the ability to create a distilled dataset with richer information and
better generalization. We call this perspective "generalized matching" and
propose Generalized Various Backbone and Statistical Matching (G-VBSM) in this
work, which aims to create a synthetic dataset with densities, ensuring
consistency with the complete dataset across various backbones, layers, and
statistics. As experimentally demonstrated, G-VBSM is the first algorithm to
obtain strong performance across both small-scale and large-scale datasets.
Specifically, G-VBSM achieves a performance of 38.7% on CIFAR-100 with
128-width ConvNet, 47.6% on Tiny-ImageNet with ResNet18, and 31.4% on the full
224x224 ImageNet-1k with ResNet18, under images per class (IPC) 10, 50, and 10,
respectively. These results surpass all SOTA methods by margins of 3.9%, 6.5%,
and 10.1%, respectively.