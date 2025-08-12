---
layout: publication
title: Towards Zero-shot Human-object Interaction Detection Via Vision-language Integration
authors: Weiying Xue, Qi Liu, Qiwei Xiong, Yuxiao Wang, Zhenao Wei, Xiaofen Xing,
  Xiangmin Xu
conference: Arxiv
year: 2024
bibkey: xue2024towards
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.07246'}]
tags: []
short_authors: Xue et al.
---
Human-object interaction (HOI) detection aims to locate human-object pairs
and identify their interaction categories in images. Most existing methods
primarily focus on supervised learning, which relies on extensive manual HOI
annotations. In this paper, we propose a novel framework, termed Knowledge
Integration to HOI (KI2HOI), that effectively integrates the knowledge of
visual-language model to improve zero-shot HOI detection. Specifically, the
verb feature learning module is designed based on visual semantics, by
employing the verb extraction decoder to convert corresponding verb queries
into interaction-specific category representations. We develop an effective
additive self-attention mechanism to generate more comprehensive visual
representations. Moreover, the innovative interaction representation decoder
effectively extracts informative regions by integrating spatial and visual
feature information through a cross-attention mechanism. To deal with zero-shot
learning in low-data, we leverage a priori knowledge from the CLIP text encoder
to initialize the linear classifier for enhanced interaction understanding.
Extensive experiments conducted on the mainstream HICO-DET and V-COCO datasets
demonstrate that our model outperforms the previous methods in various
zero-shot and full-supervised settings.