---
layout: publication
title: Compressed Bounding Volume Hierarchies For Collision Detection & Proximity
  Query
authors: Toni Tan, Rene Weller, Gabriel Zachmann
conference: Arxiv
year: 2020
bibkey: tan2020compressed
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.05348'}]
tags: ["Efficiency", "Memory Efficiency", "Scalability"]
short_authors: Toni Tan, Rene Weller, Gabriel Zachmann
---
We present a novel representation of compressed data structure for
simultaneous bounding volume hierarchy (BVH) traversals like they appear for
instance in collision detection & proximity query. The main idea is to compress
bounding volume (BV) descriptors and cluster BVH into a smaller parts 'treelet'
that fit into CPU cache while at the same time maintain random-access and
automatic cache-aware data structure layouts. To do that, we quantify BV and
compress 'treelet' using predictor-corrector scheme with the predictor at a
specific node in the BVH based on the chain of BVs upwards.