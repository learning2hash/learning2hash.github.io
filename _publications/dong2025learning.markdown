---
layout: publication
title: Learning Space Partitions For Nearest Neighbor Search
authors: Dong Yihe, Indyk, Razenshteyn, Wagner
conference: No Venue
year: 2025
bibkey: dong2025learning
additional_links: [{name: Paper, url: 'https://openreview.net/attachment?id=rkenmREFDr&name=original_pdf'}]
tags: [Quantization, Evaluation, Tools & Libraries, HASHING Methods, Locality Sensitive
    HASHING]
---
Space partitions of underlie a vast and important
class of fast nearest neighbor search (NNS) algorithms. Inspired by recent theoretical work on NNS for general metric spaces (Andoni et al. 2018b,c), we develop a new framework for building space partitions reducing the problem to balanced graph partitioning followed by supervised classification.
We instantiate this general approach with the KaHIP graph partitioner (Sanders and Schulz 2013) and neural networks, respectively, to obtain a new partitioning procedure called Neural Locality-Sensitive Hashing (Neural LSH). On several standard benchmarks for NNS (Aumuller et al. 2017), our experiments show that the partitions obtained by Neural LSH consistently outperform partitions found by quantization-based and tree-based methods as well as classic, data-oblivious LSH.