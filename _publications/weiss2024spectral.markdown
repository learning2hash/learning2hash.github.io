---
layout: publication
title: Spectral Hashing
authors: Weiss Y., Torralba, Fergus
conference: "Arxiv"
year: 2024
bibkey: weiss2024spectral
additional_links:
  - {name: "Paper", url: "https://people.csail.mit.edu/torralba/publications/spectralhashing.pdf"}
tags: ['ARXIV', 'Graph']
---
<p>Semantic hashing seeks compact binary codes of data-points so that
the Hamming distance between codewords correlates with semantic
similarity. In this paper, we show that the problem of finding a best
code for a given dataset is closely related to the problem of graph
partitioning and can be shown to be NP hard. By relaxing the original
problem, we obtain a spectral method whose solutions are simply a subset
of thresholded eigenvectors of the graph Laplacian. By utilizing recent
results on convergence of graph Laplacian eigenvectors to the
Laplace-Beltrami eigenfunctions of manifolds, we show how to efficiently
calculate the code of a novel datapoint. Taken together, both learning
the code and applying it to a novel point are extremely simple. Our
experiments show that our codes outperform the state-of-the art.</p>
