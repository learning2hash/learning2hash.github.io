---
layout: publication
title: 'LOH And Behold: Web-scale Visual Search, Recommendation And Clustering Using
  Locally Optimized Hashing'
authors: Yannis Kalantidis, Lyndon Kennedy, Huy Nguyen, Clayton Mellina, David A.
  Shamma
conference: Arxiv
year: 2016
citations: 3
bibkey: kalantidis2016loh
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.06480'}]
tags: [Hashing Methods, Quantization, ANN Search, Applications, Has Code]
---
We propose a novel hashing-based matching scheme, called Locally Optimized
Hashing (LOH), based on a state-of-the-art quantization algorithm that can be
used for efficient, large-scale search, recommendation, clustering, and
deduplication. We show that matching with LOH only requires set intersections
and summations to compute and so is easily implemented in generic distributed
computing systems. We further show application of LOH to: a) large-scale search
tasks where performance is on par with other state-of-the-art hashing
approaches; b) large-scale recommendation where queries consisting of thousands
of images can be used to generate accurate recommendations from collections of
hundreds of millions of images; and c) efficient clustering with a graph-based
algorithm that can be scaled to massive collections in a distributed
environment or can be used for deduplication for small collections, like search
results, performing better than traditional hashing approaches while only
requiring a few milliseconds to run. In this paper we experiment on datasets of
up to 100 million images, but in practice our system can scale to larger
collections and can be used for other types of data that have a vector
representation in a Euclidean space.