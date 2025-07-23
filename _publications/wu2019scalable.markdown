---
layout: publication
title: Scalable Zero-shot Entity Linking With Dense Entity Retrieval
authors: Wu Ledell, Petroni Fabio, Josifoski Martin, Riedel Sebastian, Zettlemoyer
  Luke
conference: Proceedings of the 2020 Conference on Empirical Methods in Natural Language
  Processing (EMNLP)
year: 2020
bibkey: wu2019scalable
citations: 290
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1911.03814'}]
tags: ["EMNLP", "Evaluation", "Few-shot & Zero-shot", "Scalability"]
short_authors: Wu et al.
---
This paper introduces a conceptually simple, scalable, and highly effective
BERT-based entity linking model, along with an extensive evaluation of its
accuracy-speed trade-off. We present a two-stage zero-shot linking algorithm,
where each entity is defined only by a short textual description. The first
stage does retrieval in a dense space defined by a bi-encoder that
independently embeds the mention context and the entity descriptions. Each
candidate is then re-ranked with a cross-encoder, that concatenates the mention
and entity text. Experiments demonstrate that this approach is state of the art
on recent zero-shot benchmarks (6 point absolute gains) and also on more
established non-zero-shot evaluations (e.g. TACKBP-2010), despite its relative
simplicity (e.g. no explicit entity embeddings or manually engineered mention
tables). We also show that bi-encoder linking is very fast with nearest
neighbour search (e.g. linking with 5.9 million candidates in 2 milliseconds),
and that much of the accuracy gain from the more expensive cross-encoder can be
transferred to the bi-encoder via knowledge distillation. Our code and models
are available at https://github.com/facebookresearch/BLINK.