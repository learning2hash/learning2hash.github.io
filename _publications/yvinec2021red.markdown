---
layout: publication
title: 'RED : Looking For Redundancies For Data-free Structured Compression Of Deep Neural Networks'
authors: Edouard Yvinec, Arnaud Dapogny, Matthieu Cord, Kevin Bailly
conference: "Arxiv"
year: 2021
citations: 9
bibkey: yvinec2021red
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2105.14797'}
tags: ['Cross-Modal', 'Deep', 'Compression', 'Supervised', 'Hashing']
---
Deep Neural Networks (DNNs) are ubiquitous in today's computer vision
land-scape, despite involving considerable computational costs. The mainstream
approaches for runtime acceleration consist in pruning connections
(unstructured pruning) or, better, filters (structured pruning), both often
requiring data to re-train the model. In this paper, we present RED, a
data-free structured, unified approach to tackle structured pruning. First, we
propose a novel adaptive hashing of the scalar DNN weight distribution
densities to increase the number of identical neurons represented by their
weight vectors. Second, we prune the network by merging redundant neurons based
on their relative similarities, as defined by their distance. Third, we propose
a novel uneven depthwise separation technique to further prune convolutional
layers. We demonstrate through a large variety of benchmarks that RED largely
outperforms other data-free pruning methods, often reaching performance similar
to unconstrained, data-driven methods.
