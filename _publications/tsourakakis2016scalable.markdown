---
layout: publication
title: Scalable Motif-aware Graph Clustering
authors: Charalampos Tsourakakis, Jakub Pachocki, Michael Mitzenmacher
conference: Proceedings of the 26th International Conference on World Wide Web
year: 2017
bibkey: tsourakakis2016scalable
citations: 151
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.06235'}]
tags: ["Scalability"]
short_authors: Charalampos Tsourakakis, Jakub Pachocki, Michael Mitzenmacher
---
We develop new methods based on graph motifs for graph clustering, allowing
more efficient detection of communities within networks. We focus on triangles
within graphs, but our techniques extend to other clique motifs as well. Our
intuition, which has been suggested but not formalized similarly in previous
works, is that triangles are a better signature of community than edges. We
therefore generalize the notion of conductance for a graph to \{\em triangle
conductance\}, where the edges are weighted according to the number of triangles
containing the edge. This methodology allows us to develop variations of
several existing clustering techniques, including spectral clustering, that
minimize triangles split by the cluster instead of edges cut by the cluster. We
provide theoretical results in a planted partition model to demonstrate the
potential for triangle conductance in clustering problems. We then show
experimentally the effectiveness of our methods to multiple applications in
machine learning and graph mining.