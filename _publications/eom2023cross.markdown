---
layout: publication
title: Cross-modal Retrieval Meets Inference:improving Zero-shot Classification With
  Cross-modal Retrieval
authors: Seongha Eom, Namgyu Ho, Jaehoon Oh, Se-Young Yun
conference: Arxiv
year: 2023
bibkey: eom2023cross
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.15273'}]
tags: [Evaluation, Multimodal Retrieval, Datasets, Few-shot & Zero-shot]
short_authors: Eom et al.
---
Contrastive language-image pre-training (CLIP) has demonstrated remarkable
zero-shot classification ability, namely image classification using novel text
labels. Existing works have attempted to enhance CLIP by fine-tuning on
downstream tasks, but these have inadvertently led to performance degradation
on unseen classes, thus harming zero-shot generalization. This paper aims to
address this challenge by leveraging readily available image-text pairs from an
external dataset for cross-modal guidance during inference. To this end, we
propose X-MoRe, a novel inference method comprising two key steps: (1)
cross-modal retrieval and (2) modal-confidence-based ensemble. Given a query
image, we harness the power of CLIP's cross-modal representations to retrieve
relevant textual information from an external image-text pair dataset. Then, we
assign higher weights to the more reliable modality between the original query
image and retrieved text, contributing to the final prediction. X-MoRe
demonstrates robust performance across a diverse set of tasks without the need
for additional training, showcasing the effectiveness of utilizing cross-modal
features to maximize CLIP's zero-shot ability.