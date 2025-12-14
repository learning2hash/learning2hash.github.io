---
layout: publication
title: 'K-nearest Neighbors On Road Networks: A Journey In Experimentation And In-memory
  Implementation'
authors: Tenindra Abeywickrama, Muhammad Aamir Cheema, David Taniar
conference: Arxiv
year: 2016
bibkey: abeywickrama2016k
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.01549'}]
tags: [Distance Metric Learning, Evaluation]
short_authors: Tenindra Abeywickrama, Muhammad Aamir Cheema, David Taniar
---
A k nearest neighbor (kNN) query on road networks retrieves the k closest
points of interest (POIs) by their network distances from a given location.
Today, in the era of ubiquitous mobile computing, this is a highly pertinent
query. While Euclidean distance has been used as a heuristic to search for the
closest POIs by their road network distance, its efficacy has not been
thoroughly investigated. The most recent methods have shown significant
improvement in query performance. Earlier studies, which proposed disk-based
indexes, were compared to the current state-of-the-art in main memory. However,
recent studies have shown that main memory comparisons can be challenging and
require careful adaptation. This paper presents an extensive experimental
investigation in main memory to settle these and several other issues. We use
efficient and fair memory-resident implementations of each method to reproduce
past experiments and conduct additional comparisons for several overlooked
evaluations. Notably we revisit a previously discarded technique (IER) showing
that, through a simple improvement, it is often the best performing technique.