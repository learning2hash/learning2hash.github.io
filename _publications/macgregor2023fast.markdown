---
layout: publication
title: Fast Approximation Of Similarity Graphs With Kernel Density Estimation
authors: Macgregor Peter, Sun He
conference: "Arxiv"
year: 2023
bibkey: macgregor2023fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2310.13870"}
tags: ['ARXIV', 'Graph', 'Unsupervised']
---
Constructing a similarity graph from a set \(X\) of data points in \(\mathbb\&amp;\#123;R\&amp;\#125;^d\) is the first step of many modern clustering algorithms. However, typical constructions of a similarity graph have high time complexity, and a quadratic space dependency with respect to \(|X|\). We address this limitation and present a new algorithmic framework that constructs a sparse approximation of the fully connected similarity graph while preserving its cluster structure. Our presented algorithm is based on the kernel density estimation problem, and is applicable for arbitrary kernel functions. We compare our designed algorithm with the well-known implementations from the scikit-learn library and the FAISS library, and find that our method significantly outperforms the implementation from both libraries on a variety of datasets.
