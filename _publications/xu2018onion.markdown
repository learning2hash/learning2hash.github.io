---
layout: publication
title: 'Onion Curve: A Space Filling Curve With Near-optimal Clustering'
authors: Pan Xu, Cuong Nguyen, Srikanta Tirthapura
conference: 2018 IEEE 34th International Conference on Data Engineering (ICDE)
year: 2018
bibkey: xu2018onion
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1801.07399'}]
tags: ["Efficiency"]
short_authors: Pan Xu, Cuong Nguyen, Srikanta Tirthapura
---
Space filling curves (SFCs) are widely used in the design of indexes for
spatial and temporal data. Clustering is a key metric for an SFC, that measures
how well the curve preserves locality in moving from higher dimensions to a
single dimension. We present the \{\em onion curve\}, an SFC whose clustering
performance is provably close to optimal for the cube and near-cube shaped
query sets, irrespective of the side length of the query. We show that in
contrast, the clustering performance of the widely used Hilbert curve can be
far from optimal, even for cube-shaped queries. Since the clustering
performance of an SFC is critical to the efficiency of multi-dimensional
indexes based on the SFC, the onion curve can deliver improved performance for
data structures involving multi-dimensional data.