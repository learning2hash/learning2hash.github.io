---
layout: publication
title: The Curse of Dense Low-Dimensional Information Retrieval for Large Index Sizes
authors: Reimers Nils, Gurevych Iryna
conference: "Arxiv"
year: 2020
bibkey: reimers2020the
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2012.14210"}
tags: ['ARXIV', 'TIP']
---
Information Retrieval using dense low-dimensional representations recently became popular and showed out-performance to traditional sparse-representations like BM25. However, no previous work investigated how dense representations perform with large index sizes. We show theoretically and empirically that the performance for dense representations decreases quicker than sparse representations for increasing index sizes. In extreme cases, this can even lead to a tipping point where at a certain index size sparse representations outperform dense representations. We show that this behavior is tightly connected to the number of dimensions of the representations The lower the dimension, the higher the chance for false positives, i.e. returning irrelevant documents.
