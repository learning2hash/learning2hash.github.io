---
layout: publication
title: Weakly Supervised Vision-and-language Pre-training With Relative Representations
authors: Chi Chen, Peng Li, Maosong Sun, Yang Liu
conference: 'Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2023
bibkey: chen2023weakly
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.15483'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Multimodal Retrieval", "Self-Supervised"]
short_authors: Chen et al.
---
Weakly supervised vision-and-language pre-training (WVLP), which learns
cross-modal representations with limited cross-modal supervision, has been
shown to effectively reduce the data cost of pre-training while maintaining
decent performance on downstream tasks. However, current WVLP methods use only
local descriptions of images, i.e., object tags, as cross-modal anchors to
construct weakly-aligned image-text pairs for pre-training. This affects the
data quality and thus the effectiveness of pre-training. In this paper, we
propose to directly take a small number of aligned image-text pairs as anchors,
and represent each unaligned image and text by its similarities to these
anchors, i.e., relative representations. We build a WVLP framework based on the
relative representations, namely RELIT, which collects high-quality
weakly-aligned image-text pairs from large-scale image-only and text-only data
for pre-training through relative representation-based retrieval and
generation. Experiments on four downstream tasks show that RELIT achieves new
state-of-the-art results under the weakly supervised setting.