---
layout: publication
title: 'S2SD: Simultaneous Similarity-based Self-distillation For Deep Metric Learning'
authors: "Karsten Roth, Timo Milbich, Bj\xF6rn Ommer, Joseph Paul Cohen, Marzyeh Ghassemi"
conference: Arxiv
year: 2020
bibkey: roth2020s2sd
citations: 4
additional_links: [{name: Code, url: 'https://github.com/MLforHealth/S2SD'}, {name: Paper,
    url: 'https://arxiv.org/abs/2009.08348'}]
tags: [Evaluation, Distance Metric Learning, Few-shot & Zero-shot]
short_authors: Roth et al.
---
Deep Metric Learning (DML) provides a crucial tool for visual similarity and
zero-shot applications by learning generalizing embedding spaces, although
recent work in DML has shown strong performance saturation across training
objectives. However, generalization capacity is known to scale with the
embedding space dimensionality. Unfortunately, high dimensional embeddings also
create higher retrieval cost for downstream applications. To remedy this, we
propose \emph\{Simultaneous Similarity-based Self-distillation (S2SD). S2SD
extends DML with knowledge distillation from auxiliary, high-dimensional
embedding and feature spaces to leverage complementary context during training
while retaining test-time cost and with negligible changes to the training
time. Experiments and ablations across different objectives and standard
benchmarks show S2SD offers notable improvements of up to 7% in Recall@1, while
also setting a new state-of-the-art. Code available at
https://github.com/MLforHealth/S2SD.