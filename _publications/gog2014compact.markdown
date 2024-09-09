---
layout: publication
title: "Compact Indexes for Flexible Top-k Retrieval"
authors: Gog Simon, Petri Matthias
conference: Arxiv
year: 2014
bibkey: gog2014compact
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1406.3170"}
tags: ['ARXIV']
---
We engineer a self-index based retrieval system capable of rank-safe evaluation
of top-k queries. The framework generalizes the GREEDY approach of Culpepper et
al. (ESA 2010) to handle multi-term queries, including over phrases. We propose
two techniques which significantly reduce the ranking time for a wide range of
popular Information Retrieval (IR) relevance measures, such as TFxIDF and BM25.
First, we reorder elements in the document array according to document weight.
Second, we introduce the repetition array, which generalizes Sadakane's (JDA
2007) document frequency structure to document subsets. Combining document and
repetition array, we achieve attractive functionality-space trade-offs. We
provide an extensive evaluation of our system on terabyte-sized IR collections.
