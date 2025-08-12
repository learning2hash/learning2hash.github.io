---
layout: publication
title: Hyperbolic Convolution Via Kernel Point Aggregation
authors: Eric Qu, Dongmian Zou
conference: Arxiv
year: 2023
bibkey: qu2023hyperbolic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.08862'}]
tags: []
short_authors: Eric Qu, Dongmian Zou
---
Learning representations according to the underlying geometry is of vital
importance for non-Euclidean data. Studies have revealed that the hyperbolic
space can effectively embed hierarchical or tree-like data. In particular, the
few past years have witnessed a rapid development of hyperbolic neural
networks. However, it is challenging to learn good hyperbolic representations
since common Euclidean neural operations, such as convolution, do not extend to
the hyperbolic space. Most hyperbolic neural networks do not embrace the
convolution operation and ignore local patterns. Others either only use
non-hyperbolic convolution, or miss essential properties such as equivariance
to permutation. We propose HKConv, a novel trainable hyperbolic convolution
which first correlates trainable local hyperbolic features with fixed kernel
points placed in the hyperbolic space, then aggregates the output features
within a local neighborhood. HKConv not only expressively learns local features
according to the hyperbolic geometry, but also enjoys equivariance to
permutation of hyperbolic points and invariance to parallel transport of a
local neighborhood. We show that neural networks with HKConv layers advance
state-of-the-art in various tasks.