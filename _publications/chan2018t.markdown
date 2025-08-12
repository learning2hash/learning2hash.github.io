---
layout: publication
title: 'T-sne-cuda: Gpu-accelerated T-sne And Its Applications To Modern Data'
authors: David M. Chan, Roshan Rao, Forrest Huang, John F. Canny
conference: 2018 30th International Symposium on Computer Architecture and High Performance
  Computing (SBAC-PAD)
year: 2018
bibkey: chan2018t
citations: 82
additional_links: [{name: Code, url: 'https://github.com/CannyLab/tsne-cuda'}, {name: Paper,
    url: 'https://arxiv.org/abs/1807.11824'}]
tags: []
short_authors: Chan et al.
---
Modern datasets and models are notoriously difficult to explore and analyze
due to their inherent high dimensionality and massive numbers of samples.
Existing visualization methods which employ dimensionality reduction to two or
three dimensions are often inefficient and/or ineffective for these datasets.
This paper introduces t-SNE-CUDA, a GPU-accelerated implementation of
t-distributed Symmetric Neighbor Embedding (t-SNE) for visualizing datasets and
models. t-SNE-CUDA significantly outperforms current implementations with
50-700x speedups on the CIFAR-10 and MNIST datasets. These speedups enable, for
the first time, visualization of the neural network activations on the entire
ImageNet dataset - a feat that was previously computationally intractable. We
also demonstrate visualization performance in the NLP domain by visualizing the
GloVe embedding vectors. From these visualizations, we can draw interesting
conclusions about using the L2 metric in these embedding spaces. t-SNE-CUDA is
publicly available athttps://github.com/CannyLab/tsne-cuda