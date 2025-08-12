---
layout: publication
title: Hyperdimensional Computing As A Framework For Systematic Aggregation Of Image
  Descriptors
authors: Peer Neubert, Stefan Schubert
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: neubert2021hyperdimensional
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.07720'}]
tags: ["CVPR"]
short_authors: Peer Neubert, Stefan Schubert
---
Image and video descriptors are an omnipresent tool in computer vision and
its application fields like mobile robotics. Many hand-crafted and in
particular learned image descriptors are numerical vectors with a potentially
(very) large number of dimensions. Practical considerations like memory
consumption or time for comparisons call for the creation of compact
representations. In this paper, we use hyperdimensional computing (HDC) as an
approach to systematically combine information from a set of vectors in a
single vector of the same dimensionality. HDC is a known technique to perform
symbolic processing with distributed representation in numerical vectors with
thousands of dimensions. We present a HDC implementation that is suitable for
processing the output of existing and future (deep-learning based) image
descriptors. We discuss how this can be used as a framework to process
descriptors together with additional knowledge by simple and fast vector
operations. A concrete outcome is a novel HDC-based approach to aggregate a set
of local image descriptors together with their image positions in a single
holistic descriptor. The comparison to available holistic descriptors and
aggregation methods on a series of standard mobile robotics place recognition
experiments shows a 20% improvement in average performance compared to
runner-up and 3.6x better worst-case performance.