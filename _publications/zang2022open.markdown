---
layout: publication
title: Open-vocabulary DETR With Conditional Matching
authors: Yuhang Zang, Wei Li, Kaiyang Zhou, Chen Huang, Chen Change Loy
conference: Lecture Notes in Computer Science
year: 2022
bibkey: zang2022open
citations: 109
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.11876'}]
tags: []
short_authors: Zang et al.
---
Open-vocabulary object detection, which is concerned with the problem of
detecting novel objects guided by natural language, has gained increasing
attention from the community. Ideally, we would like to extend an
open-vocabulary detector such that it can produce bounding box predictions
based on user inputs in form of either natural language or exemplar image. This
offers great flexibility and user experience for human-computer interaction. To
this end, we propose a novel open-vocabulary detector based on DETR -- hence
the name OV-DETR -- which, once trained, can detect any object given its class
name or an exemplar image. The biggest challenge of turning DETR into an
open-vocabulary detector is that it is impossible to calculate the
classification cost matrix of novel classes without access to their labeled
images. To overcome this challenge, we formulate the learning objective as a
binary matching one between input queries (class name or exemplar image) and
the corresponding objects, which learns useful correspondence to generalize to
unseen queries during testing. For training, we choose to condition the
Transformer decoder on the input embeddings obtained from a pre-trained
vision-language model like CLIP, in order to enable matching for both text and
image queries. With extensive experiments on LVIS and COCO datasets, we
demonstrate that our OV-DETR -- the first end-to-end Transformer-based
open-vocabulary detector -- achieves non-trivial improvements over current
state of the arts.