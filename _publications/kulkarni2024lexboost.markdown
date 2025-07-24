---
layout: publication
title: 'Lexboost: Improving Lexical Document Retrieval With Nearest Neighbors'
authors: Hrishikesh Kulkarni, Nazli Goharian, Ophir Frieder, Sean Macavaney
conference: Proceedings of the ACM Symposium on Document Engineering 2024
year: 2024
bibkey: kulkarni2024lexboost
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.05882'}]
tags: ["Datasets", "Efficiency", "Graph Based ANN", "Hybrid ANN Methods", "Re-Ranking", "Text Retrieval"]
short_authors: Kulkarni et al.
---
Sparse retrieval methods like BM25 are based on lexical overlap, focusing on
the surface form of the terms that appear in the query and the document. The
use of inverted indices in these methods leads to high retrieval efficiency. On
the other hand, dense retrieval methods are based on learned dense vectors and,
consequently, are effective but comparatively slow. Since sparse and dense
methods approach problems differently and use complementary relevance signals,
approximation methods were proposed to balance effectiveness and efficiency.
For efficiency, approximation methods like HNSW are frequently used to
approximate exhaustive dense retrieval. However, approximation techniques still
exhibit considerably higher latency than sparse approaches. We propose LexBoost
that first builds a network of dense neighbors (a corpus graph) using a dense
retrieval approach while indexing. Then, during retrieval, we consider both a
document's lexical relevance scores and its neighbors' scores to rank the
documents. In LexBoost this remarkably simple application of the Cluster
Hypothesis contributes to stronger ranking effectiveness while contributing
little computational overhead (since the corpus graph is constructed offline).
The method is robust across the number of neighbors considered, various fusion
parameters for determining the scores, and different dataset construction
methods. We also show that re-ranking on top of LexBoost outperforms
traditional dense re-ranking and leads to results comparable with
higher-latency exhaustive dense retrieval.