---
layout: publication
title: Bio-inspired Hashing For Unsupervised Similarity Search
authors: Chaitanya K. Ryali, John J. Hopfield, Leopold Grinberg, Dmitry Krotov
conference: Proceedings of the International Conference on Machine Learning 2020 pp.8739-8750
year: 2020
citations: 4
bibkey: ryali2020bio
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.04907'}]
tags: [Unsupervised, ANN Search, Hashing Methods, Efficient Learning]
---
The fruit fly Drosophila's olfactory circuit has inspired a new locality
sensitive hashing (LSH) algorithm, FlyHash. In contrast with classical LSH
algorithms that produce low dimensional hash codes, FlyHash produces sparse
high-dimensional hash codes and has also been shown to have superior empirical
performance compared to classical LSH algorithms in similarity search. However,
FlyHash uses random projections and cannot learn from data. Building on
inspiration from FlyHash and the ubiquity of sparse expansive representations
in neurobiology, our work proposes a novel hashing algorithm BioHash that
produces sparse high dimensional hash codes in a data-driven manner. We show
that BioHash outperforms previously published benchmarks for various hashing
methods. Since our learning algorithm is based on a local and biologically
plausible synaptic plasticity rule, our work provides evidence for the proposal
that LSH might be a computational reason for the abundance of sparse expansive
motifs in a variety of biological systems. We also propose a convolutional
variant BioConvHash that further improves performance. From the perspective of
computer science, BioHash and BioConvHash are fast, scalable and yield
compressed binary representations that are useful for similarity search.