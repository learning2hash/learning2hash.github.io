---
layout: publication
title: Faster Clustering Via Non-backtracking Random Walks
authors: Brian Rappaport, Anuththari Gamage, Shuchin Aeron
conference: Arxiv
year: 2017
bibkey: rappaport2017faster
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.07967'}]
tags: ["Unsupervised"]
short_authors: Brian Rappaport, Anuththari Gamage, Shuchin Aeron
---
This paper presents VEC-NBT, a variation on the unsupervised graph clustering
technique VEC, which improves upon the performance of the original algorithm
significantly for sparse graphs. VEC employs a novel application of the
state-of-the-art word2vec model to embed a graph in Euclidean space via random
walks on the nodes of the graph. In VEC-NBT, we modify the original algorithm
to use a non-backtracking random walk instead of the normal backtracking random
walk used in VEC. We introduce a modification to a non-backtracking random
walk, which we call a begrudgingly-backtracking random walk, and show
empirically that using this model of random walks for VEC-NBT requires shorter
walks on the graph to obtain results with comparable or greater accuracy than
VEC, especially for sparser graphs.