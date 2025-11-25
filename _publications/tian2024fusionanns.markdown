---
layout: publication
title: 'Fusionanns: An Efficient CPU/GPU Cooperative Processing Architecture For Billion-scale
  Approximate Nearest Neighbor Search'
authors: Bing Tian, Haikun Liu, Yuhang Tang, Shihai Xiao, Zhuohui Duan, Xiaofei Liao,
  Xuecang Zhang, Junhua Zhu, Yu Zhang
conference: Arxiv
year: 2024
bibkey: tian2024fusionanns
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.16576'}]
tags: ["Efficiency", "Hybrid ANN Methods", "Large Scale Search", "Re-Ranking", "Scalability"]
short_authors: Tian et al.
---
Approximate nearest neighbor search (ANNS) has emerged as a crucial component
of database and AI infrastructure. Ever-increasing vector datasets pose
significant challenges in terms of performance, cost, and accuracy for ANNS
services. None of modern ANNS systems can address these issues simultaneously.
We present FusionANNS, a high-throughput, low-latency, cost-efficient, and
high-accuracy ANNS system for billion-scale datasets using SSDs and only one
entry-level GPU. The key idea of FusionANNS lies in CPU/GPU collaborative
filtering and re-ranking mechanisms, which significantly reduce I/O operations
across CPUs, GPU, and SSDs to break through the I/O performance bottleneck.
Specifically, we propose three novel designs: (1) multi-tiered indexing to
avoid data swapping between CPUs and GPU, (2) heuristic re-ranking to eliminate
unnecessary I/Os and computations while guaranteeing high accuracy, and (3)
redundant-aware I/O deduplication to further improve I/O efficiency. We
implement FusionANNS and compare it with the state-of-the-art SSD-based ANNS
system -- SPANN and GPU-accelerated in-memory ANNS system -- RUMMY.
Experimental results show that FusionANNS achieves 1) 9.4-13.1X higher query
per second (QPS) and 5.7-8.8X higher cost efficiency compared with SPANN; 2)
and 2-4.9X higher QPS and 2.3-6.8X higher cost efficiency compared with RUMMY,
while guaranteeing low latency and high accuracy.