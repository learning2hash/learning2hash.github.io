---
layout: publication
title: Dual-Stream Knowledge-Preserving Hashing for Unsupervised Video Retrieval
authors: Li et al.
conference: Lecture Notes in Computer Science
year: 2022
bibkey: li2022dual
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.08009'}]
tags: ["Hashing-Methods", "Unsupervised", "Supervised"]
---
Unsupervised video hashing usually optimizes binary codes by learning to
reconstruct input videos. Such reconstruction constraint spends much effort on
frame-level temporal context changes without focusing on video-level global
semantics that are more useful for retrieval. Hence, we address this problem by
decomposing video information into reconstruction-dependent and
semantic-dependent information, which disentangles the semantic extraction from
reconstruction constraint. Specifically, we first design a simple dual-stream
structure, including a temporal layer and a hash layer. Then, with the help of
semantic similarity knowledge obtained from self-supervision, the hash layer
learns to capture information for semantic retrieval, while the temporal layer
learns to capture the information for reconstruction. In this way, the model
naturally preserves the disentangled semantics into binary codes. Validated by
comprehensive experiments, our method consistently outperforms the
state-of-the-arts on three video benchmarks.