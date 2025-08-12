---
layout: publication
title: Bitpath -- Label Order Constrained Reachability Queries Over Large Graphs
authors: Medha Atre, Vineet Chaoji, Mohammed J. Zaki
conference: Arxiv
year: 2012
bibkey: atre2012bitpath
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1203.2886'}]
tags: []
short_authors: Medha Atre, Vineet Chaoji, Mohammed J. Zaki
---
In this paper we focus on the following constrained reachability problem over
edge-labeled graphs like RDF -- "given source node x, destination node y, and a
sequence of edge labels (a, b, c, d), is there a path between the two nodes
such that the edge labels on the path satisfy a regular expression
"*a.*b.*c.*d.*". A "*" before "a" allows any other edge label to appear on the
path before edge "a". "a.*" forces at least one edge with label "a". ".*" after
"a" allows zero or more edge labels after "a" and before "b". Our query
processing algorithm uses simple divide-and-conquer and greedy pruning
procedures to limit the search space. However, our graph indexing technique --
based on "compressed bit-vectors" -- allows indexing large graphs which
otherwise would have been infeasible. We have evaluated our approach on graphs
with more than 22 million edges and 6 million nodes -- much larger compared to
the datasets used in the contemporary work on path queries.