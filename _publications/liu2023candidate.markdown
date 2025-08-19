---
layout: publication
title: Candidate Set Re-ranking For Composed Image Retrieval With Dual Multi-modal
  Encoder
authors: Zheyuan Liu, Weixuan Sun, Damien Teney, Stephen Gould
conference: Arxiv
year: 2023
bibkey: liu2023candidate
citations: 4
additional_links: [{name: Code, url: 'https://github.com/Cuberick-Orion/Candidate-Reranking-CIR.'},
  {name: Paper, url: 'https://arxiv.org/abs/2305.16304'}]
tags: [Scalability, Datasets, Hybrid ANN Methods, Re-ranking, Image Retrieval]
short_authors: Liu et al.
---
Composed image retrieval aims to find an image that best matches a given
multi-modal user query consisting of a reference image and text pair. Existing
methods commonly pre-compute image embeddings over the entire corpus and
compare these to a reference image embedding modified by the query text at test
time. Such a pipeline is very efficient at test time since fast vector
distances can be used to evaluate candidates, but modifying the reference image
embedding guided only by a short textual description can be difficult,
especially independent of potential candidates. An alternative approach is to
allow interactions between the query and every possible candidate, i.e.,
reference-text-candidate triplets, and pick the best from the entire set.
Though this approach is more discriminative, for large-scale datasets the
computational cost is prohibitive since pre-computation of candidate embeddings
is no longer possible. We propose to combine the merits of both schemes using a
two-stage model. Our first stage adopts the conventional vector distancing
metric and performs a fast pruning among candidates. Meanwhile, our second
stage employs a dual-encoder architecture, which effectively attends to the
input triplet of reference-text-candidate and re-ranks the candidates. Both
stages utilize a vision-and-language pre-trained network, which has proven
beneficial for various downstream tasks. Our method consistently outperforms
state-of-the-art approaches on standard benchmarks for the task. Our
implementation is available at
https://github.com/Cuberick-Orion/Candidate-Reranking-CIR.