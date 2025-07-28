---
layout: publication
title: The Curse Of Dense Low-dimensional Information Retrieval For Large Index Sizes
authors: Nils Reimers, Iryna Gurevych
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 2: Short Papers)'
year: 2021
bibkey: reimers2020curse
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.14210'}]
tags: ["Evaluation"]
short_authors: Nils Reimers, Iryna Gurevych
---
Information Retrieval using dense low-dimensional representations recently
became popular and showed out-performance to traditional sparse-representations
like BM25. However, no previous work investigated how dense representations
perform with large index sizes. We show theoretically and empirically that the
performance for dense representations decreases quicker than sparse
representations for increasing index sizes. In extreme cases, this can even
lead to a tipping point where at a certain index size sparse representations
outperform dense representations. We show that this behavior is tightly
connected to the number of dimensions of the representations: The lower the
dimension, the higher the chance for false positives, i.e. returning irrelevant
documents.