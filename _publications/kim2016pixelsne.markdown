---
layout: publication
title: 'Pixelsne: Visualizing Fast With Just Enough Precision Via Pixel-aligned Stochastic
  Neighbor Embedding'
authors: Minjeong Kim, Minsuk Choi, Sunwoong Lee, Jian Tang, Haesun Park, Jaegul Choo
conference: Arxiv
year: 2016
bibkey: kim2016pixelsne
citations: 4
additional_links: [{name: Code, url: 'https://github.com/awesome-davian/PixelSNE'},
  {name: Paper, url: 'https://arxiv.org/abs/1611.02568'}]
tags: ["Evaluation", "Scalability"]
short_authors: Kim et al.
---
Embedding and visualizing large-scale high-dimensional data in a
two-dimensional space is an important problem since such visualization can
reveal deep insights out of complex data. Most of the existing embedding
approaches, however, run on an excessively high precision, ignoring the fact
that at the end, embedding outputs are converted into coarse-grained discrete
pixel coordinates in a screen space. Motivated by such an observation and
directly considering pixel coordinates in an embedding optimization process, we
accelerate Barnes-Hut tree-based t-distributed stochastic neighbor embedding
(BH-SNE), known as a state-of-the-art 2D embedding method, and propose a novel
method called PixelSNE, a highly-efficient, screen resolution-driven 2D
embedding method with a linear computational complexity in terms of the number
of data items. Our experimental results show the significantly fast running
time of PixelSNE by a large margin against BH-SNE, while maintaining the
minimal degradation in the embedding quality. Finally, the source code of our
method is publicly available at https://github.com/awesome-davian/PixelSNE