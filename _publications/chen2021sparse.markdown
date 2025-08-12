---
layout: publication
title: Sparse Spatial Transformers For Few-shot Learning
authors: Haoxing Chen, Huaxiong Li, Yaohui Li, Chunlin Chen
conference: Science China Information Sciences
year: 2023
bibkey: chen2021sparse
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.12932'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Chen et al.
---
Learning from limited data is challenging because data scarcity leads to a
poor generalization of the trained model. A classical global pooled
representation will probably lose useful local information. Many few-shot
learning methods have recently addressed this challenge using deep descriptors
and learning a pixel-level metric. However, using deep descriptors as feature
representations may lose image contextual information. Moreover, most of these
methods independently address each class in the support set, which cannot
sufficiently use discriminative information and task-specific embeddings. In
this paper, we propose a novel transformer-based neural network architecture
called sparse spatial transformers (SSFormers), which finds task-relevant
features and suppresses task-irrelevant features. Particularly, we first divide
each input image into several image patches of different sizes to obtain dense
local features. These features retain contextual information while expressing
local information. Then, a sparse spatial transformer layer is proposed to find
spatial correspondence between the query image and the full support set to
select task-relevant image patches and suppress task-irrelevant image patches.
Finally, we propose using an image patch-matching module to calculate the
distance between dense local representations, thus determining which category
the query image belongs to in the support set. Extensive experiments on popular
few-shot learning benchmarks demonstrate the superiority of our method over
state-of-the-art methods. Our source code is available at
https://github.com/chenhaoxing/ssformers.