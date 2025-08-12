---
layout: publication
title: 'Quantized Indexing: Beyond Arithmetic Coding'
authors: Ratko V. Tomic
conference: Data Compression Conference (DCC'06)
year: 2006
bibkey: tomic2005quantized
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/cs/0511057'}]
tags: []
short_authors: Ratko V. Tomic
---
Quantized Indexing is a fast and space-efficient form of enumerative
(combinatorial) coding, the strongest among asymptotically optimal universal
entropy coding algorithms. The present advance in enumerative coding is similar
to that made by arithmetic coding with respect to its unlimited precision
predecessor, Elias coding. The arithmetic precision, execution time, table
sizes and coding delay are all reduced by a factor O(n) at a redundancy below
2*log(e)/2^g bits/symbol (for n input symbols and g-bit QI precision). Due to
its tighter enumeration, QI output redundancy is below that of arithmetic
coding (which can be derived as a lower accuracy approximation of QI). The
relative compression gain vanishes in large n and in high entropy limits and
increases for shorter outputs and for less predictable data. QI is
significantly faster than the fastest arithmetic coders, from factor 6 in high
entropy limit to over 100 in low entropy limit (`typically' 10-20 times
faster). These speedups are result of using only 3 adds, 1 shift and 2 array
lookups (all in 32 bit precision) per less probable symbol and no coding
operations for the most probable symbol . Further, the exact enumeration
algorithm is sharpened and its lattice walks formulation is generalized. A new
numeric type with a broader applicability, sliding window integer, is
introduced.