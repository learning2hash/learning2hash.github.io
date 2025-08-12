---
layout: publication
title: Optimal Storage Codes On Graphs With Fixed Locality
authors: Sabyasachi Basu, Manuj Mukherjee
conference: Arxiv
year: 2023
bibkey: basu2023optimal
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.08680'}]
tags: ["Compact Codes", "Graph Based ANN", "Memory Efficiency"]
short_authors: Sabyasachi Basu, Manuj Mukherjee
---
Storage codes on graphs are an instance of *codes with locality*, which
are used in distributed storage schemes to provide local repairability.
Specifically, the nodes of the graph correspond to storage servers, and the
neighbourhood of each server constitute the set of servers it can query to
repair its stored data in the event of a failure. A storage code on a graph
with \(n\)-vertices is a set of \(n\)-length codewords over \(\field_q\) where the
\(i\)th codeword symbol is stored in server \(i\), and it can be recovered by
querying the neighbours of server \(i\) according to the underlying graph.
  In this work, we look at binary storage codes whose repair function is the
parity check, and characterise the tradeoff between the locality of the code
and its rate. Specifically, we show that the maximum rate of a code on \(n\)
vertices with locality \(r\) is bounded between \(1-1/n\lceil n/(r+1)\rceil\) and
\(1-1/n\lceil n/(r+1)\rceil\). The lower bound on the rate is derived by
constructing an explicit family of graphs with locality \(r\), while the upper
bound is obtained via a lower bound on the binary-field rank of a class of
symmetric binary matrices. Our upper bound on maximal rate of a storage code
matches the upper bound on the larger class of codes with locality derived by
Tamo and Barg. As a corollary to our result, we obtain the following asymptotic
separation result: given a sequence \(r(n), n\geq 1\), there exists a sequence of
graphs on \(n\)-vertices with storage codes of rate \(1-o(1)\) if and only if
\(r(n)=\omega(1)\).