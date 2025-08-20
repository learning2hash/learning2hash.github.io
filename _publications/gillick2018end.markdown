---
layout: publication
title: End-to-end Retrieval In Continuous Space
authors: Daniel Gillick, Alessandro Presta, Gaurav Singh Tomar
conference: Arxiv
year: 2018
bibkey: gillick2018end
citations: 81
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1811.08008'}]
tags: [Evaluation, Datasets]
short_authors: Daniel Gillick, Alessandro Presta, Gaurav Singh Tomar
---
Most text-based information retrieval (IR) systems index objects by words or
phrases. These discrete systems have been augmented by models that use
embeddings to measure similarity in continuous space. But continuous-space
models are typically used just to re-rank the top candidates. We consider the
problem of end-to-end continuous retrieval, where standard approximate nearest
neighbor (ANN) search replaces the usual discrete inverted index, and rely
entirely on distances between learned embeddings. By training simple models
specifically for retrieval, with an appropriate model architecture, we improve
on a discrete baseline by 8% and 26% (MAP) on two similar-question retrieval
tasks. We also discuss the problem of evaluation for retrieval systems, and
show how to modify existing pairwise similarity datasets for this purpose.