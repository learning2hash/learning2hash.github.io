---
layout: publication
title: 'Are Nearby Neighbors Relatives?: Testing Deep Music Embeddings'
authors: "Jaehun Kim, Juli\xE1n Urbano, Cynthia C. S. Liem, Alan Hanjalic"
conference: Frontiers in Applied Mathematics and Statistics
year: 2019
bibkey: kim2019are
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.07154'}]
tags: ["Evaluation"]
short_authors: Kim et al.
---
Deep neural networks have frequently been used to directly learn
representations useful for a given task from raw input data. In terms of
overall performance metrics, machine learning solutions employing deep
representations frequently have been reported to greatly outperform those using
hand-crafted feature representations. At the same time, they may pick up on
aspects that are predominant in the data, yet not actually meaningful or
interpretable. In this paper, we therefore propose a systematic way to test the
trustworthiness of deep music representations, considering musical semantics.
The underlying assumption is that in case a deep representation is to be
trusted, distance consistency between known related points should be maintained
both in the input audio space and corresponding latent deep space. We generate
known related points through semantically meaningful transformations, both
considering imperceptible and graver transformations. Then, we examine within-
and between-space distance consistencies, both considering audio space and
latent embedded space, the latter either being a result of a conventional
feature extractor or a deep encoder. We illustrate how our method, as a
complement to task-specific performance, provides interpretable insight into
what a network may have captured from training data signals.