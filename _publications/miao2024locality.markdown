---
layout: publication
title: Locality-sensitive Hashing-based Efficient Point Transformer With Applications In High-energy Physics
authors: Miao Siqi, Lu Zhiyuan, Liu Mia, Duarte Javier, Li Pan
conference: "Arxiv"
year: 2024
bibkey: miao2024locality
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2402.12535"}
  - {name: "Code", url: "https://github.com/Graph-COM/HEPT"}
tags: ['ARXIV', 'Deep Learning', 'Graph', 'Has Code', 'LSH', 'Supervised']
---
This study introduces a novel transformer model optimized for large-scale point cloud processing in scientific domains such as high-energy physics (HEP) and astrophysics. Addressing the limitations of graph neural networks and standard transformers, our model integrates local inductive bias and achieves near-linear complexity with hardware-friendly regular operations. One contribution of this work is the quantitative analysis of the error-complexity tradeoff of various sparsification techniques for building efficient transformers. Our findings highlight the superiority of using locality-sensitive hashing (LSH), especially OR &amp; AND-construction LSH, in kernel approximation for large-scale point cloud data with local inductive bias. Based on this finding, we propose LSH-based Efficient Point Transformer (HEPT), which combines E$^2$LSH with OR &amp; AND constructions and is built upon regular computations. HEPT demonstrates remarkable performance on two critical yet time-consuming HEP tasks, significantly outperforming existing GNNs and transformers in accuracy and computational speed, marking a significant advancement in geometric deep learning and large-scale scientific data processing. Our code is available at https://github.com/Graph-COM/HEPT.
