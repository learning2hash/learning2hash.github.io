---
layout: publication
title: Searching Dense Representations With Inverted Indexes
authors: Jimmy Lin, Tommaso Teofili
conference: Arxiv
year: 2023
bibkey: lin2023searching
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.01556'}]
tags: [Evaluation, Graph-based ANN, Datasets]
short_authors: Jimmy Lin, Tommaso Teofili
---
Nearly all implementations of top-\(k\) retrieval with dense vector
representations today take advantage of hierarchical navigable small-world
network (HNSW) indexes. However, the generation of vector representations and
efficiently searching large collections of vectors are distinct challenges that
can be decoupled. In this work, we explore the contrarian approach of
performing top-\(k\) retrieval on dense vector representations using inverted
indexes. We present experiments on the MS MARCO passage ranking dataset,
evaluating three dimensions of interest: output quality, speed, and index size.
Results show that searching dense representations using inverted indexes is
possible. Our approach exhibits reasonable effectiveness with compact indexes,
but is impractically slow. Thus, while workable, our solution does not provide
a compelling tradeoff and is perhaps best characterized today as a "technical
curiosity".