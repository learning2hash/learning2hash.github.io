---
layout: publication
title: Deformable Radial Kernel Splatting
authors: Yi-Hua Huang, Ming-Xian Lin, Yang-Tian Sun, Ziyi Yang, Xiaoyang Lyu, Yan-Pei
  Cao, Xiaojuan Qi
conference: Arxiv
year: 2024
bibkey: huang2024deformable
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.11752'}]
tags: []
short_authors: Huang et al.
---
Recently, Gaussian splatting has emerged as a robust technique for
representing 3D scenes, enabling real-time rasterization and high-fidelity
rendering. However, Gaussians' inherent radial symmetry and smoothness
constraints limit their ability to represent complex shapes, often requiring
thousands of primitives to approximate detailed geometry. We introduce
Deformable Radial Kernel (DRK), which extends Gaussian splatting into a more
general and flexible framework. Through learnable radial bases with adjustable
angles and scales, DRK efficiently models diverse shape primitives while
enabling precise control over edge sharpness and boundary curvature. iven DRK's
planar nature, we further develop accurate ray-primitive intersection
computation for depth sorting and introduce efficient kernel culling strategies
for improved rasterization efficiency. Extensive experiments demonstrate that
DRK outperforms existing methods in both representation efficiency and
rendering quality, achieving state-of-the-art performance while dramatically
reducing primitive count.