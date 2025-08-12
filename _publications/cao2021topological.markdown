---
layout: publication
title: Topological Information Retrieval With Dilation-invariant Bottleneck Comparative
  Measures
authors: Yueqi Cao, Athanasios Vlontzos, Luca Schmidtke, Bernhard Kainz, Anthea Monod
conference: 'Information and Inference: A Journal of the IMA'
year: 2023
bibkey: cao2021topological
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.01672'}]
tags: []
short_authors: Cao et al.
---
Appropriately representing elements in a database so that queries may be
accurately matched is a central task in information retrieval; recently, this
has been achieved by embedding the graphical structure of the database into a
manifold in a hierarchy-preserving manner using a variety of metrics.
Persistent homology is a tool commonly used in topological data analysis that
is able to rigorously characterize a database in terms of both its hierarchy
and connectivity structure. Computing persistent homology on a variety of
embedded datasets reveals that some commonly used embeddings fail to preserve
the connectivity. We show that those embeddings which successfully retain the
database topology coincide in persistent homology by introducing two
dilation-invariant comparative measures to capture this effect: in particular,
they address the issue of metric distortion on manifolds. We provide an
algorithm for their computation that exhibits greatly reduced time complexity
over existing methods. We use these measures to perform the first instance of
topology-based information retrieval and demonstrate its increased performance
over the standard bottleneck distance for persistent homology. We showcase our
approach on databases of different data varieties including text, videos, and
medical images.