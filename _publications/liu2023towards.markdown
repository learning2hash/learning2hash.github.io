---
layout: publication
title: Towards Better Entity Linking With Multi-view Enhanced Distillation
authors: Yi Liu, Yuan Tian, Jianxun Lian, Xinlong Wang, Yanan Cao, Fang Fang, Wen
  Zhang, Haizhen Huang, Denvy Deng, Qi Zhang
conference: 'Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2023
bibkey: liu2023towards
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.17371'}]
tags: [ACL, Tools & Libraries, Scalability, Evaluation]
short_authors: Liu et al.
---
Dense retrieval is widely used for entity linking to retrieve entities from
large-scale knowledge bases. Mainstream techniques are based on a dual-encoder
framework, which encodes mentions and entities independently and calculates
their relevances via rough interaction metrics, resulting in difficulty in
explicitly modeling multiple mention-relevant parts within entities to match
divergent mentions. Aiming at learning entity representations that can match
divergent mentions, this paper proposes a Multi-View Enhanced Distillation
(MVD) framework, which can effectively transfer knowledge of multiple
fine-grained and mention-relevant parts within entities from cross-encoders to
dual-encoders. Each entity is split into multiple views to avoid irrelevant
information being over-squashed into the mention-relevant view. We further
design cross-alignment and self-alignment mechanisms for this framework to
facilitate fine-grained knowledge distillation from the teacher model to the
student model. Meanwhile, we reserve a global-view that embeds the entity as a
whole to prevent dispersal of uniform information. Experiments show our method
achieves state-of-the-art performance on several entity linking benchmarks.