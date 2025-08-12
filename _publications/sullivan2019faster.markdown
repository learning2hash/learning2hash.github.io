---
layout: publication
title: Faster Biclique Mining In Near-bipartite Graphs
authors: Blair D. Sullivan, Andrew van Der Poel, Trey Woodlief
conference: Lecture Notes in Computer Science
year: 2019
bibkey: sullivan2019faster
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.01538'}]
tags: ["Efficiency", "Graph Based ANN"]
short_authors: Blair D. Sullivan, Andrew van Der Poel, Trey Woodlief
---
Identifying dense bipartite subgraphs is a common graph data mining task.
Many applications focus on the enumeration of all maximal bicliques (MBs),
though sometimes the stricter variant of maximal induced bicliques (MIBs) is of
interest. Recent work of Kloster et al. introduced a MIB-enumeration approach
designed for "near-bipartite" graphs, where the runtime is parameterized by the
size k of an odd cycle transversal (OCT), a vertex set whose deletion results
in a bipartite graph. Their algorithm was shown to outperform the previously
best known algorithm even when k was logarithmic in |V|. In this paper, we
introduce two new algorithms optimized for near-bipartite graphs - one which
enumerates MIBs in time O(M_I |V||E| k), and another based on the approach of
Alexe et al. which enumerates MBs in time O(M_B |V||E| k), where M_I and M_B
denote the number of MIBs and MBs in the graph, respectively. We implement all
of our algorithms in open-source C++ code and experimentally verify that the
OCT-based approaches are faster in practice than the previously existing
algorithms on graphs with a wide variety of sizes, densities, and OCT
decompositions.