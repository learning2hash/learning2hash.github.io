---
layout: publication
title: A New Near-linear Time Algorithm For K-nearest Neighbor Search Using A Compressed
  Cover Tree
authors: Yury Elkin, Vitaliy Kurlin
conference: Arxiv
year: 2021
bibkey: elkin2021new
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.15478'}]
tags: ["Tree Based ANN"]
short_authors: Yury Elkin, Vitaliy Kurlin
---
Given a reference set \\(R\\) of \\(n\\) points and a query set \\(Q\\) of \\(m\\) points in
a metric space, this paper studies an important problem of finding \\(k\\)-nearest
neighbors of every point \\(q \in Q\\) in the set \\(R\\) in a near-linear time. In the
paper at ICML 2006, Beygelzimer, Kakade, and Langford introduced a cover tree
on \\(R\\) and attempted to prove that this tree can be built in \\(O(nlog n)\\) time
while the nearest neighbor search can be done in \\(O(nlog m)\\) time with a
hidden dimensionality factor. This paper fills a substantial gap in the past
proofs of time complexity by defining a simpler compressed cover tree on the
reference set \\(R\\). The first new algorithm constructs a compressed cover tree
in \\(O(n log n)\\) time. The second new algorithm finds all \\(k\\)-nearest neighbors
of all points from \\(Q\\) using a compressed cover tree in time \\(O(m(k+log n)log
k)\\) with a hidden dimensionality factor depending on point distributions of the
given sets \\(R,Q\\) but not on their sizes.