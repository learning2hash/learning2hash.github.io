---
layout: publication
title: Integrating Semantics And Neighborhood Information With Graph-driven Generative
  Models For Document Retrieval
authors: Zijing Ou et al.
conference: ACL2021
year: 2021
citations: 0
bibkey: ou2021integrating
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.13066'}]
tags: [Hashing Methods, Evaluation Metrics, Benchmarks and Datasets]
---
With the need of fast retrieval speed and small memory footprint, document
hashing has been playing a crucial role in large-scale information retrieval.
To generate high-quality hashing code, both semantics and neighborhood
information are crucial. However, most existing methods leverage only one of
them or simply combine them via some intuitive criteria, lacking a theoretical
principle to guide the integration process. In this paper, we encode the
neighborhood information with a graph-induced Gaussian distribution, and
propose to integrate the two types of information with a graph-driven
generative model. To deal with the complicated correlations among documents, we
further propose a tree-structured approximation method for learning. Under the
approximation, we prove that the training objective can be decomposed into
terms involving only singleton or pairwise documents, enabling the model to be
trained as efficiently as uncorrelated ones. Extensive experimental results on
three benchmark datasets show that our method achieves superior performance
over state-of-the-art methods, demonstrating the effectiveness of the proposed
model for simultaneously preserving semantic and neighborhood information.\