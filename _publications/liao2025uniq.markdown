---
layout: publication
title: 'Uniq: Unified Decoder With Task-specific Queries For Efficient Scene Graph
  Generation'
authors: Xinyao Liao, Wei Wei, Dangyang Chen, Yuanyuan Fu
conference: Arxiv
year: 2025
bibkey: liao2025uniq
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.05687'}]
tags: []
short_authors: Liao et al.
---
Scene Graph Generation(SGG) is a scene understanding task that aims at
identifying object entities and reasoning their relationships within a given
image. In contrast to prevailing two-stage methods based on a large object
detector (e.g., Faster R-CNN), one-stage methods integrate a fixed-size set of
learnable queries to jointly reason relational triplets <subject, predicate,
object>. This paradigm demonstrates robust performance with significantly
reduced parameters and computational overhead. However, the challenge in
one-stage methods stems from the issue of weak entanglement, wherein entities
involved in relationships require both coupled features shared within triplets
and decoupled visual features. Previous methods either adopt a single decoder
for coupled triplet feature modeling or multiple decoders for separate visual
feature extraction but fail to consider both. In this paper, we introduce UniQ,
a Unified decoder with task-specific Queries architecture, where task-specific
queries generate decoupled visual features for subjects, objects, and
predicates respectively, and unified decoder enables coupled feature modeling
within relational triplets. Experimental results on the Visual Genome dataset
demonstrate that UniQ has superior performance to both one-stage and two-stage
methods.