---
layout: publication
title: Massively Parallel Algorithms For \(b\)-matching
authors: "Mohsen Ghaffari, Christoph Grunau, Slobodan Mitrovi\u0107"
conference: Proceedings of the 34th ACM Symposium on Parallelism in Algorithms and
  Architectures
year: 2022
bibkey: ghaffari2022massively
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.07796'}]
tags: []
short_authors: "Mohsen Ghaffari, Christoph Grunau, Slobodan Mitrovi\u0107"
---
This paper presents an \(O(loglog \bar\{d\})\) round massively parallel
algorithm for \(1+\epsilon\) approximation of maximum weighted \(b\)-matchings,
using near-linear memory per machine. Here \(\bar\{d\}\) denotes the average degree
in the graph and \(\epsilon\) is an arbitrarily small positive constant. Recall
that \(b\)-matching is the natural and well-studied generalization of the
matching problem where different vertices are allowed to have multiple (and
differing number of) incident edges in the matching. Concretely, each vertex
\(v\) is given a positive integer budget \(b_v\) and it can have up to \(b_v\)
incident edges in the matching. Previously, there were known algorithms with
round complexity \(O(loglog n)\), or \(O(loglog \Delta)\) where \(\Delta\)
denotes maximum degree, for \(1+\epsilon\) approximation of weighted matching and
for maximal matching [Czumaj et al., STOC'18, Ghaffari et al. PODC'18; Assadi
et al. SODA'19; Behnezhad et al. FOCS'19; Gamlath et al. PODC'19], but these
algorithms do not extend to the more general \(b\)-matching problem.