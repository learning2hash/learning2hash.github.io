---
layout: publication
title: Leveraging Decoder Architectures For Learned Sparse Retrieval
authors: Jingfen Qiao, Thong Nguyen, Evangelos Kanoulas, Andrew Yates
conference: Lecture Notes in Computer Science
year: 2025
bibkey: qiao2025leveraging
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.18151'}]
tags: [Scalability, Evaluation, Few-shot & Zero-shot]
short_authors: Qiao et al.
---
Learned Sparse Retrieval (LSR) has traditionally focused on small-scale
encoder-only transformer architectures. With the advent of large-scale
pre-trained language models, their capability to generate sparse
representations for retrieval tasks across different transformer-based
architectures, including encoder-only, decoder-only, and encoder-decoder
models, remains largely unexplored. This study investigates the effectiveness
of LSR across these architectures, exploring various sparse representation
heads and model scales. Our results highlight the limitations of using large
language models to create effective sparse representations in zero-shot
settings, identifying challenges such as inappropriate term expansions and
reduced performance due to the lack of expansion. We find that the
encoder-decoder architecture with multi-tokens decoding approach achieves the
best performance among the three backbones. While the decoder-only model
performs worse than the encoder-only model, it demonstrates the potential to
outperform when scaled to a high number of parameters.