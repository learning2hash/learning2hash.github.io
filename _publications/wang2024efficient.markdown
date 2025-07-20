---
layout: publication
title: Efficient Self-Supervised Video Hashing with Selective State Spaces
authors: Wang et al.
conference: Proceedings of the VLDB Endowment
year: 2024
bibkey: wang2024efficient
citations: 98
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.14518'}]
tags: [Self Supervised, Hashing Methods, Supervised]
---
Self-supervised video hashing (SSVH) is a practical task in video indexing
and retrieval. Although Transformers are predominant in SSVH for their
impressive temporal modeling capabilities, they often suffer from computational
and memory inefficiencies. Drawing inspiration from Mamba, an advanced
state-space model, we explore its potential in SSVH to achieve a better balance
between efficacy and efficiency. We introduce S5VH, a Mamba-based video hashing
model with an improved self-supervised learning paradigm. Specifically, we
design bidirectional Mamba layers for both the encoder and decoder, which are
effective and efficient in capturing temporal relationships thanks to the
data-dependent selective scanning mechanism with linear complexity. In our
learning strategy, we transform global semantics in the feature space into
semantically consistent and discriminative hash centers, followed by a center
alignment loss as a global learning signal. Our self-local-global (SLG)
paradigm significantly improves learning efficiency, leading to faster and
better convergence. Extensive experiments demonstrate S5VH's improvements over
state-of-the-art methods, superior transferability, and scalable advantages in
inference efficiency. Code is available at
https://github.com/gimpong/AAAI25-S5VH.