---
layout: publication
title: Speeding Up Convolutional Neural Networks With Low Rank Expansions
authors: Max Jaderberg, Andrea Vedaldi, Andrew Zisserman
conference: Proceedings of the British Machine Vision Conference 2014
year: 2014
bibkey: jaderberg2014speeding
citations: 1121
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1405.3866'}]
tags: ["Efficiency"]
short_authors: Max Jaderberg, Andrea Vedaldi, Andrew Zisserman
---
The focus of this paper is speeding up the evaluation of convolutional neural
networks. While delivering impressive results across a range of computer vision
and machine learning tasks, these networks are computationally demanding,
limiting their deployability. Convolutional layers generally consume the bulk
of the processing time, and so in this work we present two simple schemes for
drastically speeding up these layers. This is achieved by exploiting
cross-channel or filter redundancy to construct a low rank basis of filters
that are rank-1 in the spatial domain. Our methods are architecture agnostic,
and can be easily applied to existing CPU and GPU convolutional frameworks for
tuneable speedup performance. We demonstrate this with a real world network
designed for scene text character recognition, showing a possible 2.5x speedup
with no loss in accuracy, and 4.5x speedup with less than 1% drop in accuracy,
still achieving state-of-the-art on standard benchmarks.