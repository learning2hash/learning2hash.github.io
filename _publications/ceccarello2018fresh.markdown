---
layout: publication
title: FRESH Frechet Similarity With Hashing
authors: Ceccarello Matteo, Driemel Anne, Silvestri Francesco
conference: Proc. of Algorithms and Data Structures Symposium
year: 2018
citations: 6
bibkey: ceccarello2018fresh
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1809.02350'}]
tags: [Independent, Efficiency and Optimization]
---
This paper studies the \\(r\\)-range search problem for curves under the
continuous Fr\'echet distance: given a dataset \\(S\\) of \\(n\\) polygonal curves and
a threshold \\(r>0\\), construct a data structure that, for any query curve \\(q\\),
efficiently returns all entries in \\(S\\) with distance at most \\(r\\) from \\(q\\). We
propose FRESH, an approximate and randomized approach for \\(r\\)-range search,
that leverages on a locality sensitive hashing scheme for detecting candidate
near neighbors of the query curve, and on a subsequent pruning step based on a
cascade of curve simplifications. We experimentally compare \fresh to exact and
deterministic solutions, and we show that high performance can be reached by
suitably relaxing precision and recall.