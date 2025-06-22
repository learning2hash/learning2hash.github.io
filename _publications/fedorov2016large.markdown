---
layout: publication
title: Large Scale Near-duplicate Image Retrieval Using Triples Of Adjacent Ranked
  Features (TARF) With Embedded Geometric Information
authors: Sergei Fedorov, Olga Kacher
conference: Arxiv
year: 2016
citations: 1
bibkey: fedorov2016large
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.06093'}]
tags: [Applications, Indexing]
---
Most approaches to large-scale image retrieval are based on the construction
of the inverted index of local image descriptors or visual words. A search in
such an index usually results in a large number of candidates. This list of
candidates is then re-ranked with the help of a geometric verification, using a
RANSAC algorithm, for example. In this paper we propose a feature
representation, which is built as a combination of three local descriptors. It
allows one to significantly decrease the number of false matches and to shorten
the list of candidates after the initial search in the inverted index. This
combination of local descriptors is both reproducible and highly
discriminative, and thus can be efficiently used for large-scale near-duplicate
image retrieval.