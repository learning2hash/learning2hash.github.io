---
layout: publication
title: Distance-aware Private Set Intersection
authors: Anrin Chakraborti, Giulia Fanti, Michael K. Reiter
conference: Arxiv
year: 2021
bibkey: chakraborti2021distance
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.14737'}]
tags: ["Distance Metric Learning", "Privacy & Security"]
short_authors: Anrin Chakraborti, Giulia Fanti, Michael K. Reiter
---
Private set intersection (PSI) allows two mutually untrusting parties to
compute an intersection of their sets, without revealing information about
items that are not in the intersection. This work introduces a PSI variant
called distance-aware PSI (DA-PSI) for sets whose elements lie in a metric
space. DA-PSI returns pairs of items that are within a specified distance
threshold of each other. This paper puts forward DA-PSI constructions for two
metric spaces: (i) Minkowski distance of order 1 over the set of integers
(i.e., for integers \(a\) and \(b\), their distance is \(|a-b|\)); and (ii) Hamming
distance over the set of binary strings of length \(\ell\). In the Minkowski
DA-PSI protocol, the communication complexity scales logarithmically in the
distance threshold and linearly in the set size. In the Hamming DA-PSI
protocol, the communication volume scales quadratically in the distance
threshold and is independent of the dimensionality of string length \(\ell\).
Experimental results with real applications confirm that DA-PSI provides more
effective matching at lower cost than naive solutions.