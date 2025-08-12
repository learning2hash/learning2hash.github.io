---
layout: publication
title: Feature Fusion Vision Transformer For Fine-grained Visual Categorization
authors: Jun Wang, Xiaohan Yu, Yongsheng Gao
conference: Arxiv
year: 2021
bibkey: wang2021feature
citations: 76
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2107.02341'}]
tags: []
short_authors: Jun Wang, Xiaohan Yu, Yongsheng Gao
---
The core for tackling the fine-grained visual categorization (FGVC) is to
learn subtle yet discriminative features. Most previous works achieve this by
explicitly selecting the discriminative parts or integrating the attention
mechanism via CNN-based approaches.However, these methods enhance the
computational complexity and make the modeldominated by the regions containing
the most of the objects. Recently, vision trans-former (ViT) has achieved SOTA
performance on general image recognition tasks. Theself-attention mechanism
aggregates and weights the information from all patches to the classification
token, making it perfectly suitable for FGVC. Nonetheless, the classifi-cation
token in the deep layer pays more attention to the global information, lacking
the local and low-level features that are essential for FGVC. In this work, we
proposea novel pure transformer-based framework Feature Fusion Vision
Transformer (FFVT)where we aggregate the important tokens from each transformer
layer to compensate thelocal, low-level and middle-level information. We design
a novel token selection mod-ule called mutual attention weight selection (MAWS)
to guide the network effectively and efficiently towards selecting
discriminative tokens without introducing extra param-eters. We verify the
effectiveness of FFVT on three benchmarks where FFVT achieves the
state-of-the-art performance.