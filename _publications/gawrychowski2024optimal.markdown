---
layout: publication
title: Optimal Distance Labeling For Permutation Graphs
authors: "Pawe\u0142 Gawrychowski, Wojciech Janczewski"
conference: Arxiv
year: 2024
bibkey: gawrychowski2024optimal
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.12147'}]
tags: ["Distance Metric Learning", "Graph Based ANN"]
short_authors: "Pawe\u0142 Gawrychowski, Wojciech Janczewski"
---
A permutation graph is the intersection graph of a set of segments between
two parallel lines. In other words, they are defined by a permutation \(\pi\) on
\(n\) elements, such that \(u\) and \(v\) are adjacent if an only if \(u<v\) but
\(\pi(u)>\pi(v)\). We consider the problem of computing the distances in such a
graph in the setting of informative labeling schemes.
  The goal of such a scheme is to assign a short bitstring \(\ell(u)\) to every
vertex \(u\), such that the distance between \(u\) and \(v\) can be computed using
only \(\ell(u)\) and \(\ell(v)\), and no further knowledge about the whole graph
(other than that it is a permutation graph). This elegantly captures the
intuition that we would like our data structure to be distributed, and often
leads to interesting combinatorial challenges while trying to obtain lower and
upper bounds that match up to the lower-order terms.
  For distance labeling of permutation graphs on \(n\) vertices, Katz, Katz, and
Peleg [STACS 2000] showed how to construct labels consisting of
\(\mathcal\{O\}(log^\{2\} n)\) bits. Later, Bazzaro and Gavoille [Discret. Math.
309(11)] obtained an asymptotically optimal bounds by showing how to construct
labels consisting of \(9log\{n\}+\mathcal\{O\}(1)\) bits, and proving that
\(3log\{n\}-\mathcal\{O\}(log\{log\{n\}\})\) bits are necessary. This however leaves a
quite large gap between the known lower and upper bounds. We close this gap by
showing how to construct labels consisting of \(3log\{n\}+\mathcal\{O\}(loglog
n)\) bits.