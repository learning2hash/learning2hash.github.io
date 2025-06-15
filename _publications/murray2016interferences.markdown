---
layout: publication
title: 'Interferences In Match Kernels'
authors: Naila Murray, Hervé Jégou, Florent Perronnin, Andrew Zisserman
conference: "Arxiv"
year: 2016
citations: 17
bibkey: murray2016interferences
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1611.08194'}
tags: ['Cross-Modal', 'Independent', 'Retrieval Models', 'Shallow', 'Applications']
---
We consider the design of an image representation that embeds and aggregates
a set of local descriptors into a single vector. Popular representations of
this kind include the bag-of-visual-words, the Fisher vector and the VLAD. When
two such image representations are compared with the dot-product, the
image-to-image similarity can be interpreted as a match kernel. In match
kernels, one has to deal with interference, i.e. with the fact that even if two
descriptors are unrelated, their matching score may contribute to the overall
similarity.
  We formalise this problem and propose two related solutions, both aimed at
equalising the individual contributions of the local descriptors in the final
representation. These methods modify the aggregation stage by including a set
of per-descriptor weights. They differ by the objective function that is
optimised to compute those weights. The first is a "democratisation" strategy
that aims at equalising the relative importance of each descriptor in the set
comparison metric. The second one involves equalising the match of a single
descriptor to the aggregated vector.
  These concurrent methods give a substantial performance boost over the state
of the art in image search with short or mid-size vectors, as demonstrated by
our experiments on standard public image retrieval benchmarks.
