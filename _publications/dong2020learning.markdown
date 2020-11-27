---
layout: publication
title: "Learning Space Partitions for Nearest Neighbor Search"
authors: Yihe Dong, Piotr Indyk, Ilya Razenshteyn, Tal Wagner
conference: ICLR
year: 2020
bibkey: dong2020learning
additional_links:
   - {name: "PDF", url: "https://openreview.net/attachment?id=rkenmREFDr&name=original_pdf"}
   - {name: "Code", url: "https://anonymous.4open.science/r/cdd789a8-818c-4675-98fd-39f8da656129/"}
   - {name: "Openreview", url: "https://openreview.net/forum?id=rkenmREFDr"}
---
Space partitions of underlie a vast and important
class of fast nearest neighbor search (NNS) algorithms. Inspired by recent theoretical work on NNS for general metric spaces (Andoni et al. 2018b,c), we develop a new framework for building space partitions reducing the problem to balanced graph partitioning followed by supervised classification.
We instantiate this general approach with the KaHIP graph partitioner (Sanders and Schulz 2013) and neural networks, respectively, to obtain a new partitioning procedure called Neural Locality-Sensitive Hashing (Neural LSH). On several standard benchmarks for NNS (Aumuller et al. 2017), our experiments show that the partitions obtained by Neural LSH consistently outperform partitions found by quantization-based and tree-based methods as well as classic, data-oblivious LSH.

