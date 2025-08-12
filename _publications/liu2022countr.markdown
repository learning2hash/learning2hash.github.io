---
layout: publication
title: 'Countr: Transformer-based Generalised Visual Counting'
authors: Chang Liu, Yujie Zhong, Andrew Zisserman, Weidi Xie
conference: Arxiv
year: 2022
bibkey: liu2022countr
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.13721'}]
tags: []
short_authors: Liu et al.
---
In this paper, we consider the problem of generalised visual object counting,
with the goal of developing a computational model for counting the number of
objects from arbitrary semantic categories, using arbitrary number of
"exemplars", i.e. zero-shot or few-shot counting. To this end, we make the
following four contributions: (1) We introduce a novel transformer-based
architecture for generalised visual object counting, termed as Counting
Transformer (CounTR), which explicitly capture the similarity between image
patches or with given "exemplars" with the attention mechanism;(2) We adopt a
two-stage training regime, that first pre-trains the model with self-supervised
learning, and followed by supervised fine-tuning;(3) We propose a simple,
scalable pipeline for synthesizing training images with a large number of
instances or that from different semantic categories, explicitly forcing the
model to make use of the given "exemplars";(4) We conduct thorough ablation
studies on the large-scale counting benchmark, e.g. FSC-147, and demonstrate
state-of-the-art performance on both zero and few-shot settings.