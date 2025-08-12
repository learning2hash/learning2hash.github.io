---
layout: publication
title: Multi-view Graph Embedding Using Randomized Shortest Paths
authors: Anuththari Gamage, Brian Rappaport, Shuchin Aeron, Xiaozhe Hu
conference: Arxiv
year: 2018
bibkey: gamage2018multi
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.06560'}]
tags: []
short_authors: Gamage et al.
---
Real-world data sets often provide multiple types of information about the
same set of entities. This data is well represented by multi-view graphs, which
consist of several distinct sets of edges over the same nodes. These can be
used to analyze how entities interact from different viewpoints. Combining
multiple views improves the quality of inferences drawn from the underlying
data, which has increased interest in developing efficient multi-view graph
embedding methods. We propose an algorithm, C-RSP, that generates a common (C)
embedding of a multi-view graph using Randomized Shortest Paths (RSP). This
algorithm generates a dissimilarity measure between nodes by minimizing the
expected cost of a random walk between any two nodes across all views of a
multi-view graph, in doing so encoding both the local and global structure of
the graph. We test C-RSP on both real and synthetic data and show that it
outperforms benchmark algorithms at embedding and clustering tasks while
remaining computationally efficient.