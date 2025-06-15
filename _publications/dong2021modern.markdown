---
layout: publication
title: 'ASH: A Modern Framework For Parallel Spatial Hashing In 3D Perception'
authors: Wei Dong, Yixing Lao, Michael Kaess, Vladlen Koltun
conference: "Arxiv"
year: 2021
citations: 8
bibkey: dong2021modern
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2110.00511'}
  - {name: "Code", url: 'http://www.open3d.org)'}
tags: ['Hashing Methods', 'Applications', 'Evaluation Metrics', 'Tools and Libraries', 'Hashing Fundamentals', 'Has Code']
---
We present ASH, a modern and high-performance framework for parallel spatial
hashing on GPU. Compared to existing GPU hash map implementations, ASH achieves
higher performance, supports richer functionality, and requires fewer lines of
code (LoC) when used for implementing spatially varying operations from
volumetric geometry reconstruction to differentiable appearance reconstruction.
Unlike existing GPU hash maps, the ASH framework provides a versatile tensor
interface, hiding low-level details from the users. In addition, by decoupling
the internal hashing data structures and key-value data in buffers, we offer
direct access to spatially varying data via indices, enabling seamless
integration to modern libraries such as PyTorch. To achieve this, we 1) detach
stored key-value data from the low-level hash map implementation; 2) bridge the
pointer-first low level data structures to index-first high-level tensor
interfaces via an index heap; 3) adapt both generic and non-generic
integer-only hash map implementations as backends to operate on
multi-dimensional keys. We first profile our hash map against state-of-the-art
hash maps on synthetic data to show the performance gain from this
architecture. We then show that ASH can consistently achieve higher performance
on various large-scale 3D perception tasks with fewer LoC by showcasing several
applications, including 1) point cloud voxelization, 2) retargetable volumetric
scene reconstruction, 3) non-rigid point cloud registration and volumetric
deformation, and 4) spatially varying geometry and appearance refinement. ASH
and its example applications are open sourced in Open3D
(http://www.open3d.org).
