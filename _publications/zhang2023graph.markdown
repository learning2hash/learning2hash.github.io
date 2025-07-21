---
layout: publication
title: Graph Convolution Based Efficient Re-Ranking for Visual Retrieval
authors: Zhang et al.
conference: IEEE Transactions on Multimedia
year: 2023
bibkey: zhang2023graph
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.08792'}]
tags: ["Hybrid-ANN-Methods", "Re-Ranking"]
---
Visual retrieval tasks such as image retrieval and person re-identification
(Re-ID) aim at effectively and thoroughly searching images with similar content
or the same identity. After obtaining retrieved examples, re-ranking is a
widely adopted post-processing step to reorder and improve the initial
retrieval results by making use of the contextual information from semantically
neighboring samples. Prevailing re-ranking approaches update distance metrics
and mostly rely on inefficient crosscheck set comparison operations while
computing expanded neighbors based distances. In this work, we present an
efficient re-ranking method which refines initial retrieval results by updating
features. Specifically, we reformulate re-ranking based on Graph Convolution
Networks (GCN) and propose a novel Graph Convolution based Re-ranking (GCR) for
visual retrieval tasks via feature propagation. To accelerate computation for
large-scale retrieval, a decentralized and synchronous feature propagation
algorithm which supports parallel or distributed computing is introduced. In
particular, the plain GCR is extended for cross-camera retrieval and an
improved feature propagation formulation is presented to leverage affinity
relationships across different cameras. It is also extended for video-based
retrieval, and Graph Convolution based Re-ranking for Video (GCRV) is proposed
by mathematically deriving a novel profile vector generation method for the
tracklet. Without bells and whistles, the proposed approaches achieve
state-of-the-art performances on seven benchmark datasets from three different
tasks, i.e., image retrieval, person Re-ID and video-based person Re-ID.