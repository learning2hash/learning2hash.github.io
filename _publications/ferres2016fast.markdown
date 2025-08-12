---
layout: publication
title: Fast And Compact Planar Embeddings
authors: "Leo Ferres, Jos\xE9 Fuentes, Travis Gagie, Meng He, Gonzalo Navarro"
conference: Computational Geometry
year: 2020
bibkey: ferres2016fast
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.00130'}]
tags: ["Efficiency"]
short_authors: Ferres et al.
---
There are many representations of planar graphs, but few are as elegant as
Tur\'an's (1984): it is simple and practical, uses only 4 bits per edge, can
handle self-loops and multi-edges, and can store any specified embedding. Its
main disadvantage has been that "it does not allow efficient searching"
(Jacobson, 1989). In this paper we show how to add a sublinear number of bits
to Tur\'an's representation such that it supports fast navigation while
retaining simplicity. As a consequence of the inherited simplicity, we offer
the first efficient parallel construction of a compact encoding of a planar
graph embedding. Our experimental results show that the resulting
representation uses about 6 bits per edge in practice, supports basic
navigation operations within a few microseconds, and can be built sequentially
at a rate below 1 microsecond per edge, featuring a linear speedup with a
parallel efficiency around 50% for large datasets.