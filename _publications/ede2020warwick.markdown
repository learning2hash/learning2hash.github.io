---
layout: publication
title: 'Warwick Electron Microscopy Datasets'
authors: Jeffrey M. Ede
conference: "Mach. Learn. Sci. Technol. 1 045003 (2020)"
year: 2020
citations: 11
bibkey: ede2020warwick
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2003.01113'}
  - {name: "Code", url: 'https://github.com/Jeffrey-Ede/datasets'}
tags: ['Cross-Modal', 'Deep', 'Model Design', 'Benchmarks and Tools', 'Datasets', 'Vector Indexing', 'Has Code', 'Supervised', 'Applications']
---
Large, carefully partitioned datasets are essential to train neural networks
and standardize performance benchmarks. As a result, we have set up new
repositories to make our electron microscopy datasets available to the wider
community. There are three main datasets containing 19769 scanning transmission
electron micrographs, 17266 transmission electron micrographs, and 98340
simulated exit wavefunctions, and multiple variants of each dataset for
different applications. To visualize image datasets, we trained variational
autoencoders to encode data as 64-dimensional multivariate normal
distributions, which we cluster in two dimensions by t-distributed stochastic
neighbor embedding. In addition, we have improved dataset visualization with
variational autoencoders by introducing encoding normalization and
regularization, adding an image gradient loss, and extending t-distributed
stochastic neighbor embedding to account for encoded standard deviations. Our
datasets, source code, pretrained models, and interactive visualizations are
openly available at https://github.com/Jeffrey-Ede/datasets.
