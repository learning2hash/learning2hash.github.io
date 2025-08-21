---
layout: publication
title: Labeled Nearest Neighbor Search And Metric Spanners Via Locality Sensitive
  Orderings
authors: Arnold Filtser
conference: Arxiv
year: 2022
bibkey: filtser2022labeled
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.11846'}]
tags: ["Uncategorized"]
short_authors: Arnold Filtser
---
Chan, Har-Peled, and Jones [SICOMP 2020] developed locality-sensitive
orderings (LSO) for Euclidean space. A \((\tau,\rho)\)-LSO is a collection
\(\Sigma\) of orderings such that for every \(x,y\in\mathbb\{R\}^d\) there is an
ordering \(\sigma\in\Sigma\), where all the points between \(x\) and \(y\) w.r.t.
\(\sigma\) are in the \(\rho\)-neighborhood of either \(x\) or \(y\). In essence, LSO
allow one to reduce problems to the \(1\)-dimensional line. Later, Filtser and Le
[STOC 2022] developed LSO's for doubling metrics, general metric spaces, and
minor free graphs. For Euclidean and doubling spaces, the number of orderings
in the LSO is exponential in the dimension, which made them mainly useful for
the low dimensional regime. In this paper, we develop new LSO's for Euclidean,
\(\ell_p\), and doubling spaces that allow us to trade larger stretch for a much
smaller number of orderings. We then use our new LSO's (as well as the previous
ones) to construct path reporting low hop spanners, fault tolerant spanners,
reliable spanners, and light spanners for different metric spaces. While many
nearest neighbor search (NNS) data structures were constructed for metric
spaces with implicit distance representations (where the distance between two
metric points can be computed using their names, e.g. Euclidean space), for
other spaces almost nothing is known. In this paper we initiate the study of
the labeled NNS problem, where one is allowed to artificially assign labels
(short names) to metric points. We use LSO's to construct efficient labeled NNS
data structures in this model.