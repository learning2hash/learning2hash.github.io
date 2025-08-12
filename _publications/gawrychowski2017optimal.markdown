---
layout: publication
title: Optimal Trade-offs For Pattern Matching With \(k\) Mismatches
authors: "Pawe\u0142 Gawrychowski, Przemys\u0142aw Uzna\u0144ski"
conference: Arxiv
year: 2017
bibkey: gawrychowski2017optimal
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.01311'}]
tags: ["Efficiency"]
short_authors: "Pawe\u0142 Gawrychowski, Przemys\u0142aw Uzna\u0144ski"
---
Given a pattern of length \(m\) and a text of length \(n\), the goal in
\(k\)-mismatch pattern matching is to compute, for every \(m\)-substring of the
text, the exact Hamming distance to the pattern or report that it exceeds \(k\).
This can be solved in either \(\widetilde\{O\}(n \sqrt\{k\})\) time as shown by Amir
et al. [J. Algorithms 2004] or \(\widetilde\{O\}((m + k^2) \cdot n/m)\) time due to
a result of Clifford et al. [SODA 2016]. We provide a smooth time trade-off
between these two bounds by designing an algorithm working in time
\(\widetilde\{O\}( (m + k \sqrt\{m\}) \cdot n/m)\). We complement this with a
matching conditional lower bound, showing that a significantly faster
combinatorial algorithm is not possible, unless the combinatorial matrix
multiplication conjecture fails.