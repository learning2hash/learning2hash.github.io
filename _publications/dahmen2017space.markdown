---
layout: publication
title: Space-filling Curve Indices As Acceleration Structure For Exemplar-based Inpainting
authors: Tim Dahmen, Patrick Trampert, Pascal Peter, Pinak Bheed, Joachim Weickert,
  Philipp Slusallek
conference: Arxiv
year: 2017
bibkey: dahmen2017space
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1712.06326'}]
tags: ["Efficiency", "Vector Indexing"]
short_authors: Dahmen et al.
---
Exemplar-based inpainting is the process of reconstructing missing parts of
an image by searching the remaining data for patches that fit seamlessly. The
image is completed to a plausible-looking solution by repeatedly inserting the
patch that is the best match according to some cost function. We present an
acceleration structure that uses a multi-index scheme to accelerate this search
procedure drastically, particularly in the case of very large datasets. The
index scheme uses ideas such as dimensionality reduction and k-nearest neighbor
search on space-filling curves that are well known in the field of multimedia
databases. Our method has a theoretic runtime of O(log2 n) per iteration and
reaches a speedup factor of up to 660 over the original method. The approach
has the advantage of being agnostic to most modelbased parts of exemplar-based
inpainting such as the order in which patches are processed and the cost
function used to determine patch similarity. Thus, the acceleration structure
can be used in conjunction with most exemplar-based inpainting algorithms.