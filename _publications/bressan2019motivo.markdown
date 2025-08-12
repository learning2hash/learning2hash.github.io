---
layout: publication
title: 'Motivo: Fast Motif Counting Via Succinct Color Coding And Adaptive Sampling'
authors: Marco Bressan, Stefano Leucci, Alessandro Panconesi
conference: Arxiv
year: 2019
bibkey: bressan2019motivo
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.01599'}]
tags: ["Memory Efficiency", "Tools & Libraries"]
short_authors: Marco Bressan, Stefano Leucci, Alessandro Panconesi
---
The randomized technique of color coding is behind state-of-the-art
algorithms for estimating graph motif counts. Those algorithms, however, are
not yet capable of scaling well to very large graphs with billions of edges. In
this paper we develop novel tools for the `motif counting via color coding'
framework. As a result, our new algorithm, Motivo, is able to scale well to
larger graphs while at the same time provide more accurate graphlet counts than
ever before. This is achieved thanks to two types of improvements. First, we
design new succinct data structures that support fast common color coding
operations, and a biased coloring trick that trades accuracy versus running
time and memory usage. These adaptations drastically reduce the time and memory
requirements of color coding. Second, we develop an adaptive graphlet sampling
strategy, based on a fractional set cover problem, that breaks the additive
approximation barrier of standard sampling. This strategy gives multiplicative
approximations for all graphlets at once, allowing us to count not only the
most frequent graphlets but also extremely rare ones.
  To give an idea of the improvements, in \(40\) minutes Motivo counts \(7\)-nodes
motifs on a graph with \(65\)M nodes and \(1.8\)B edges; this is \(30\) and \(500\)
times larger than the state of the art, respectively in terms of nodes and
edges. On the accuracy side, in one hour Motivo produces accurate counts of
\(\approx \! 10.000\) distinct \(8\)-node motifs on graphs where state-of-the-art
algorithms fail even to find the second most frequent motif. Our method
requires just a high-end desktop machine. These results show how color coding
can bring motif mining to the realm of truly massive graphs using only ordinary
hardware.