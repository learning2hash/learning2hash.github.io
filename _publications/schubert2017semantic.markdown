---
layout: publication
title: Semantic Word Clouds With Background Corpus Normalization And T-distributed
  Stochastic Neighbor Embedding
authors: "Erich Schubert, Andreas Spitz, Michael Weiler, Johanna Gei\xDF, Michael\
  \ Gertz"
conference: Arxiv
year: 2017
bibkey: schubert2017semantic
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.03569'}]
tags: ["Evaluation"]
short_authors: Schubert et al.
---
Many word clouds provide no semantics to the word placement, but use a random
layout optimized solely for aesthetic purposes. We propose a novel approach to
model word significance and word affinity within a document, and in comparison
to a large background corpus. We demonstrate its usefulness for generating more
meaningful word clouds as a visual summary of a given document. We then select
keywords based on their significance and construct the word cloud based on the
derived affinity. Based on a modified t-distributed stochastic neighbor
embedding (t-SNE), we generate a semantic word placement. For words that
cooccur significantly, we include edges, and cluster the words according to
their cooccurrence. For this we designed a scalable and memory-efficient
sketch-based approach usable on commodity hardware to aggregate the required
corpus statistics needed for normalization, and for identifying keywords as
well as significant cooccurences. We empirically validate our approch using a
large Wikipedia corpus.