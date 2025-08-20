---
layout: publication
title: Identity-aware Textual-visual Matching With Latent Co-attention
authors: Shuang Li, Tong Xiao, Hongsheng Li, Wei Yang, Xiaogang Wang
conference: 2017 IEEE International Conference on Computer Vision (ICCV)
year: 2017
bibkey: li2017identity
citations: 243
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.01988'}]
tags: [Tools & Libraries, Datasets, ICCV]
short_authors: Li et al.
---
Textual-visual matching aims at measuring similarities between sentence
descriptions and images. Most existing methods tackle this problem without
effectively utilizing identity-level annotations. In this paper, we propose an
identity-aware two-stage framework for the textual-visual matching problem. Our
stage-1 CNN-LSTM network learns to embed cross-modal features with a novel
Cross-Modal Cross-Entropy (CMCE) loss. The stage-1 network is able to
efficiently screen easy incorrect matchings and also provide initial training
point for the stage-2 training. The stage-2 CNN-LSTM network refines the
matching results with a latent co-attention mechanism. The spatial attention
relates each word with corresponding image regions while the latent semantic
attention aligns different sentence structures to make the matching results
more robust to sentence structure variations. Extensive experiments on three
datasets with identity-level annotations show that our framework outperforms
state-of-the-art approaches by large margins.