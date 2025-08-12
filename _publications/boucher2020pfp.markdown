---
layout: publication
title: PFP Data Structures
authors: "Christina Boucher, Ond\u0159ej Cvacho, Travis Gagie, Jan Holub, Giovanni\
  \ Manzini, Gonzalo Navarro, Massimiliano Rossi"
conference: Arxiv
year: 2020
bibkey: boucher2020pfp
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.11687'}]
tags: ["Datasets"]
short_authors: Boucher et al.
---
Prefix-free parsing (PFP) was introduced by Boucher et al. (2019) as a
preprocessing step to ease the computation of Burrows-Wheeler Transforms (BWTs)
of genomic databases. Given a string \(S\), it produces a dictionary \(D\) and a
parse \(P\) of overlapping phrases such that \(\mathrm\{BWT\} (S)\) can be computed
from \(D\) and \(P\) in time and workspace bounded in terms of their combined size
\(|\mathrm\{PFP\} (S)|\). In practice \(D\) and \(P\) are significantly smaller than
\(S\) and computing \(\mathrm\{BWT\} (S)\) from them is more efficient than computing
it from \(S\) directly, at least when \(S\) consists of genomes from individuals of
the same species. In this paper, we consider \(\mathrm\{PFP\} (S)\) as a \{\em data
structure\} and show how it can be augmented to support the following queries
quickly, still in \(O (|\mathrm\{PFP\} (S)|)\) space: longest common extension
(LCE), suffix array (SA), longest common prefix (LCP) and BWT. Lastly, we
provide experimental evidence that the PFP data structure can be efficiently
constructed for very large repetitive datasets: it takes one hour and 54 GB
peak memory for \(1000\) variants of human chromosome 19, initially occupying
roughly 56 GB.