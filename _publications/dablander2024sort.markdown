---
layout: publication
title: 'Sort & Slice: A Simple And Superior Alternative To Hash-based Folding For
  Extended-connectivity Fingerprints'
authors: Markus Dablander, Thierry Hanser, Renaud Lambiotte, Garrett M. Morris
conference: Journal of Cheminformatics vol. 16 Article number 135 (2024)
year: 2024
bibkey: dablander2024sort
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.17954'}]
tags: []
short_authors: Dablander et al.
---
Extended-connectivity fingerprints (ECFPs) are a ubiquitous tool in current
cheminformatics and molecular machine learning, and one of the most prevalent
molecular feature extraction techniques used for chemical prediction. Atom
features learned by graph neural networks can be aggregated to compound-level
representations using a large spectrum of graph pooling methods; in contrast,
sets of detected ECFP substructures are by default transformed into bit vectors
using only a simple hash-based folding procedure. We introduce a general
mathematical framework for the vectorisation of structural fingerprints via a
formal operation called substructure pooling that encompasses hash-based
folding, algorithmic substructure-selection, and a wide variety of other
potential techniques. We go on to describe Sort & Slice, an easy-to-implement
and bit-collision-free alternative to hash-based folding for the pooling of
ECFP substructures. Sort & Slice first sorts ECFP substructures according to
their relative prevalence in a given set of training compounds and then slices
away all but the \(L\) most frequent substructures which are subsequently used to
generate a binary fingerprint of desired length, \(L\). We computationally
compare the performance of hash-based folding, Sort & Slice, and two advanced
supervised substructure-selection schemes (filtering and mutual-information
maximisation) for ECFP-based molecular property prediction. Our results
indicate that, despite its technical simplicity, Sort & Slice robustly (and at
times substantially) outperforms traditional hash-based folding as well as the
other investigated methods across prediction tasks, data splitting techniques,
machine-learning models and ECFP hyperparameters. We thus recommend that Sort &
Slice canonically replace hash-based folding as the default
substructure-pooling technique to vectorise ECFPs for supervised molecular
machine learning.