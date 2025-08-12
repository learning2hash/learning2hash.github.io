---
layout: publication
title: Towards The Locality Of Vizing's Theorem
authors: Hsin-Hao Su, Hoa T. Vu
conference: Arxiv
year: 2019
bibkey: su2019towards
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1901.00479'}]
tags: []
short_authors: Hsin-Hao Su, Hoa T. Vu
---
Vizing showed that it suffices to color the edges of a simple graph using
\(\Delta + 1\) colors, where \(\Delta\) is the maximum degree of the graph.
However, up to this date, no efficient distributed edge-coloring algorithms are
known for obtaining such a coloring, even for constant degree graphs. The
current algorithms that get closest to this number of colors are the randomized
\((\Delta + \tilde\{\Theta\}(\sqrt\{\Delta\}))\)-edge-coloring algorithm that runs in
\(\text\{polylog\}(n)\) rounds by Chang et al. (SODA '18) and the deterministic
\((\Delta + \text\{polylog\}(n))\)-edge-coloring algorithm that runs in
\(\text\{poly\}(\Delta, log n)\) rounds by Ghaffari et al. (STOC '18).
  We present two distributed edge-coloring algorithms that run in
\(\text\{poly\}(\Delta,log n)\) rounds. The first algorithm, with randomization,
uses only \(\Delta+2\) colors. The second algorithm is a deterministic algorithm
that uses \(\Delta+ O(log n/ log log n)\) colors. Our approach is to reduce
the distributed edge-coloring problem into an online, restricted version of
balls-into-bins problem. If \(\ell\) is the maximum load of the bins, our
algorithm uses \(\Delta + 2\ell - 1\) colors. We show how to achieve \(\ell = 1\)
with randomization and \(\ell = O(log n / log log n)\) without randomization.