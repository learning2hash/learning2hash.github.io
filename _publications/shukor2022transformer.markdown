---
layout: publication
title: Transformer Decoders with MultiModal Regularization for Cross-Modal Food Retrieval
authors: Shukor et al.
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2022
bibkey: shukor2022transformer
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.09730'}]
tags: [CVPR]
---
Cross-modal image-recipe retrieval has gained significant attention in recent
years. Most work focuses on improving cross-modal embeddings using unimodal
encoders, that allow for efficient retrieval in large-scale databases, leaving
aside cross-attention between modalities which is more computationally
expensive. We propose a new retrieval framework, T-Food (Transformer Decoders
with MultiModal Regularization for Cross-Modal Food Retrieval) that exploits
the interaction between modalities in a novel regularization scheme, while
using only unimodal encoders at test time for efficient retrieval. We also
capture the intra-dependencies between recipe entities with a dedicated recipe
encoder, and propose new variants of triplet losses with dynamic margins that
adapt to the difficulty of the task. Finally, we leverage the power of the
recent Vision and Language Pretraining (VLP) models such as CLIP for the image
encoder. Our approach outperforms existing approaches by a large margin on the
Recipe1M dataset. Specifically, we achieve absolute improvements of 8.1 % (72.6
R@1) and +10.9 % (44.6 R@1) on the 1k and 10k test sets respectively. The code
is available here:https://github.com/mshukor/TFood