---
layout: publication
title: Incremental Sparse TFIDF Incremental Similarity With Bipartite Graphs
authors: Sarmento Rui Portocarrero, Brazdil Pavel
conference: "Arxiv"
year: 2018
bibkey: sarmento2018incremental
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1811.11746"}
tags: ['ARXIV', 'Graph']
---
In this report we experimented with several concepts regarding text streams analysis. We tested an implementation of Incremental Sparse TF-IDF (IS-TFIDF) and Incremental Cosine Similarity (ICS) with the use of bipartite graphs. We are using bipartite graphs - one type of node are documents and the other type of nodes are words - to know what documents are affected with a word arrival at the stream (the neighbors of the word in the graph). Thus with this information we leverage optimized algorithms used for graph-based applications. The concept is similar to for example the use of hash tables or other computer science concepts used for fast access to information in memory.
