---
layout: publication
title: 'Unicoder-vl: A Universal Encoder For Vision And Language By Cross-modal Pre-training'
authors: Gen Li, Nan Duan, Yuejian Fang, Ming Gong, Daxin Jiang, Ming Zhou
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2020
bibkey: li2019unicoder
citations: 702
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.06066'}]
tags: [AAAI, Scalability, Text Retrieval]
short_authors: Li et al.
---
We propose Unicoder-VL, a universal encoder that aims to learn joint
representations of vision and language in a pre-training manner. Borrow ideas
from cross-lingual pre-trained models, such as XLM and Unicoder, both visual
and linguistic contents are fed into a multi-layer Transformer for the
cross-modal pre-training, where three pre-trained tasks are employed, including
Masked Language Modeling (MLM), Masked Object Classification (MOC) and
Visual-linguistic Matching (VLM). The first two tasks learn context-aware
representations for input tokens based on linguistic and visual contents
jointly. The last task tries to predict whether an image and a text describe
each other. After pretraining on large-scale image-caption pairs, we transfer
Unicoder-VL to caption-based image-text retrieval and visual commonsense
reasoning, with just one additional output layer. We achieve state-of-the-art
or comparable results on both two tasks and show the powerful ability of the
cross-modal pre-training.