---
layout: publication
title: 'Freshdiskann: A Fast And Accurate Graph-based ANN Index For Streaming Similarity
  Search'
authors: Singh Aditi, Subramanya Suhas Jayaram, Krishnaswamy Ravishankar, Simhadri
  Harsha Vardhan
conference: Arxiv
year: 2021
bibkey: singh2021freshdiskann
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.09613'}]
tags: ["Efficiency", "Graph-based ANN", "Similarity Search", "Vector Indexing"]
short_authors: Singh et al.
---
Approximate nearest neighbor search (ANNS) is a fundamental building block in
information retrieval with graph-based indices being the current
state-of-the-art and widely used in the industry. Recent advances in
graph-based indices have made it possible to index and search billion-point
datasets with high recall and millisecond-level latency on a single commodity
machine with an SSD.
  However, existing graph algorithms for ANNS support only static indices that
cannot reflect real-time changes to the corpus required by many key real-world
scenarios (e.g. index of sentences in documents, email, or a news index). To
overcome this drawback, the current industry practice for manifesting updates
into such indices is to periodically re-build these indices, which can be
prohibitively expensive.
  In this paper, we present the first graph-based ANNS index that reflects
corpus updates into the index in real-time without compromising on search
performance. Using update rules for this index, we design FreshDiskANN, a
system that can index over a billion points on a workstation with an SSD and
limited memory, and support thousands of concurrent real-time inserts, deletes
and searches per second each, while retaining \\(>95%\\) 5-recall@5. This
represents a 5-10x reduction in the cost of maintaining freshness in indices
when compared to existing methods.