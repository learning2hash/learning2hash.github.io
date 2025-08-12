---
layout: publication
title: Lcp-aware Parallel String Sorting
authors: Jonas Ellert, Johannes Fischer, Nodari Sitchinava
conference: Lecture Notes in Computer Science
year: 2020
bibkey: ellert2020lcp
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.02219'}]
tags: []
short_authors: Jonas Ellert, Johannes Fischer, Nodari Sitchinava
---
When lexicographically sorting strings, it is not always necessary to inspect
all symbols. For example, the lexicographical rank of "europar" amongst the
strings "eureka", "eurasia", and "excells" only depends on its so called
relevant prefix "euro". The distinguishing prefix size \(D\) of a set of strings
is the number of symbols that actually need to be inspected to establish the
lexicographical ordering of all strings. Efficient string sorters should be
\(D\)-aware, i.e. their complexity should depend on \(D\) rather than on the total
number \(N\) of all symbols in all strings. While there are many \(D\)-aware
sorters in the sequential setting, there appear to be no such results in the
PRAM model. We propose a framework yielding a \(D\)-aware modification of any
existing PRAM string sorter. The derived algorithms are work-optimal with
respect to their original counterpart: If the original algorithm requires
\(O(w(N))\) work, the derived one requires \(O(w(D))\) work. The execution time
increases only by a small factor that is logarithmic in the length of the
longest relevant prefix. Our framework universally works for deterministic and
randomized algorithms in all variations of the PRAM model, such that future
improvements in (\(D\)-unaware) parallel string sorting will directly result in
improvements in \(D\)-aware parallel string sorting.