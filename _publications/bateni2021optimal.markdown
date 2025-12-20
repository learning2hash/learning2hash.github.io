---
layout: publication
title: Optimal Fully Dynamic \(k\)-centers Clustering
authors: Mohammadhossein Bateni, Hossein Esfandiari, Rajesh Jayaram, Vahab Mirrokni
conference: Arxiv
year: 2021
bibkey: bateni2021optimal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.07050'}]
tags: ["Hashing Methods", "Locality-Sensitive-Hashing"]
short_authors: Bateni et al.
---
We present the first algorithm for fully dynamic \(k\)-centers clustering in an
arbitrary metric space that maintains an optimal \(2+\epsilon\) approximation in
\(O(k \cdot \operatorname\{polylog\}(n,\Delta))\) amortized update time. Here, \(n\)
is an upper bound on the number of active points at any time, and \(\Delta\) is
the aspect ratio of the data. Previously, the best known amortized update time
was \(O(k^2\cdot \operatorname\{polylog\}(n,\Delta))\), and is due to Chan,
Gourqin, and Sozio. We demonstrate that the runtime of our algorithm is optimal
up to \(\operatorname\{polylog\}(n,\Delta)\) factors, even for insertion-only
streams, which closes the complexity of fully dynamic \(k\)-centers clustering.
In particular, we prove that any algorithm for \(k\)-clustering tasks in
arbitrary metric spaces, including \(k\)-means, \(k\)-medians, and \(k\)-centers,
must make at least \(Ω(n k)\) distance queries to achieve any non-trivial
approximation factor.
  Despite the lower bound for arbitrary metrics, we demonstrate that an update
time sublinear in \(k\) is possible for metric spaces which admit locally
sensitive hash functions (LSH). Namely, we demonstrate a black-box
transformation which takes a locally sensitive hash family for a metric space
and produces a faster fully dynamic \(k\)-centers algorithm for that space. In
particular, for a large class of metrics including Euclidean space, \(\ell_p\)
spaces, the Hamming Metric, and the Jaccard Metric, for any \(c > 1\), our
results yield a \(c(4+\epsilon)\) approximate \(k\)-centers solution in \(O(n^\{1/c\}
\cdot \operatorname\{polylog\}(n,\Delta))\) amortized update time, simultaneously
for all \(k \geq 1\). Previously, the only known comparable result was a \(O(c
log n)\) approximation for Euclidean space due to Schmidt and Sohler, running
in the same amortized update time.