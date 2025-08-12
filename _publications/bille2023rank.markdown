---
layout: publication
title: Rank And Select On Degenerate Strings
authors: "Philip Bille, Inge Li G\xF8rtz, Tord Stordalen"
conference: 2024 Data Compression Conference (DCC)
year: 2024
bibkey: bille2023rank
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.19702'}]
tags: ["Efficiency"]
short_authors: "Philip Bille, Inge Li G\xF8rtz, Tord Stordalen"
---
A 'degenerate string' is a sequence of subsets of some alphabet; it
represents any string obtainable by selecting one character from each set from
left to right. Recently, Alanko et al. generalized the rank-select problem to
degenerate strings, where given a character \\(c\\) and position \\(i\\) the goal is to
find either the \\(i\\)th set containing \\(c\\) or the number of occurrences of \\(c\\) in
the first \\(i\\) sets [SEA 2023]. The problem has applications to pangenomics; in
another work by Alanko et al. they use it as the basis for a compact
representation of 'de Bruijn Graphs' that supports fast membership queries.
  In this paper we revisit the rank-select problem on degenerate strings,
introducing a new, natural parameter and reanalyzing existing reductions to
rank-select on regular strings. Plugging in standard data structures, the time
bounds for queries are improved exponentially while essentially matching, or
improving, the space bounds. Furthermore, we provide a lower bound on space
that shows that the reductions lead to succinct data structures in a wide range
of cases. Finally, we provide implementations; our most compact structure
matches the space of the most compact structure of Alanko et al. while
answering queries twice as fast. We also provide an implementation using modern
vector processing features; it uses less than one percent more space than the
most compact structure of Alanko et al. while supporting queries four to seven
times faster, and has competitive query time with all the remaining structures.