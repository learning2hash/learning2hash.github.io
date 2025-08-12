---
layout: publication
title: Block-diagonal Guided DBSCAN Clustering
authors: Weibing Zhao
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2024
bibkey: zhao2024block
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.01341'}]
tags: []
short_authors: Weibing Zhao
---
Cluster analysis plays a crucial role in database mining, and one of the most
widely used algorithms in this field is DBSCAN. However, DBSCAN has several
limitations, such as difficulty in handling high-dimensional large-scale data,
sensitivity to input parameters, and lack of robustness in producing clustering
results. This paper introduces an improved version of DBSCAN that leverages the
block-diagonal property of the similarity graph to guide the clustering
procedure of DBSCAN. The key idea is to construct a graph that measures the
similarity between high-dimensional large-scale data points and has the
potential to be transformed into a block-diagonal form through an unknown
permutation, followed by a cluster-ordering procedure to generate the desired
permutation. The clustering structure can be easily determined by identifying
the diagonal blocks in the permuted graph. We propose a gradient descent-based
method to solve the proposed problem. Additionally, we develop a DBSCAN-based
points traversal algorithm that identifies clusters with high densities in the
graph and generates an augmented ordering of clusters. The block-diagonal
structure of the graph is then achieved through permutation based on the
traversal order, providing a flexible foundation for both automatic and
interactive cluster analysis. We introduce a split-and-refine algorithm to
automatically search for all diagonal blocks in the permuted graph with
theoretically optimal guarantees under specific cases. We extensively evaluate
our proposed approach on twelve challenging real-world benchmark clustering
datasets and demonstrate its superior performance compared to the
state-of-the-art clustering method on every dataset.