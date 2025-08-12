---
layout: publication
title: Sequential Transformer For End-to-end Person Search
authors: Long Chen, Jinhua Xu
conference: Lecture Notes in Computer Science
year: 2023
bibkey: chen2022sequential
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.04323'}]
tags: []
short_authors: Long Chen, Jinhua Xu
---
Person Search aims to simultaneously localize and recognize a target person
from realistic and uncropped gallery images. One major challenge of person
search comes from the contradictory goals of the two sub-tasks, i.e., person
detection focuses on finding the commonness of all persons so as to distinguish
persons from the background, while person re-identification (re-ID) focuses on
the differences among different persons. In this paper, we propose a novel
Sequential Transformer (SeqTR) for end-to-end person search to deal with this
challenge. Our SeqTR contains a detection transformer and a novel re-ID
transformer that sequentially addresses detection and re-ID tasks. The re-ID
transformer comprises the self-attention layer that utilizes contextual
information and the cross-attention layer that learns local fine-grained
discriminative features of the human body. Moreover, the re-ID transformer is
shared and supervised by multi-scale features to improve the robustness of
learned person representations. Extensive experiments on two widely-used person
search benchmarks, CUHK-SYSU and PRW, show that our proposed SeqTR not only
outperforms all existing person search methods with a 59.3% mAP on PRW but also
achieves comparable performance to the state-of-the-art results with an mAP of
94.8% on CUHK-SYSU.