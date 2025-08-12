---
layout: publication
title: 'Diverse Instance Discovery: Vision-transformer For Instance-aware Multi-label
  Image Recognition'
authors: Yunqing Hu, Xuan Jin, Yin Zhang, Haiwen Hong, Jingfeng Zhang, Feihu Yan,
  Yuan He, Hui Xue
conference: 2022 IEEE International Conference on Multimedia and Expo (ICME)
year: 2022
bibkey: hu2022diverse
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.10731'}]
tags: []
short_authors: Hu et al.
---
Previous works on multi-label image recognition (MLIR) usually use CNNs as a
starting point for research. In this paper, we take pure Vision Transformer
(ViT) as the research base and make full use of the advantages of Transformer
with long-range dependency modeling to circumvent the disadvantages of CNNs
limited to local receptive field. However, for multi-label images containing
multiple objects from different categories, scales, and spatial relations, it
is not optimal to use global information alone. Our goal is to leverage ViT's
patch tokens and self-attention mechanism to mine rich instances in multi-label
images, named diverse instance discovery (DiD). To this end, we propose a
semantic category-aware module and a spatial relationship-aware module,
respectively, and then combine the two by a re-constraint strategy to obtain
instance-aware attention maps. Finally, we propose a weakly supervised object
localization-based approach to extract multi-scale local features, to form a
multi-view pipeline. Our method requires only weakly supervised information at
the label level, no additional knowledge injection or other strongly supervised
information is required. Experiments on three benchmark datasets show that our
method significantly outperforms previous works and achieves state-of-the-art
results under fair experimental comparisons.