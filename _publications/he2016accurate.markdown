---
layout: publication
title: Accurate Text Localization In Natural Image With Cascaded Convolutional Text
  Network
authors: Tong He, Weilin Huang, Yu Qiao, Jian Yao
conference: Arxiv
year: 2016
bibkey: he2016accurate
citations: 84
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.09423'}]
tags: ["Robustness"]
short_authors: He et al.
---
We introduce a new top-down pipeline for scene text detection. We propose a
novel Cascaded Convolutional Text Network (CCTN) that joints two customized
convolutional networks for coarse-to-fine text localization. The CCTN fast
detects text regions roughly from a low-resolution image, and then accurately
localizes text lines from each enlarged region. We cast previous character
based detection into direct text region estimation, avoiding multiple bottom-
up post-processing steps. It exhibits surprising robustness and discriminative
power by considering whole text region as detection object which provides
strong semantic information. We customize convolutional network by develop- ing
rectangle convolutions and multiple in-network fusions. This enables it to
handle multi-shape and multi-scale text efficiently. Furthermore, the CCTN is
computationally efficient by sharing convolutional computations, and high-level
property allows it to be invariant to various languages and multiple
orientations. It achieves 0.84 and 0.86 F-measures on the ICDAR 2011 and ICDAR
2013, delivering substantial improvements over state-of-the-art results [23,
1].