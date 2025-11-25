---
layout: publication
title: Non-iterative Label Propagation In Optimal Leading Forest
authors: Ji Xu, Guoyin Wang
conference: Arxiv
year: 2017
bibkey: xu2017non
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.08426'}]
tags: ["Efficiency", "Graph Based ANN", "Locality-Sensitive-Hashing"]
short_authors: Ji Xu, Guoyin Wang
---
Graph based semi-supervised learning (GSSL) has intuitive representation and
can be improved by exploiting the matrix calculation. However, it has to
perform iterative optimization to achieve a preset objective, which usually
leads to low efficiency. Another inconvenience lying in GSSL is that when new
data come, the graph construction and the optimization have to be conducted all
over again. We propose a sound assumption, arguing that: the neighboring data
points are not in peer-to-peer relation, but in a partial-ordered relation
induced by the local density and distance between the data; and the label of a
center can be regarded as the contribution of its followers. Starting from the
assumption, we develop a highly efficient non-iterative label propagation
algorithm based on a novel data structure named as optimal leading forest
(LaPOLeaF). The major weaknesses of the traditional GSSL are addressed by this
study. We further scale LaPOLeaF to accommodate big data by utilizing block
distance matrix technique, parallel computing, and Locality-Sensitive Hashing
(LSH). Experiments on large datasets have shown the promising results of the
proposed methods.