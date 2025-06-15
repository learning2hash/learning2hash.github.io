---
layout: publication
title: Yes We CANN Constrained Approximate Nearest Neighbors For Local Feature-based Visual Localization
authors: Aiger Dror, Araujo André, Lynen Simon
conference: "Arxiv"
year: 2023
citations: 2
bibkey: aiger2023yes
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2306.09012"}
  - {name: "Code", url: "https://github.com/google-research/google-research/tree/master/cann}"}
tags: ['ARXIV', 'Has Code', 'Image Retrieval']
---
Large-scale visual localization systems continue to rely on 3D point clouds
built from image collections using structure-from-motion. While the 3D points
in these models are represented using local image features, directly matching a
query image's local features against the point cloud is challenging due to the
scale of the nearest-neighbor search problem. Many recent approaches to visual
localization have thus proposed a hybrid method, where first a global (per
image) embedding is used to retrieve a small subset of database images, and
local features of the query are matched only against those. It seems to have
become common belief that global embeddings are critical for said
image-retrieval in visual localization, despite the significant downside of
having to compute two feature types for each query image. In this paper, we
take a step back from this assumption and propose Constrained Approximate
Nearest Neighbors (CANN), a joint solution of k-nearest-neighbors across both
the geometry and appearance space using only local features. We first derive
the theoretical foundation for k-nearest-neighbor retrieval across multiple
metrics and then showcase how CANN improves visual localization. Our
experiments on public localization benchmarks demonstrate that our method
significantly outperforms both state-of-the-art global feature-based retrieval
and approaches using local feature aggregation schemes. Moreover, it is an
order of magnitude faster in both index and query time than feature aggregation
schemes for these datasets. Code:
\url\{https://github.com/google-research/google-research/tree/master/cann\}
