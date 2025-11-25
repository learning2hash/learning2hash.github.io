---
layout: publication
title: Binarized Johnson-lindenstrauss Embeddings
authors: Sjoerd Dirksen, Alexander Stollenwerk
conference: Arxiv
year: 2020
bibkey: dirksen2020binarized
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.08320'}]
tags: ["Distance Metric Learning", "Quantization"]
short_authors: Sjoerd Dirksen, Alexander Stollenwerk
---
We consider the problem of encoding a set of vectors into a minimal number of
bits while preserving information on their Euclidean geometry. We show that
this task can be accomplished by applying a Johnson-Lindenstrauss embedding and
subsequently binarizing each vector by comparing each entry of the vector to a
uniformly random threshold. Using this simple construction we produce two
encodings of a dataset such that one can query Euclidean information for a pair
of points using a small number of bit operations up to a desired additive error
- Euclidean distances in the first case and inner products and squared
Euclidean distances in the second. In the latter case, each point is encoded in
near-linear time. The number of bits required for these encodings is quantified
in terms of two natural complexity parameters of the dataset - its covering
numbers and localized Gaussian complexity - and shown to be near-optimal.