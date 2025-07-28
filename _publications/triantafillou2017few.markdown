---
layout: publication
title: Few-shot Learning Through An Information Retrieval Lens
authors: Eleni Triantafillou, Richard Zemel, Raquel Urtasun
conference: Arxiv
year: 2017
bibkey: triantafillou2017few
citations: 111
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.02610'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Eleni Triantafillou, Richard Zemel, Raquel Urtasun
---
Few-shot learning refers to understanding new concepts from only a few
examples. We propose an information retrieval-inspired approach for this
problem that is motivated by the increased importance of maximally leveraging
all the available information in this low-data regime. We define a training
objective that aims to extract as much information as possible from each
training batch by effectively optimizing over all relative orderings of the
batch points simultaneously. In particular, we view each batch point as a
`query' that ranks the remaining ones based on its predicted relevance to them
and we define a model within the framework of structured prediction to optimize
mean Average Precision over these rankings. Our method achieves impressive
results on the standard few-shot classification benchmarks while is also
capable of few-shot retrieval.