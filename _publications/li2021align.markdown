---
layout: publication
title: 'Align Before Fuse: Vision And Language Representation Learning With Momentum
  Distillation'
authors: Junnan Li, Ramprasaath R. Selvaraju, Akhilesh Deepak Gotmare, Shafiq Joty,
  Caiming Xiong, Steven Hoi
conference: Arxiv
year: 2021
bibkey: li2021align
citations: 820
additional_links: [{name: Code, url: 'https://github.com/salesforce/ALBEF/'}, {name: Paper,
    url: 'https://arxiv.org/abs/2107.07651'}]
tags: [Evaluation, Distance Metric Learning, Datasets, Scalability, Text Retrieval]
short_authors: Li et al.
---
Large-scale vision and language representation learning has shown promising
improvements on various vision-language tasks. Most existing methods employ a
transformer-based multimodal encoder to jointly model visual tokens
(region-based image features) and word tokens. Because the visual tokens and
word tokens are unaligned, it is challenging for the multimodal encoder to
learn image-text interactions. In this paper, we introduce a contrastive loss
to ALign the image and text representations BEfore Fusing (ALBEF) them through
cross-modal attention, which enables more grounded vision and language
representation learning. Unlike most existing methods, our method does not
require bounding box annotations nor high-resolution images. In order to
improve learning from noisy web data, we propose momentum distillation, a
self-training method which learns from pseudo-targets produced by a momentum
model. We provide a theoretical analysis of ALBEF from a mutual information
maximization perspective, showing that different training tasks can be
interpreted as different ways to generate views for an image-text pair. ALBEF
achieves state-of-the-art performance on multiple downstream vision-language
tasks. On image-text retrieval, ALBEF outperforms methods that are pre-trained
on orders of magnitude larger datasets. On VQA and NLVR\(^2\), ALBEF achieves
absolute improvements of 2.37% and 3.84% compared to the state-of-the-art,
while enjoying faster inference speed. Code and pre-trained models are
available at https://github.com/salesforce/ALBEF/.