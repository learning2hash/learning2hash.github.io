---
layout: publication
title: 'Few-shot Learning Meets Transformer: Unified Query-support Transformers For
  Few-shot Classification'
authors: Xixi Wang, Xiao Wang, Bo Jiang, Bin Luo
conference: IEEE Transactions on Circuits and Systems for Video Technology
year: 2023
bibkey: wang2022few
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.12398'}]
tags: []
short_authors: Wang et al.
---
Few-shot classification which aims to recognize unseen classes using very
limited samples has attracted more and more attention. Usually, it is
formulated as a metric learning problem. The core issue of few-shot
classification is how to learn (1) consistent representations for images in
both support and query sets and (2) effective metric learning for images
between support and query sets. In this paper, we show that the two challenges
can be well modeled simultaneously via a unified Query-Support TransFormer
(QSFormer) model. To be specific,the proposed QSFormer involves global
query-support sample Transformer (sampleFormer) branch and local patch
Transformer (patchFormer) learning branch. sampleFormer aims to capture the
dependence of samples in support and query sets for image representation. It
adopts the Encoder, Decoder and Cross-Attention to respectively model the
Support, Query (image) representation and Metric learning for few-shot
classification task. Also, as a complementary to global learning branch, we
adopt a local patch Transformer to extract structural representation for each
image sample by capturing the long-range dependence of local image patches. In
addition, a novel Cross-scale Interactive Feature Extractor (CIFE) is proposed
to extract and fuse multi-scale CNN features as an effective backbone module
for the proposed few-shot learning method. All modules are integrated into a
unified framework and trained in an end-to-end manner. Extensive experiments on
four popular datasets demonstrate the effectiveness and superiority of the
proposed QSFormer.