---
layout: publication
title: Efficient Wind Speed Nowcasting With Gpu-accelerated Nearest Neighbors Algorithm
authors: "Arnaud Pannatier, Ricardo Picatoste, Fran\xE7ois Fleuret"
conference: Arxiv
year: 2021
bibkey: pannatier2021efficient
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.10408'}]
tags: [Datasets, Efficiency]
short_authors: "Arnaud Pannatier, Ricardo Picatoste, Fran\xE7ois Fleuret"
---
This paper proposes a simple yet efficient high-altitude wind nowcasting
pipeline. It processes efficiently a vast amount of live data recorded by
airplanes over the whole airspace and reconstructs the wind field with good
accuracy. It creates a unique context for each point in the dataset and then
extrapolates from it. As creating such context is computationally intensive,
this paper proposes a novel algorithm that reduces the time and memory cost by
efficiently fetching nearest neighbors in a data set whose elements are
organized along smooth trajectories that can be approximated with piece-wise
linear structures.
  We introduce an efficient and exact strategy implemented through algebraic
tensorial operations, which is well-suited to modern GPU-based computing
infrastructure. This method employs a scalable Euclidean metric and allows
masking data points along one dimension. When applied, this method is more
efficient than plain Euclidean k-NN and other well-known data selection methods
such as KDTrees and provides a several-fold speedup. We provide an
implementation in PyTorch and a novel data set to allow the replication of
empirical results.