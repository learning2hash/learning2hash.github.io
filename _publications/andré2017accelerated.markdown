---
layout: publication
title: Accelerated Nearest Neighbor Search With Quick ADC
authors: André Fabien Technicolor, Kermarrec Anne-marie Inria, Scouarnec Nicolas Le Technicolor
conference: "Arxiv"
year: 2017
bibkey: andré2017accelerated
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1704.07355"}
tags: ['ARXIV', 'Quantisation']
---
Efficient Nearest Neighbor (NN) search in high-dimensional spaces is a foundation of many multimedia retrieval systems. Because it offers low responses times, Product Quantization (PQ) is a popular solution. PQ compresses high-dimensional vectors into short codes using several sub-quantizers, which enables in-RAM storage of large databases. This allows fast answers to NN queries, without accessing the SSD or HDD. The key feature of PQ is that it can compute distances between short codes and high-dimensional vectors using cache-resident lookup tables. The efficiency of this technique, named Asymmetric Distance Computation (ADC), remains limited because it performs many cache accesses. In this paper, we introduce Quick ADC, a novel technique that achieves a 3 to 6 times speedup over ADC by exploiting Single Instruction Multiple Data (SIMD) units available in current CPUs. Efficiently exploiting SIMD requires algorithmic changes to the ADC procedure. Namely, Quick ADC relies on two key modifications of ADC: (i) the use 4-bit sub-quantizers instead of the standard 8-bit sub-quantizers and (ii) the quantization of floating-point distances. This allows Quick ADC to exceed the performance of state-of-the-art systems, e.g., it achieves a Recall@100 of 0.94 in 3.4 ms on 1 billion SIFT descriptors (128-bit codes).
