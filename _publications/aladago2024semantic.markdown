---
layout: publication
title: Semantic Compositions Enhance Vision-language Contrastive Learning
authors: Maxwell Aladago, Lorenzo Torresani, Soroush Vosoughi
conference: Arxiv
year: 2024
bibkey: aladago2024semantic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.01408'}]
tags: [Datasets, Self-Supervised, Multimodal Retrieval, Evaluation, Few-shot & Zero-shot]
short_authors: Maxwell Aladago, Lorenzo Torresani, Soroush Vosoughi
---
In the field of vision-language contrastive learning, models such as CLIP
capitalize on matched image-caption pairs as positive examples and leverage
within-batch non-matching pairs as negatives. This approach has led to
remarkable outcomes in zero-shot image classification, cross-modal retrieval,
and linear evaluation tasks. We show that the zero-shot classification and
retrieval capabilities of CLIP-like models can be improved significantly
through the introduction of semantically composite examples during pretraining.
Inspired by CutMix in vision categorization, we create semantically composite
image-caption pairs by merging elements from two distinct instances in the
dataset via a novel procedure. Our method fuses the captions and blends 50% of
each image to form a new composite sample. This simple technique (termed CLIP-C
for CLIP Compositions), devoid of any additional computational overhead or
increase in model parameters, significantly improves zero-shot image
classification and cross-modal retrieval. The benefits of CLIP-C are
particularly pronounced in settings with relatively limited pretraining data.