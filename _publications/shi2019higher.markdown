---
layout: publication
title: Higher-order Count Sketch Dimensionality Reduction That Retains Efficient Tensor Operations
authors: Shi Yang, Anandkumar Animashree
conference: "Arxiv"
year: 2019
bibkey: shi2019higher
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1901.11261"}
tags: ['ARXIV', 'TIP']
---
Sketching is a randomized dimensionality-reduction method that aims to preserve relevant information in large-scale datasets. Count sketch is a simple popular sketch which uses a randomized hash function to achieve compression. In this paper we propose a novel extension known as Higher-order Count Sketch (HCS). While count sketch uses a single hash function HCS uses multiple (smaller) hash functions for sketching. HCS reshapes the input (vector) data into a higher-order tensor and employs a tensor product of the random hash functions to compute the sketch. This results in an exponential saving (with respect to the order of the tensor) in the memory requirements of the hash functions under certain conditions on the input data. Furthermore when the input data itself has an underlying structure in the form of various tensor representations such as the Tucker decomposition we obtain significant advantages. We derive efficient (approximate) computation of various tensor operations such as tensor products and tensor contractions directly on the sketched data. Thus HCS is the first sketch to fully exploit the multi-dimensional nature of higher-order tensors. We apply HCS to tensorized neural networks where we replace fully connected layers with sketched tensor operations. We achieve nearly state of the art accuracy with significant compression on the image classification benchmark.
