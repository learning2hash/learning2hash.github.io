---
layout: publication
title: Parallel Nearest Neighbors In Low Dimensions With Batch Updates
authors: Magdalen Dobson, Guy Blelloch
conference: Arxiv
year: 2021
bibkey: dobson2021parallel
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.04182'}]
tags: ["Efficiency", "Evaluation", "Tree Based ANN"]
short_authors: Magdalen Dobson, Guy Blelloch
---
We present a set of parallel algorithms for computing exact k-nearest
neighbors in low dimensions. Many k-nearest neighbor algorithms use either a
kd-tree or the Morton ordering of the point set; our algorithms combine these
approaches using a data structure we call the \textit\{zd-tree\}. We show that
this combination is both theoretically efficient under common assumptions, and
fast in practice. For point sets of size \(n\) with bounded expansion constant
and bounded ratio, the zd-tree can be built in \(O(n)\) work with
\(O(n^\{\epsilon\})\) span for constant \(\epsilon<1\), and searching for the
\(k\)-nearest neighbors of a point takes expected \(O(klog k)\) time. We benchmark
our k-nearest neighbor algorithms against existing parallel k-nearest neighbor
algorithms, showing that our implementations are generally faster than the
state of the art as well as achieving 75x speedup on 144 hyperthreads.
Furthermore, the zd-tree supports parallel batch-dynamic insertions and
deletions; to our knowledge, it is the first k-nearest neighbor data structure
to support such updates. On point sets with bounded expansion constant and
bounded ratio, a batch-dynamic update of size \(k\) requires \(O(k log n/k)\) work
with \(O(k^\{\epsilon\} + \text\{polylog\}(n))\) span.