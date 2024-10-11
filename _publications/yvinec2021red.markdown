---
layout: publication
title: RED Looking For Redundancies For Data-freestructured Compression Of Deep Neural Networks
authors: Edouard Yvinec, Arnaud Dapogny, Matthieu Cord, Kevin Bailly
conference: "Neural Information Processing Systems"
year: 2021
bibkey: yvinec2021red
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2021/hash/ae5e3ce40e0404a45ecacaaf05e5f735-Abstract.html"}
tags: ['NEURIPS', 'Supervised']
---
Deep Neural Networks (DNNs) are ubiquitous in today's computer vision landscape, despite involving considerable computational costs. The mainstream approaches for runtime acceleration consist in pruning connections (unstructured pruning) or, better, filters (structured pruning), both often requiring data to retrain the model. In this paper, we present RED, a data-free, unified approach to tackle structured pruning. First, we propose a novel adaptive hashing of the scalar DNN weight distribution densities to increase the number of identical neurons represented by their weight vectors. Second, we prune the network by merging redundant neurons based on their relative similarities, as defined by their distance. Third, we propose a novel uneven depthwise separation technique to further prune convolutional layers. We demonstrate through a large variety of benchmarks that RED largely outperforms other data-free pruning methods, often reaching performance similar to unconstrained, data-driven methods.
