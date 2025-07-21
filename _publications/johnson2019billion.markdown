---
layout: publication
title: Billion-scale similarity search with GPUs
authors: "Johnson Jeff, Douze Matthijs, J\xE9gou Herv\xE9"
conference: IEEE Transactions on Big Data
year: 2019
bibkey: johnson2019billion
citations: 2024
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1702.08734'}]
tags: ["Similarity Search", "Scalability", "Large Scale Search"]
---
Similarity search finds application in specialized database systems handling
complex data such as images or videos, which are typically represented by
high-dimensional features and require specific indexing structures. This paper
tackles the problem of better utilizing GPUs for this task. While GPUs excel at
data-parallel tasks, prior approaches are bottlenecked by algorithms that
expose less parallelism, such as k-min selection, or make poor use of the
memory hierarchy.
  We propose a design for k-selection that operates at up to 55% of theoretical
peak performance, enabling a nearest neighbor implementation that is 8.5x
faster than prior GPU state of the art. We apply it in different similarity
search scenarios, by proposing optimized design for brute-force, approximate
and compressed-domain search based on product quantization. In all these
setups, we outperform the state of the art by large margins. Our implementation
enables the construction of a high accuracy k-NN graph on 95 million images
from the Yfcc100M dataset in 35 minutes, and of a graph connecting 1 billion
vectors in less than 12 hours on 4 Maxwell Titan X GPUs. We have open-sourced
our approach for the sake of comparison and reproducibility.