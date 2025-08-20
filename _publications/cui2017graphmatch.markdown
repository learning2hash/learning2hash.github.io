---
layout: publication
title: 'Graphmatch: Efficient Large-scale Graph Construction For Structure From Motion'
authors: Qiaodong Cui, Victor Fragoso, Chris Sweeney, Pradeep Sen
conference: 2017 International Conference on 3D Vision (3DV)
year: 2017
bibkey: cui2017graphmatch
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1710.01602'}]
tags: [Scalability, Graph-based ANN]
short_authors: Cui et al.
---
We present GraphMatch, an approximate yet efficient method for building the
matching graph for large-scale structure-from-motion (SfM) pipelines. Unlike
modern SfM pipelines that use vocabulary (Voc.) trees to quickly build the
matching graph and avoid a costly brute-force search of matching image pairs,
GraphMatch does not require an expensive offline pre-processing phase to
construct a Voc. tree. Instead, GraphMatch leverages two priors that can
predict which image pairs are likely to match, thereby making the matching
process for SfM much more efficient. The first is a score computed from the
distance between the Fisher vectors of any two images. The second prior is
based on the graph distance between vertices in the underlying matching graph.
GraphMatch combines these two priors into an iterative "sample-and-propagate"
scheme similar to the PatchMatch algorithm. Its sampling stage uses Fisher
similarity priors to guide the search for matching image pairs, while its
propagation stage explores neighbors of matched pairs to find new ones with a
high image similarity score. Our experiments show that GraphMatch finds the
most image pairs as compared to competing, approximate methods while at the
same time being the most efficient.