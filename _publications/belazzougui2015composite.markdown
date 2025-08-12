---
layout: publication
title: Composite Repetition-aware Data Structures
authors: Djamal Belazzougui, Fabio Cunial, Travis Gagie, Nicola Prezza, Mathieu Raffinot
conference: Lecture Notes in Computer Science
year: 2015
bibkey: belazzougui2015composite
citations: 56
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1502.05937'}]
tags: []
short_authors: Belazzougui et al.
---
In highly repetitive strings, like collections of genomes from the same
species, distinct measures of repetition all grow sublinearly in the length of
the text, and indexes targeted to such strings typically depend only on one of
these measures. We describe two data structures whose size depends on multiple
measures of repetition at once, and that provide competitive tradeoffs between
the time for counting and reporting all the exact occurrences of a pattern, and
the space taken by the structure. The key component of our constructions is the
run-length encoded BWT (RLBWT), which takes space proportional to the number of
BWT runs: rather than augmenting RLBWT with suffix array samples, we combine it
with data structures from LZ77 indexes, which take space proportional to the
number of LZ77 factors, and with the compact directed acyclic word graph
(CDAWG), which takes space proportional to the number of extensions of maximal
repeats. The combination of CDAWG and RLBWT enables also a new representation
of the suffix tree, whose size depends again on the number of extensions of
maximal repeats, and that is powerful enough to support matching statistics and
constant-space traversal.