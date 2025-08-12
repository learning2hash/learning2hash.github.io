---
layout: publication
title: Learning Hierarchical Semantic Image Manipulation Through Structured Representations
authors: Seunghoon Hong, Xinchen Yan, Thomas Huang, Honglak Lee
conference: Arxiv
year: 2018
bibkey: hong2018learning
citations: 62
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1808.07535'}]
tags: []
short_authors: Hong et al.
---
Understanding, reasoning, and manipulating semantic concepts of images have
been a fundamental research problem for decades. Previous work mainly focused
on direct manipulation on natural image manifold through color strokes,
key-points, textures, and holes-to-fill. In this work, we present a novel
hierarchical framework for semantic image manipulation. Key to our hierarchical
framework is that we employ a structured semantic layout as our intermediate
representation for manipulation. Initialized with coarse-level bounding boxes,
our structure generator first creates pixel-wise semantic layout capturing the
object shape, object-object interactions, and object-scene relations. Then our
image generator fills in the pixel-level textures guided by the semantic
layout. Such framework allows a user to manipulate images at object-level by
adding, removing, and moving one bounding box at a time. Experimental
evaluations demonstrate the advantages of the hierarchical manipulation
framework over existing image generation and context hole-filing models, both
qualitatively and quantitatively. Benefits of the hierarchical framework are
further demonstrated in applications such as semantic object manipulation,
interactive image editing, and data-driven image manipulation.