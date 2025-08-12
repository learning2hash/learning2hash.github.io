---
layout: publication
title: Supervision Accelerates Pre-training In Contrastive Semi-supervised Learning
  Of Visual Representations
authors: Mahmoud Assran, Nicolas Ballas, Lluis Castrejon, Michael Rabbat
conference: Arxiv
year: 2020
bibkey: assran2020supervision
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.10803'}]
tags: ["Efficiency", "Self-Supervised", "Supervised"]
short_authors: Assran et al.
---
We investigate a strategy for improving the efficiency of contrastive
learning of visual representations by leveraging a small amount of supervised
information during pre-training. We propose a semi-supervised loss, SuNCEt,
based on noise-contrastive estimation and neighbourhood component analysis,
that aims to distinguish examples of different classes in addition to the
self-supervised instance-wise pretext tasks. On ImageNet, we find that SuNCEt
can be used to match the semi-supervised learning accuracy of previous
contrastive approaches while using less than half the amount of pre-training
and compute. Our main insight is that leveraging even a small amount of labeled
data during pre-training, and not only during fine-tuning, provides an
important signal that can significantly accelerate contrastive learning of
visual representations. Our code is available online at
github.com/facebookresearch/suncet.