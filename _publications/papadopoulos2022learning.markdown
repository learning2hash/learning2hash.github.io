---
layout: publication
title: Learning Program Representations For Food Images And Cooking Recipes
authors: Dim P. Papadopoulos, Enrique Mora, Nadiia Chepurko, Kuan Wei Huang, Ferda
  Ofli, Antonio Torralba
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: papadopoulos2022learning
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.16071'}]
tags: [Multimodal Retrieval, CVPR]
short_authors: Papadopoulos et al.
---
In this paper, we are interested in modeling a how-to instructional
procedure, such as a cooking recipe, with a meaningful and rich high-level
representation. Specifically, we propose to represent cooking recipes and food
images as cooking programs. Programs provide a structured representation of the
task, capturing cooking semantics and sequential relationships of actions in
the form of a graph. This allows them to be easily manipulated by users and
executed by agents. To this end, we build a model that is trained to learn a
joint embedding between recipes and food images via self-supervision and
jointly generate a program from this embedding as a sequence. To validate our
idea, we crowdsource programs for cooking recipes and show that: (a) projecting
the image-recipe embeddings into programs leads to better cross-modal retrieval
results; (b) generating programs from images leads to better recognition
results compared to predicting raw cooking instructions; and (c) we can
generate food images by manipulating programs via optimizing the latent code of
a GAN. Code, data, and models are available online.