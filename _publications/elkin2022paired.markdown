---
layout: publication
title: Paired Compressed Cover Trees Guarantee A Near Linear Parametrized Complexity
  For All \(k\)-nearest Neighbors Search In An Arbitrary Metric Space
authors: Yury Elkin, Vitaliy Kurlin
conference: Arxiv
year: 2022
bibkey: elkin2022paired
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.06553'}]
tags: ["Scalability", "Similarity Search", "Tree Based ANN"]
short_authors: Yury Elkin, Vitaliy Kurlin
---
This paper studies the important problem of finding all \(k\)-nearest neighbors
to points of a query set \(Q\) in another reference set \(R\) within any metric
space. Our previous work defined compressed cover trees and corrected the key
arguments in several past papers for challenging datasets. In 2009 Ram, Lee,
March, and Gray attempted to improve the time complexity by using pairs of
cover trees on the query and reference sets. In 2015 Curtin with the above
co-authors used extra parameters to finally prove a time complexity for \(k=1\).
The current work fills all previous gaps and improves the nearest neighbor
search based on pairs of new compressed cover trees. The novel imbalance
parameter of paired trees allowed us to prove a better time complexity for any
number of neighbors \(k\geq 1\).