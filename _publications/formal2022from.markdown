---
layout: publication
title: 'From Distillation To Hard Negative Sampling: Making Sparse Neural IR Models
  More Effective'
authors: "Thibault Formal, Carlos Lassance, Benjamin Piwowarski, St\xE9phane Clinchant"
conference: Arxiv
year: 2022
bibkey: formal2022from
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.04733'}]
tags: [Few-shot & Zero-shot, Efficiency]
short_authors: Formal et al.
---
Neural retrievers based on dense representations combined with Approximate
Nearest Neighbors search have recently received a lot of attention, owing their
success to distillation and/or better sampling of examples for training --
while still relying on the same backbone architecture. In the meantime, sparse
representation learning fueled by traditional inverted indexing techniques has
seen a growing interest, inheriting from desirable IR priors such as explicit
lexical matching. While some architectural variants have been proposed, a
lesser effort has been put in the training of such models. In this work, we
build on SPLADE -- a sparse expansion-based retriever -- and show to which
extent it is able to benefit from the same training improvements as dense
models, by studying the effect of distillation, hard-negative mining as well as
the Pre-trained Language Model initialization. We furthermore study the link
between effectiveness and efficiency, on in-domain and zero-shot settings,
leading to state-of-the-art results in both scenarios for sufficiently
expressive models.