---
layout: publication
title: Spectral Hashing
authors: Yair Weiss, Antonio Torralba, Rob Fergus
conference: "Neural Information Processing Systems"
year: 2008
citations: 2154
bibkey: weiss2008spectral
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2008/hash/d58072be2820e8682c0a27c0518e805e-Abstract.html"}
tags: ['Graph', 'NEURIPS', 'Unsupervised']
---
Semantic hashing seeks compact binary codes of datapoints so that the Hamming distance between codewords correlates with semantic similarity. Hinton et al. used a clever implementation of autoencoders to find such codes. In this paper, we show that the problem of finding a best code for a given dataset is closely related to the problem of graph partitioning and can be shown to be NP hard. By relaxing the original problem, we obtain a spectral method whose solutions are simply a subset of thresh- olded eigenvectors of the graph Laplacian. By utilizing recent results on convergence of graph Laplacian eigenvectors to the Laplace-Beltrami eigen- functions of manifolds, we show how to efficiently calculate the code of a novel datapoint. Taken together, both learning the code and applying it to a novel point are extremely simple. Our experiments show that our codes significantly outperform the state-of-the art.
