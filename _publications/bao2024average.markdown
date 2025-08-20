---
layout: publication
title: Average-distortion Sketching
authors: Yiqiao Bao, Anubhav Baweja, Nicolas Menand, Erik Waingarten, Nathan White,
  Tian Zhang
conference: Arxiv
year: 2024
bibkey: bao2024average
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.05156'}]
tags: [Hashing Methods]
short_authors: Bao et al.
---
We introduce average-distortion sketching for metric spaces. As in
(worst-case) sketching, these algorithms compress points in a metric space
while approximately recovering pairwise distances. The novelty is studying
average-distortion: for any fixed (yet, arbitrary) distribution \(\mu\) over the
metric, the sketch should not over-estimate distances, and it should
(approximately) preserve the average distance with respect to draws from \(\mu\).
The notion generalizes average-distortion embeddings into \(\ell_1\) [Rabinovich
'03, Kush-Nikolov-Tang '21] as well as data-dependent locality-sensitive
hashing [Andoni-Razenshteyn '15, Andoni-Naor-Nikolov-et-al. '18], which have
been recently studied in the context of nearest neighbor search.
  \(\bullet\) For all \(p \in (2, \infty)\) and any \(c\) larger than a fixed
constant, we give an average-distortion sketch for \(([\Delta]^d, \ell_p)\) with
approximation \(c\) and bit-complexity \(\text\{poly\}(2^\{p/c\} \cdot
log(d\Delta))\), which is provably impossible in (worst-case) sketching.
  \(\bullet\) As an application, we improve on the approximation of
sublinear-time data structures for nearest neighbor search over \(\ell_p\) (for
large \(p > 2\)). The prior best approximation was \(O(p)\)
[Andoni-Naor-Nikolov-et-al. '18, Kush-Nikolov-Tang '21], and we show it can be
any \(c\) larger than a fixed constant (irrespective of \(p\)) by using
\(n^\{O(p/c)\}\) space.
  We give some evidence that \(2^\{Ω(p/c)\}\) space may be necessary by giving
a lower bound on average-distortion sketches which produce a certain
probabilistic certificate of farness (which our sketches crucially rely on).