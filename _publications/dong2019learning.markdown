---
layout: publication
title: Learning Space Partitions For Nearest Neighbor Search
authors: Dong Yihe, Indyk Piotr, Razenshteyn Ilya, Wagner Tal
conference: "Arxiv"
year: 2019
bibkey: dong2019learning
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1901.08544"}
tags: ['ARXIV', 'FOCS', 'Graph', 'LSH', 'Quantisation', 'Supervised']
---
Space partitions of \{\{ '\{\{' \}\}\mathbb\{R\}^d\{\{ '\}\}' \}\} underlie a vast and important class of fast nearest neighbor search (NNS) algorithms. Inspired by recent theoretical work on NNS for general metric spaces [Andoni, Naor, Nikolov, Razenshteyn, Waingarten STOC 2018, FOCS 2018], we develop a new framework for building space partitions reducing the problem to balanced graph partitioning followed by supervised classification. We instantiate this general approach with the KaHIP graph partitioner [Sanders, Schulz SEA 2013] and neural networks, respectively, to obtain a new partitioning procedure called Neural Locality-Sensitive Hashing (Neural LSH). On several standard benchmarks for NNS, our experiments show that the partitions obtained by Neural LSH consistently outperform partitions found by quantization-based and tree-based methods as well as classic, data-oblivious LSH.
