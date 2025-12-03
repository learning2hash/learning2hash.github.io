---
layout: publication
title: On The Adversarial Robustness Of Locality-sensitive Hashing In Hamming Space
authors: Michael Kapralov, Mikhail Makarov, Christian Sohler
conference: Arxiv
year: 2024
bibkey: kapralov2024on
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.09707'}]
tags: ["Datasets", "Hashing Methods", "Locality-Sensitive-Hashing", "Robustness"]
short_authors: Michael Kapralov, Mikhail Makarov, Christian Sohler
---
Locality-sensitive hashing~[Indyk,Motwani'98] is a classical data structure
for approximate nearest neighbor search. It allows, after a close to linear
time preprocessing of the input dataset, to find an approximately nearest
neighbor of any fixed query in sublinear time in the dataset size. The
resulting data structure is randomized and succeeds with high probability for
every fixed query.
  In many modern applications of nearest neighbor search the queries are chosen
adaptively. In this paper, we study the robustness of the locality-sensitive
hashing to adaptive queries in Hamming space. We present a simple adversary
that can, under mild assumptions on the initial point set, provably find a
query to the approximate near neighbor search data structure that the data
structure fails on. Crucially, our adaptive algorithm finds the hard query
exponentially faster than random sampling.