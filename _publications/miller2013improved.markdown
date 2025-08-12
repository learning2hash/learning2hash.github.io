---
layout: publication
title: Improved Parallel Algorithms For Spanners And Hopsets
authors: Gary L. Miller, Richard Peng, Adrian Vladu, Shen Chen Xu
conference: Proceedings of the 27th ACM symposium on Parallelism in Algorithms and
  Architectures
year: 2015
bibkey: miller2013improved
citations: 73
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1309.3545'}]
tags: []
short_authors: Miller et al.
---
We use exponential start time clustering to design faster and more
work-efficient parallel graph algorithms involving distances. Previous
algorithms usually rely on graph decomposition routines with strict
restrictions on the diameters of the decomposed pieces. We weaken these bounds
in favor of stronger local probabilistic guarantees. This allows more direct
analyses of the overall process, giving: * Linear work parallel algorithms that
construct spanners with \\(O(k)\\) stretch and size \\(O(n^\{1+1/k\})\\) in unweighted
graphs, and size \\(O(n^\{1+1/k\} log k)\\) in weighted graphs. * Hopsets that lead
to the first parallel algorithm for approximating shortest paths in undirected
graphs with \\(O(m\;\mathrm\{polylog\}\;n)\\) work.