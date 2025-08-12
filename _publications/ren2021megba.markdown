---
layout: publication
title: 'Megba: A Gpu-based Distributed Library For Large-scale Bundle Adjustment'
authors: Jie Ren, Wenteng Liang, Ran Yan, Luo Mai, Shiwen Liu, Xiao Liu
conference: Lecture Notes in Computer Science
year: 2022
bibkey: ren2021megba
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.01349'}]
tags: ["Scalability", "Tools & Libraries"]
short_authors: Ren et al.
---
Large-scale Bundle Adjustment (BA) requires massive memory and computation
resources which are difficult to be fulfilled by existing BA libraries. In this
paper, we propose MegBA, a GPU-based distributed BA library. MegBA can provide
massive aggregated memory by automatically partitioning large BA problems, and
assigning the solvers of sub-problems to parallel nodes. The parallel solvers
adopt distributed Precondition Conjugate Gradient and distributed Schur
Elimination, so that an effective solution, which can match the precision of
those computed by a single node, can be efficiently computed. To accelerate BA
computation, we implement end-to-end BA computation using high-performance
primitives available on commodity GPUs. MegBA exposes easy-to-use APIs that are
compatible with existing popular BA libraries. Experiments show that MegBA can
significantly outperform state-of-the-art BA libraries: Ceres (41.45\\(\times\\)),
RootBA (64.576\\(\times\\)) and DeepLM (6.769\\(\times\\)) in several large-scale BA
benchmarks. The code of MegBA is available at
https://github.com/MegviiRobot/MegBA.