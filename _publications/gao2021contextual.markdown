---
layout: publication
title: Contextual Non-local Alignment Over Full-scale Representation For Text-based
  Person Search
authors: Chenyang Gao, Guanyu Cai, Xinyang Jiang, Feng Zheng, Jun Zhang, Yifei Gong,
  Pai Peng, Xiaowei Guo, Xing Sun
conference: Arxiv
year: 2021
bibkey: gao2021contextual
citations: 59
additional_links: [{name: Code, url: 'https://github.com/TencentYoutuResearch/PersonReID-NAFS'},
  {name: Paper, url: 'https://arxiv.org/abs/2101.03036'}]
tags: []
short_authors: Gao et al.
---
Text-based person search aims at retrieving target person in an image gallery
using a descriptive sentence of that person. It is very challenging since modal
gap makes effectively extracting discriminative features more difficult.
Moreover, the inter-class variance of both pedestrian images and descriptions
is small. So comprehensive information is needed to align visual and textual
clues across all scales. Most existing methods merely consider the local
alignment between images and texts within a single scale (e.g. only global
scale or only partial scale) then simply construct alignment at each scale
separately. To address this problem, we propose a method that is able to
adaptively align image and textual features across all scales, called NAFS
(i.e.Non-local Alignment over Full-Scale representations). Firstly, a novel
staircase network structure is proposed to extract full-scale image features
with better locality. Secondly, a BERT with locality-constrained attention is
proposed to obtain representations of descriptions at different scales. Then,
instead of separately aligning features at each scale, a novel contextual
non-local attention mechanism is applied to simultaneously discover latent
alignments across all scales. The experimental results show that our method
outperforms the state-of-the-art methods by 5.53% in terms of top-1 and 5.35%
in terms of top-5 on text-based person search dataset. The code is available at
https://github.com/TencentYoutuResearch/PersonReID-NAFS