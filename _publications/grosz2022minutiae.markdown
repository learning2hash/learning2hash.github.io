---
layout: publication
title: Minutiae-Guided Fingerprint Embeddings via Vision Transformers
authors: Grosz et al.
conference: Arxiv
year: 2022
bibkey: grosz2022minutiae
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.13994'}]
tags: []
---
Minutiae matching has long dominated the field of fingerprint recognition.
However, deep networks can be used to extract fixed-length embeddings from
fingerprints. To date, the few studies that have explored the use of CNN
architectures to extract such embeddings have shown extreme promise. Inspired
by these early works, we propose the first use of a Vision Transformer (ViT) to
learn a discriminative fixed-length fingerprint embedding. We further
demonstrate that by guiding the ViT to focus in on local, minutiae related
features, we can boost the recognition performance. Finally, we show that by
fusing embeddings learned by CNNs and ViTs we can reach near parity with a
commercial state-of-the-art (SOTA) matcher. In particular, we obtain a
TAR=94.23% @ FAR=0.1% on the NIST SD 302 public-domain dataset, compared to a
SOTA commercial matcher which obtains TAR=96.71% @ FAR=0.1%. Additionally, our
fixed-length embeddings can be matched orders of magnitude faster than the
commercial system (2.5 million matches/second compared to 50K matches/second).
We make our code and models publicly available to encourage further research on
this topic: https://github.com/tba.