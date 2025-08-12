---
layout: publication
title: Linear-time String Indexing And Analysis In Small Space
authors: "Djamal Belazzougui, Fabio Cunial, Juha K\xE4rkk\xE4inen, Veli M\xE4kinen"
conference: ACM Transactions on Algorithms
year: 2020
bibkey: belazzougui2016linear
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.06378'}]
tags: ["Scalability"]
short_authors: Belazzougui et al.
---
The field of succinct data structures has flourished over the last 16 years.
Starting from the compressed suffix array (CSA) by Grossi and Vitter (STOC
2000) and the FM-index by Ferragina and Manzini (FOCS 2000), a number of
generalizations and applications of string indexes based on the Burrows-Wheeler
transform (BWT) have been developed, all taking an amount of space that is
close to the input size in bits. In many large-scale applications, the
construction of the index and its usage need to be considered as one unit of
computation. Efficient string indexing and analysis in small space lies also at
the core of a number of primitives in the data-intensive field of
high-throughput DNA sequencing. We report the following advances in string
indexing and analysis. We show that the BWT of a string \\(T\in
\\{1,\ldots,\sigma\\}^n\\) can be built in deterministic \\(O(n)\\) time using just
\\(O(nlog\{\sigma\})\\) bits of space, where \\(\sigma \leq n\\). Within the same time
and space budget, we can build an index based on the BWT that allows one to
enumerate all the internal nodes of the suffix tree of \\(T\\). Many fundamental
string analysis problems can be mapped to such enumeration, and can thus be
solved in deterministic \\(O(n)\\) time and in \\(O(nlog\{\sigma\})\\) bits of space
from the input string. We also show how to build many of the existing indexes
based on the BWT, such as the CSA, the compressed suffix tree (CST), and the
bidirectional BWT index, in randomized \\(O(n)\\) time and in \\(O(nlog\{\sigma\})\\)
bits of space. The previously fastest construction algorithms for BWT, CSA and
CST, which used \\(O(nlog\{\sigma\})\\) bits of space, took \\(O(nlog\{log\{\sigma\}\})\\)
time for the first two structures, and \\(O(nlog^\{\epsilon\}n)\\) time for the
third, where \\(\epsilon\\) is any positive constant. Contrary to the state of the
art, our bidirectional BWT index supports every operation in constant time per
element in its output.