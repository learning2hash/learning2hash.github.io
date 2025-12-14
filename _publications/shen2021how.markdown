---
layout: publication
title: How Much Can CLIP Benefit Vision-and-language Tasks?
authors: Sheng Shen, Liunian Harold Li, Hao Tan, Mohit Bansal, Anna Rohrbach, Kai-Wei
  Chang, Zhewei Yao, Kurt Keutzer
conference: Arxiv
year: 2021
bibkey: shen2021how
citations: 152
additional_links: [{name: Code, url: 'https://github.com/clip-vil/CLIP-ViL'}, {name: Paper,
    url: 'https://arxiv.org/abs/2107.06383'}]
tags: [Scalability, Evaluation, Few-shot & Zero-shot]
short_authors: Shen et al.
---
Most existing Vision-and-Language (V&L) models rely on pre-trained visual
encoders, using a relatively small set of manually-annotated data (as compared
to web-crawled data), to perceive the visual world. However, it has been
observed that large-scale pretraining usually can result in better
generalization performance, e.g., CLIP (Contrastive Language-Image
Pre-training), trained on a massive amount of image-caption pairs, has shown a
strong zero-shot capability on various vision tasks. To further study the
advantage brought by CLIP, we propose to use CLIP as the visual encoder in
various V&L models in two typical scenarios: 1) plugging CLIP into
task-specific fine-tuning; 2) combining CLIP with V&L pre-training and
transferring to downstream tasks. We show that CLIP significantly outperforms
widely-used visual encoders trained with in-domain annotated data, such as
BottomUp-TopDown. We achieve competitive or better results on diverse V&L
tasks, while establishing new state-of-the-art results on Visual Question
Answering, Visual Entailment, and V&L Navigation tasks. We release our code at
https://github.com/clip-vil/CLIP-ViL.