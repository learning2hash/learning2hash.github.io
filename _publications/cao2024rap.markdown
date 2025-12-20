---
layout: publication
title: 'RAP: Efficient Text-video Retrieval With Sparse-and-correlated Adapter'
authors: Meng Cao, Haoran Tang, Jinfa Huang, Peng Jin, Can Zhang, Ruyang Liu, Long
  Chen, Xiaodan Liang, Li Yuan, Ge Li
conference: Findings of the Association for Computational Linguistics ACL 2024
year: 2024
bibkey: cao2024rap
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.19465'}]
tags: ["Datasets", "Evaluation", "Scalability", "Video Retrieval"]
short_authors: Cao et al.
---
Text-Video Retrieval (TVR) aims to align relevant video content with natural
language queries. To date, most state-of-the-art TVR methods learn
image-to-video transfer learning based on large-scale pre-trained
visionlanguage models (e.g., CLIP). However, fully fine-tuning these
pre-trained models for TVR incurs prohibitively expensive computation costs. To
this end, we propose to conduct efficient text-video Retrieval with a
sparse-andcorrelated AdaPter (RAP), i.e., fine-tuning the pre-trained model
with a few parameterized layers. To accommodate the text-video scenario, we
equip our RAP with two indispensable characteristics: temporal sparsity and
correlation. Specifically, we propose a low-rank modulation module to refine
the per-image features from the frozen CLIP backbone, which accentuates salient
frames within the video features while alleviating temporal redundancy.
Besides, we introduce an asynchronous self-attention mechanism that first
selects the top responsive visual patches and augments the correlation modeling
between them with learnable temporal and patch offsets. Extensive experiments
on four TVR datasets demonstrate that RAP achieves superior or comparable
performance compared to the fully fine-tuned counterpart and other
parameter-efficient fine-tuning methods.