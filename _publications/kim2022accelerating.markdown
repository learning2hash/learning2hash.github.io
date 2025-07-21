---
layout: publication
title: Accelerating Large-Scale Graph-based Nearest Neighbor Search on a Computational
  Storage Platform
authors: Kim et al.
conference: IEEE Transactions on Computers
year: 2022
bibkey: kim2022accelerating
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.05241'}]
tags: ["Graph-Based-ANN", "Scalability"]
---
K-nearest neighbor search is one of the fundamental tasks in various
applications and the hierarchical navigable small world (HNSW) has recently
drawn attention in large-scale cloud services, as it easily scales up the
database while offering fast search. On the other hand, a computational storage
device (CSD) that combines programmable logic and storage modules on a single
board becomes popular to address the data bandwidth bottleneck of modern
computing systems. In this paper, we propose a computational storage platform
that can accelerate a large-scale graph-based nearest neighbor search algorithm
based on SmartSSD CSD. To this end, we modify the algorithm more amenable on
the hardware and implement two types of accelerators using HLS- and RTL-based
methodology with various optimization methods. In addition, we scale up the
proposed platform to have 4 SmartSSDs and apply graph parallelism to boost the
system performance further. As a result, the proposed computational storage
platform achieves 75.59 query per second throughput for the SIFT1B dataset at
258.66W power dissipation, which is 12.83x and 17.91x faster and 10.43x and
24.33x more energy efficient than the conventional CPU-based and GPU-based
server platform, respectively. With multi-terabyte storage and custom
acceleration capability, we believe that the proposed computational storage
platform is a promising solution for cost-sensitive cloud datacenters.