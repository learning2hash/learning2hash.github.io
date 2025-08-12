---
layout: publication
title: 'TRUST: Triangle Counting Reloaded On Gpus'
authors: Santosh Pandey, Zhibin Wang, Sheng Zhong, Chen Tian, Bolong Zheng, Xiaoye
  Li, Lingda Li, Adolfy Hoisie, Caiwen Ding, Dong Li, Hang Liu
conference: IEEE Transactions on Parallel and Distributed Systems
year: 2021
bibkey: pandey2021trust
citations: 27
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.08053'}]
tags: ["Scalability"]
short_authors: Pandey et al.
---
Triangle counting is a building block for a wide range of graph applications.
Traditional wisdom suggests that i) hashing is not suitable for triangle
counting, ii) edge-centric triangle counting beats vertex-centric design, and
iii) communication-free and workload balanced graph partitioning is a grand
challenge for triangle counting. On the contrary, we advocate that i) hashing
can help the key operations for scalable triangle counting on Graphics
Processing Units (GPUs), i.e., list intersection and graph partitioning,
ii)vertex-centric design reduces both hash table construction cost and memory
consumption, which is limited on GPUs. In addition, iii) we exploit graph and
workload collaborative, and hashing-based 2D partitioning to scale
vertex-centric triangle counting over 1,000 GPUswith sustained scalability. In
this work, we present TRUST which performs triangle counting with the hash
operation and vertex-centric mechanism at the core. To the best of our
knowledge, TRUSTis the first work that achieves over one trillion Traversed
Edges Per Second (TEPS) rate for triangle counting.