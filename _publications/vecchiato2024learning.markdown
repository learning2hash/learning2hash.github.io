---
layout: publication
title: Learning Cluster Representatives For Approximate Nearest Neighbor Search
authors: Thomas Vecchiato
conference: Arxiv
year: 2024
bibkey: vecchiato2024learning
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.05921'}]
tags: ["Efficiency", "Scalability", "Similarity Search", "Unsupervised"]
short_authors: Thomas Vecchiato
---
Developing increasingly efficient and accurate algorithms for approximate
nearest neighbor search is a paramount goal in modern information retrieval. A
primary approach to addressing this question is clustering, which involves
partitioning the dataset into distinct groups, with each group characterized by
a representative data point. By this method, retrieving the top-k data points
for a query requires identifying the most relevant clusters based on their
representatives -- a routing step -- and then conducting a nearest neighbor
search within these clusters only, drastically reducing the search space.
  The objective of this thesis is not only to provide a comprehensive
explanation of clustering-based approximate nearest neighbor search but also to
introduce and delve into every aspect of our novel state-of-the-art method,
which originated from a natural observation: The routing function solves a
ranking problem, making the function amenable to learning-to-rank. The
development of this intuition and applying it to maximum inner product search
has led us to demonstrate that learning cluster representatives using a simple
linear function significantly boosts the accuracy of clustering-based
approximate nearest neighbor search.