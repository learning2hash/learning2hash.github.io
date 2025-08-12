---
layout: publication
title: Reducing The Footprint Of Multi-vector Retrieval With Minimal Performance Impact
  Via Token Pooling
authors: "Benjamin Clavi\xE9, Antoine Chaffin, Griffin Adams"
conference: Arxiv
year: 2024
bibkey: "clavi\xE92024reducing"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.14683'}]
tags: []
short_authors: "Benjamin Clavi\xE9, Antoine Chaffin, Griffin Adams"
---
Over the last few years, multi-vector retrieval methods, spearheaded by
ColBERT, have become an increasingly popular approach to Neural IR. By storing
representations at the token level rather than at the document level, these
methods have demonstrated very strong retrieval performance, especially in
out-of-domain settings. However, the storage and memory requirements necessary
to store the large number of associated vectors remain an important drawback,
hindering practical adoption. In this paper, we introduce a simple
clustering-based token pooling approach to aggressively reduce the number of
vectors that need to be stored. This method can reduce the space & memory
footprint of ColBERT indexes by 50% with virtually no retrieval performance
degradation. This method also allows for further reductions, reducing the
vector count by 66%-to-75% , with degradation remaining below 5% on a vast
majority of datasets. Importantly, this approach requires no architectural
change nor query-time processing, and can be used as a simple drop-in during
indexation with any ColBERT-like model.