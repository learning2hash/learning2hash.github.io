---
layout: publication
title: Finding Maximum Matchings In RDV Graphs Efficiently
authors: Therese Biedl, Prashant Gokhale
conference: Arxiv
year: 2024
bibkey: biedl2024finding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.03632'}]
tags: ["Efficiency", "Scalability"]
short_authors: Therese Biedl, Prashant Gokhale
---
In this paper, we study the maximum matching problem in RDV graphs, i.e.,
graphs that are vertex-intersection graphs of downward paths in a rooted tree.
We show that this problem can be reduced to a problem of testing (repeatedly)
whether a vertical segment intersects one of a dynamically changing set of
horizontal segments, which in turn reduces to an orthogonal ray shooting query.
Using a suitable data structure, we can therefore find a maximum matching in
\(O(nlog n)\) time (presuming a linear-sized representation of the graph is
given), i.e., without even looking at all edges.