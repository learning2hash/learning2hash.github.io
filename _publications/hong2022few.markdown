---
layout: publication
title: Few-shot Image Generation Using Discrete Content Representation
authors: Yan Hong, Li Niu, Jianfu Zhang, Liqing Zhang
conference: Proceedings of the 30th ACM International Conference on Multimedia
year: 2022
bibkey: hong2022few
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.10833'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Hong et al.
---
Few-shot image generation and few-shot image translation are two related
tasks, both of which aim to generate new images for an unseen category with
only a few images. In this work, we make the first attempt to adapt few-shot
image translation method to few-shot image generation task. Few-shot image
translation disentangles an image into style vector and content map. An unseen
style vector can be combined with different seen content maps to produce
different images. However, it needs to store seen images to provide content
maps and the unseen style vector may be incompatible with seen content maps. To
adapt it to few-shot image generation task, we learn a compact dictionary of
local content vectors via quantizing continuous content maps into discrete
content maps instead of storing seen images. Furthermore, we model the
autoregressive distribution of discrete content map conditioned on style
vector, which can alleviate the incompatibility between content map and style
vector. Qualitative and quantitative results on three real datasets demonstrate
that our model can produce images of higher diversity and fidelity for unseen
categories than previous methods.