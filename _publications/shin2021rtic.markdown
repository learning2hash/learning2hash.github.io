---
layout: publication
title: 'RTIC: Residual Learning For Text And Image Composition Using Graph Convolutional
  Network'
authors: Minchul Shin, Yoonjae Cho, Byungsoo Ko, Geonmo Gu
conference: Arxiv
year: 2021
bibkey: shin2021rtic
citations: 23
additional_links: [{name: Code, url: 'https://github.com/nashory/rtic-gcn-pytorch'},
  {name: Paper, url: 'https://arxiv.org/abs/2104.03015'}]
tags: [Evaluation, Image Retrieval]
short_authors: Shin et al.
---
In this paper, we study the compositional learning of images and texts for
image retrieval. The query is given in the form of an image and text that
describes the desired modifications to the image; the goal is to retrieve the
target image that satisfies the given modifications and resembles the query by
composing information in both the text and image modalities. To remedy this, we
propose a novel architecture designed for the image-text composition task and
show that the proposed structure can effectively encode the differences between
the source and target images conditioned on the text. Furthermore, we introduce
a new joint training technique based on the graph convolutional network that is
generally applicable for any existing composition methods in a plug-and-play
manner. We found that the proposed technique consistently improves performance
and achieves state-of-the-art scores on various benchmarks. To avoid misleading
experimental results caused by trivial training hyper-parameters, we reproduce
all individual baselines and train models with a unified training environment.
We expect this approach to suppress undesirable effects from irrelevant
components and emphasize the image-text composition module's ability. Also, we
achieve the state-of-the-art score without restricting the training
environment, which implies the superiority of our method considering the gains
from hyper-parameter tuning. The code, including all the baseline methods, are
released https://github.com/nashory/rtic-gcn-pytorch.