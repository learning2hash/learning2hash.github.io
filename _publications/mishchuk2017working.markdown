---
layout: publication
title: 'Working Hard To Know Your Neighbor''s Margins: Local Descriptor Learning Loss'
authors: Anastasiya Mishchuk, Dmytro Mishkin, Filip Radenovic, Jiri Matas
conference: Arxiv
year: 2017
bibkey: mishchuk2017working
citations: 268
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.10872'}]
tags: ["Evaluation"]
short_authors: Mishchuk et al.
---
We introduce a novel loss for learning local feature descriptors which is
inspired by the Lowe's matching criterion for SIFT. We show that the proposed
loss that maximizes the distance between the closest positive and closest
negative patch in the batch is better than complex regularization methods; it
works well for both shallow and deep convolution network architectures.
Applying the novel loss to the L2Net CNN architecture results in a compact
descriptor -- it has the same dimensionality as SIFT (128) that shows
state-of-art performance in wide baseline stereo, patch verification and
instance retrieval benchmarks. It is fast, computing a descriptor takes about 1
millisecond on a low-end GPU.