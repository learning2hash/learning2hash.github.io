---
layout: publication
title: The All-paths And Cycles Graph Kernel
authors: P. -L. Giscard, R. C. Wilson
conference: Arxiv
year: 2017
bibkey: giscard2017all
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1708.01410'}]
tags: []
short_authors: P. -L. Giscard, R. C. Wilson
---
With the recent rise in the amount of structured data available, there has
been considerable interest in methods for machine learning with graphs. Many of
these approaches have been kernel methods, which focus on measuring the
similarity between graphs. These generally involving measuring the similarity
of structural elements such as walks or paths. Borgwardt and Kriegel proposed
the all-paths kernel but emphasized that it is NP-hard to compute and
infeasible in practice, favouring instead the shortest-path kernel. In this
paper, we introduce a new algorithm for computing the all-paths kernel which is
very efficient and enrich it further by including the simple cycles as well. We
demonstrate how it is feasible even on large datasets to compute all the paths
and simple cycles up to a moderate length. We show how to count labelled
paths/simple cycles between vertices of a graph and evaluate a labelled path
and simple cycles kernel. Extensive evaluations on a variety of graph datasets
demonstrate that the all-paths and cycles kernel has superior performance to
the shortest-path kernel and state-of-the-art performance overall.