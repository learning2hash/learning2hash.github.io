---
layout: publication
title: Vertex-context Sampling For Weighted Network Embedding
authors: Chih-Ming Chen, Yi-Hsuan Yang, Yian Chen, Ming-Feng Tsai
conference: Arxiv
year: 2017
bibkey: chen2017vertex
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.00227'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Memory Efficiency", "Recommender Systems", "Scalability", "Similarity Search", "Tools & Libraries"]
short_authors: Chen et al.
---
In recent years, network embedding methods have garnered increasing attention
because of their effectiveness in various information retrieval tasks. The goal
is to learn low-dimensional representations of vertexes in an information
network and simultaneously capture and preserve the network structure. Critical
to the performance of a network embedding method is how the edges/vertexes of
the network is sampled for the learning process. Many existing methods adopt a
uniform sampling method to reduce learning complexity, but when the network is
non-uniform (i.e. a weighted network) such uniform sampling incurs information
loss. The goal of this paper is to present a generalized vertex sampling
framework that works seamlessly with most existing network embedding methods to
support weighted instead of uniform vertex/edge sampling. For efficiency, we
propose a delicate sequential vertex-to-context graph data structure, such that
sampling a training pair for learning takes only constant time. For scalability
and memory efficiency, we design the graph data structure in a way that keeps
space consumption low without requiring additional space. In addition to
implementing existing network embedding methods, the proposed framework can be
used to implement extensions that feature high-order proximity modeling and
weighted relation modeling. Experiments conducted on three datasets, including
a commercial large-scale one, verify the effectiveness and efficiency of the
proposed weighted network embedding methods on a variety of tasks, including
word similarity search, multi-label classification, and item recommendation.