---
layout: publication
title: Parallel Construction Of Wavelet Trees On Multicore Architectures
authors: "Jos\xE9 Fuentes-Sep\xFAlveda, Erick Elejalde, Leo Ferres, Diego Seco"
conference: Knowledge and Information Systems
year: 2016
bibkey: "fuentessep\xFAlveda2016parallel"
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.05994'}]
tags: ["Efficiency"]
short_authors: "Fuentes-Sep\xFAlveda et al."
---
The wavelet tree has become a very useful data structure to efficiently
represent and query large volumes of data in many different domains, from
bioinformatics to geographic information systems. One problem with wavelet
trees is their construction time. In this paper, we introduce two algorithms
that reduce the time complexity of a wavelet tree's construction by taking
advantage of nowadays ubiquitous multicore machines.
  Our first algorithm constructs all the levels of the wavelet in parallel in
\(O(n)\) time and \(O(n\lg\sigma + \sigma\lg n)\) bits of working space, where \(n\)
is the size of the input sequence and \(\sigma\) is the size of the alphabet. Our
second algorithm constructs the wavelet tree in a domain-decomposition fashion,
using our first algorithm in each segment, reaching \(O(\lg n)\) time and
\(O(n\lg\sigma + p\sigma\lg n/\lg\sigma)\) bits of extra space, where \(p\) is the
number of available cores. Both algorithms are practical and report good
speedup for large real datasets.