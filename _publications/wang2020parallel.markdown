---
layout: publication
title: A Parallel Batch-dynamic Data Structure For The Closest Pair Problem
authors: Yiqiu Wang, Shangdi Yu, Yan Gu, Julian Shun
conference: Arxiv
year: 2021
bibkey: wang2020parallel
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.02379'}]
tags: ["Efficiency"]
short_authors: Wang et al.
---
We propose a theoretically-efficient and practical parallel batch-dynamic
data structure for the closest pair problem. Our solution is based on a serial
dynamic closest pair data structure by Golin et al., and supports batches of
insertions and deletions in parallel. For a data set of size \\(n\\), our data
structure supports a batch of insertions or deletions of size \\(m\\) in
\\(O(m(1+log ((n+m)/m)))\\) expected work and \\(O(log (n+m)log^*(n+m))\\) depth
with high probability, and takes linear space. The key techniques for achieving
these bounds are a new work-efficient parallel batch-dynamic binary heap, and
careful management of the computation across sets of points to minimize work
and depth.
  We provide an optimized multicore implementation of our data structure using
dynamic hash tables, parallel heaps, and dynamic \\(k\\)-d trees. Our experiments
on a variety of synthetic and real-world data sets show that it achieves a
parallel speedup of up to 38.57x (15.10x on average) on 48 cores with
hyper-threading. In addition, we also implement and compare four parallel
algorithms for static closest pair problem, for which we are not aware of any
existing practical implementations. On 48 cores with hyper-threading, the
static algorithms achieve up to 51.45x (29.42x on average) speedup, and Rabin's
algorithm performs the best on average. Comparing our dynamic algorithm to the
fastest static algorithm, we find that it is advantageous to use the dynamic
algorithm for batch sizes of up to 20% of the data set. As far as we know, our
work is the first to experimentally evaluate parallel closest pair algorithms,
in both the static and the dynamic settings.