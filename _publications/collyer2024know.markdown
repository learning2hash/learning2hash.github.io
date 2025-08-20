---
layout: publication
title: 'Know Your Neighborhood: General And Zero-shot Capable Binary Function Search
  Powered By Call Graphlets'
authors: Joshua Collyer, Tim Watson, Iain Phillips
conference: Arxiv
year: 2024
bibkey: collyer2024know
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.02606'}]
tags: [Compact Codes, Datasets, Evaluation, Distance Metric Learning, Few-shot & Zero-shot]
short_authors: Joshua Collyer, Tim Watson, Iain Phillips
---
Binary code similarity detection is an important problem with applications in
areas such as malware analysis, vulnerability research and license violation
detection. This paper proposes a novel graph neural network architecture
combined with a novel graph data representation called call graphlets. A call
graphlet encodes the neighborhood around each function in a binary executable,
capturing the local and global context through a series of statistical
features. A specialized graph neural network model operates on this graph
representation, learning to map it to a feature vector that encodes semantic
binary code similarities using deep-metric learning. The proposed approach is
evaluated across five distinct datasets covering different architectures,
compiler tool chains, and optimization levels. Experimental results show that
the combination of call graphlets and the novel graph neural network
architecture achieves comparable or state-of-the-art performance compared to
baseline techniques across cross-architecture, mono-architecture and zero shot
tasks. In addition, our proposed approach also performs well when evaluated
against an out-of-domain function inlining task. The work provides a general
and effective graph neural network-based solution for conducting binary code
similarity detection.