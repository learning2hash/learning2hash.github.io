---
layout: publication
title: Massively Parallel Path Space Filtering
authors: Nikolaus Binder, Sascha Fricke, Alexander Keller
conference: Arxiv
year: 2019
citations: 5
bibkey: binder2019massively
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.05942'}]
tags: [Uncategorized]
---
Restricting path tracing to a small number of paths per pixel for performance
reasons rarely achieves a satisfactory image quality for scenes of interest.
However, path space filtering may dramatically improve the visual quality by
sharing information across vertices of paths classified as proximate. Unlike
screen space-based approaches, these paths neither need to be present on the
screen, nor is filtering restricted to the first intersection with the scene.
While searching proximate vertices had been more expensive than filtering in
screen space, we greatly improve over this performance penalty by storing,
updating, and looking up the required information in a hash table. The keys are
constructed from jittered and quantized information, such that only a single
query very likely replaces costly neighborhood searches. A massively parallel
implementation of the algorithm is demonstrated on a graphics processing unit
(GPU).