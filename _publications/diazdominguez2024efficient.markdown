---
layout: publication
title: Efficient Terabyte-scale Text Compression Via Stable Local Consistency And
  Parallel Grammar Processing
authors: Diego Diaz-Dominguez
conference: Arxiv
year: 2024
bibkey: diazdominguez2024efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.12439'}]
tags: ["Compact Codes"]
short_authors: Diego Diaz-Dominguez
---
We present a highly parallelizable text compression algorithm that scales
efficiently to terabyte-sized datasets. Our method builds on locally consistent
grammars, a lightweight form of compression, combined with simple recompression
techniques to achieve further space reductions. Locally consistent grammar
algorithms are particularly suitable for scaling, as they need minimal
satellite information to compact the text. We introduce a novel concept to
enable parallelisation, stable local consistency. A grammar algorithm ALG is
stable, if for any pattern \(P\) occurring in a collection \(\mathcal\{T\}=\\{T_1,
T_2, \ldots, T_k\\}\), the instances \(ALG(T_1), ALG(T_2), \ldots, ALG(T_k)\)
independently produce cores for \(P\) with the same topology. In a locally
consistent grammar, the core of \(P\) is a subset of nodes and edges in
\(\mathcal\{T\}\)'s parse tree that remains the same in all the occurrences of \(P\).
This feature is important to achieve compression, but it only holds if ALG
synchronises the parsing of the strings, for instance, by defining a common set
of nonterminal symbols for them. Stability removes the need for synchronisation
during the parsing phase. Consequently, we can run \(ALG(T_1), ALG(T_2), \ldots,
ALG(T_k)\) fully in parallel and then merge the resulting grammars into a single
compressed output equivalent to \(ALG(\mathcal\{T\})\). We implemented our ideas
and tested them on massive datasets. Our results showed that our method could
process a diverse collection of bacterial genomes (7.9 TB) in around nine
hours, requiring 16 threads and 0.43 bits/symbol of working memory, producing a
compressed representation 85 times smaller than the original input.