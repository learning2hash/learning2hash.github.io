---
layout: publication
title: 'Specklenn: A Unified Embedding For Real-time Speckle Pattern Classification
  In X-ray Single-particle Imaging With Limited Labeled Examples'
authors: Cong Wang, Eric Florin, Hsing-Yin Chang, Jana Thayer, Chun Hong Yoon
conference: IUCrJ
year: 2023
bibkey: wang2023specklenn
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.06895'}]
tags: ["Efficiency"]
short_authors: Wang et al.
---
With X-ray free-electron lasers (XFELs), it is possible to determine the
three-dimensional structure of noncrystalline nanoscale particles using X-ray
single-particle imaging (SPI) techniques at room temperature. Classifying SPI
scattering patterns, or "speckles", to extract single hits that are needed for
real-time vetoing and three-dimensional reconstruction poses a challenge for
high data rate facilities like European XFEL and LCLS-II-HE. Here, we introduce
SpeckleNN, a unified embedding model for real-time speckle pattern
classification with limited labeled examples that can scale linearly with
dataset size. Trained with twin neural networks, SpeckleNN maps speckle
patterns to a unified embedding vector space, where similarity is measured by
Euclidean distance. We highlight its few-shot classification capability on new
never-seen samples and its robust performance despite only tens of labels per
classification category even in the presence of substantial missing detector
areas. Without the need for excessive manual labeling or even a full detector
image, our classification method offers a great solution for real-time
high-throughput SPI experiments.