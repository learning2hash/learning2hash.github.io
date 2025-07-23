---
layout: publication
title: Fast Single-core K-nearest Neighbor Graph Computation
authors: Kluser Dan, Bokstaller Jonas, Rutz Samuel, Buner Tobias
conference: Arxiv
year: 2021
bibkey: kluser2021fast
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.06630'}]
tags: ["Efficiency", "Evaluation", "Graph-based ANN", "Scalability"]
short_authors: Kluser et al.
---
Fast and reliable K-Nearest Neighbor Graph algorithms are more important than
ever due to their widespread use in many data processing techniques. This paper
presents a runtime optimized C implementation of the heuristic "NN-Descent"
algorithm by Wei Dong et al. for the l2-distance metric. Various implementation
optimizations are explained which improve performance for low-dimensional as
well as high dimensional datasets. Optimizations to speed up the selection of
which datapoint pairs to evaluate the distance for are primarily impactful for
low-dimensional datasets. A heuristic which exploits the iterative nature of
NN-Descent to reorder data in memory is presented which enables better use of
locality and thereby improves the runtime. The restriction to the l2-distance
metric allows for the use of blocked distance evaluations which significantly
increase performance for high dimensional datasets. In combination the
optimizations yield an implementation which significantly outperforms a widely
used implementation of NN-Descent on all considered datasets. For instance, the
runtime on the popular MNIST handwritten digits dataset is halved.