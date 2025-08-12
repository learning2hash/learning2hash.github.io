---
layout: publication
title: Incorporating Feature Pyramid Tokenization And Open Vocabulary Semantic Segmentation
authors: Jianyu Zhang, Li Zhang, Shijian Li
conference: Arxiv
year: 2024
bibkey: zhang2024incorporating
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.14145'}]
tags: []
short_authors: Jianyu Zhang, Li Zhang, Shijian Li
---
The visual understanding are often approached from 3 granular levels: image,
patch and pixel. Visual Tokenization, trained by self-supervised reconstructive
learning, compresses visual data by codebook in patch-level with marginal
information loss, but the visual tokens does not have semantic meaning. Open
Vocabulary semantic segmentation benefits from the evolving Vision-Language
models (VLMs) with strong image zero-shot capability, but transferring
image-level to pixel-level understanding remains an imminent challenge. In this
paper, we treat segmentation as tokenizing pixels and study a united perceptual
and semantic token compression for all granular understanding and consequently
facilitate open vocabulary semantic segmentation. Referring to the cognitive
process of pretrained VLM where the low-level features are progressively
composed to high-level semantics, we propose Feature Pyramid Tokenization (PAT)
to cluster and represent multi-resolution feature by learnable codebooks and
then decode them by joint learning pixel reconstruction and semantic
segmentation. We design loosely coupled pixel and semantic learning branches.
The pixel branch simulates bottom-up composition and top-down visualization of
codebook tokens, while the semantic branch collectively fuse hierarchical
codebooks as auxiliary segmentation guidance. Our experiments show that PAT
enhances the semantic intuition of VLM feature pyramid, improves performance
over the baseline segmentation model and achieves competitive performance on
open vocabulary semantic segmentation benchmark. Our model is
parameter-efficient for VLM integration and flexible for the independent
tokenization. We hope to give inspiration not only on improving segmentation
but also on semantic visual token utilization.