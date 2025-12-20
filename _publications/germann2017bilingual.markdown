---
layout: publication
title: Bilingual Document Alignment With Latent Semantic Indexing
authors: Ulrich Germann
conference: Arxiv
year: 2017
bibkey: germann2017bilingual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.09443'}]
tags: ["Distance Metric Learning", "Evaluation", "Text Retrieval"]
short_authors: Ulrich Germann
---
We apply cross-lingual Latent Semantic Indexing to the Bilingual Document
Alignment Task at WMT16. Reduced-rank singular value decomposition of a
bilingual term-document matrix derived from known English/French page pairs in
the training data allows us to map monolingual documents into a joint semantic
space. Two variants of cosine similarity between the vectors that place each
document into the joint semantic space are combined with a measure of string
similarity between corresponding URLs to produce 1:1 alignments of
English/French web pages in a variety of domains. The system achieves a recall
of ca. 88% if no in-domain data is used for building the latent semantic model,
and 93% if such data is included.
  Analysing the system's errors on the training data, we argue that evaluating
aligner performance based on exact URL matches under-estimates their true
performance and propose an alternative that is able to account for duplicates
and near-duplicates in the underlying data.