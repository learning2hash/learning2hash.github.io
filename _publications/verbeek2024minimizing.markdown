---
layout: publication
title: Minimizing The Minimizers Via Alphabet Reordering
authors: Hilde Verbeek, Lorraine A. K. Ayad, Grigorios Loukides, Solon P. Pissis
conference: Arxiv
year: 2024
bibkey: verbeek2024minimizing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.04052'}]
tags: []
short_authors: Verbeek et al.
---
Minimizers sampling is one of the most widely-used mechanisms for sampling
strings [Roberts et al., Bioinformatics 2004]. Let \(S=S[1]\ldots S[n]\) be a
string over a totally ordered alphabet \(\Sigma\). Further let \(w\geq 2\) and
\(k\geq 1\) be two integers. The minimizer of \(S[i\mathinner\{.\,.\} i+w+k-2]\) is
the smallest position in \([i,i+w-1]\) where the lexicographically smallest
length-\(k\) substring of \(S[i\mathinner\{.\,.\} i+w+k-2]\) starts. The set of
minimizers over all \(i\in[1,n-w-k+2]\) is the set \(\mathcal\{M\}_\{w,k\}(S)\) of the
minimizers of \(S\). We consider the following basic problem: Given \(S\), \(w\), and
\(k\), can we efficiently compute a total order on \(\Sigma\) that minimizes
\(|\mathcal\{M\}_\{w,k\}(S)|\)? We show that this is unlikely by proving that the
problem is NP-hard for any \(w\geq 2\) and \(k\geq 1\). Our result provides
theoretical justification as to why there exist no exact algorithms for
minimizing the minimizers samples, while there exists a plethora of heuristics
for the same purpose.