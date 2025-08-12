---
layout: publication
title: Enhanced Graph Pattern Matching
authors: Nicola Cotumaccio
conference: Arxiv
year: 2024
bibkey: cotumaccio2024enhanced
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.16205'}]
tags: ["Graph Based ANN"]
short_authors: Nicola Cotumaccio
---
Pattern matching queries on strings can be solved in linear time by
Knuth-Morris-Pratt (KMP) algorithm. In 1973, Weiner introduced the suffix tree
of a string [FOCS 1973] and showed that the seemingly more difficult problem of
computing matching statistics can also be solved in liner time. Pattern
matching queries on graphs are inherently more difficult: under the Orthogonal
Vector hypothesis, the graph pattern matching problem cannot be solved in
subquadratic time [TALG 2023]. The complexity of graph pattern matching can be
parameterized by the topological complexity of the considered graph, which is
captured by a parameter \( p \) [JACM 2023].
  In this paper, we show that, as in the string setting, computing matching
statistics on graph is as difficult as solving standard pattern matching
queries. To this end, we introduce a notion of longest common prefix (LCP)
array for arbitrary graphs.