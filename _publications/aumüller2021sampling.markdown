---
layout: publication
title: Sampling A Near Neighbor In High Dimensions -- Who Is The Fairest Of Them All?
authors: "Aum\xFCller Martin, Har-peled Sariel, Mahabadi Sepideh, Pagh Rasmus, Silvestri\
  \ Francesco"
conference: ACM Transactions on Database Systems
year: 2022
bibkey: "aum\xFCller2021sampling"
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.10905'}]
tags: ["Hashing-Methods", "Locality-Sensitive-Hashing", "Efficiency", "Similarity-Search", "Datasets", "Evaluation"]
short_authors: "Aum\xFCller et al."
---
Similarity search is a fundamental algorithmic primitive, widely used in many
computer science disciplines. Given a set of points \\(S\\) and a radius parameter
\\(r>0\\), the \\(r\\)-near neighbor (\\(r\\)-NN) problem asks for a data structure that,
given any query point \\(q\\), returns a point \\(p\\) within distance at most \\(r\\) from
\\(q\\). In this paper, we study the \\(r\\)-NN problem in the light of individual
fairness and providing equal opportunities: all points that are within distance
\\(r\\) from the query should have the same probability to be returned. In the
low-dimensional case, this problem was first studied by Hu, Qiao, and Tao (PODS
2014). Locality sensitive hashing (LSH), the theoretically strongest approach
to similarity search in high dimensions, does not provide such a fairness
guarantee. In this work, we show that LSH based algorithms can be made fair,
without a significant loss in efficiency. We propose several efficient data
structures for the exact and approximate variants of the fair NN problem. Our
approach works more generally for sampling uniformly from a sub-collection of
sets of a given collection and can be used in a few other applications. We also
develop a data structure for fair similarity search under inner product that
requires nearly-linear space and exploits locality sensitive filters. The paper
concludes with an experimental evaluation that highlights the inherent
unfairness of NN data structures and shows the performance of our algorithms on
real-world datasets.