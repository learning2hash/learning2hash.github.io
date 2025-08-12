---
layout: publication
title: One-shot Object Detection Without Fine-tuning
authors: Xiang Li, Lin Zhang, Yau Pun Chen, Yu-Wing Tai, Chi-Keung Tang
conference: Arxiv
year: 2020
bibkey: li2020one
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.03819'}]
tags: []
short_authors: Li et al.
---
Deep learning has revolutionized object detection thanks to large-scale
datasets, but their object categories are still arguably very limited. In this
paper, we attempt to enrich such categories by addressing the one-shot object
detection problem, where the number of annotated training examples for learning
an unseen class is limited to one. We introduce a two-stage model consisting of
a first stage Matching-FCOS network and a second stage Structure-Aware Relation
Module, the combination of which integrates metric learning with an anchor-free
Faster R-CNN-style detection pipeline, eventually eliminating the need to
fine-tune on the support images. We also propose novel training strategies that
effectively improve detection performance. Extensive quantitative and
qualitative evaluations were performed and our method exceeds the
state-of-the-art one-shot performance consistently on multiple datasets.