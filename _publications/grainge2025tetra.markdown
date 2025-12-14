---
layout: publication
title: 'Tetra-vpr: A Ternary Transformer Approach For Compact Visual Place Recognition'
authors: Oliver Grainge, Michael Milford, Indu Bodala, Sarvapali D. Ramchurn, Shoaib
  Ehsan
conference: IEEE Robotics and Automation Letters
year: 2025
bibkey: grainge2025tetra
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2503.02511'}]
tags: [Evaluation]
short_authors: Grainge et al.
---
Visual Place Recognition (VPR) localizes a query image by matching it against
a database of geo-tagged reference images, making it essential for navigation
and mapping in robotics. Although Vision Transformer (ViT) solutions deliver
high accuracy, their large models often exceed the memory and compute budgets
of resource-constrained platforms such as drones and mobile robots. To address
this issue, we propose TeTRA, a ternary transformer approach that progressively
quantizes the ViT backbone to 2-bit precision and binarizes its final embedding
layer, offering substantial reductions in model size and latency. A carefully
designed progressive distillation strategy preserves the representational power
of a full-precision teacher, allowing TeTRA to retain or even surpass the
accuracy of uncompressed convolutional counterparts, despite using fewer
resources. Experiments on standard VPR benchmarks demonstrate that TeTRA
reduces memory consumption by up to 69% compared to efficient baselines, while
lowering inference latency by 35%, with either no loss or a slight improvement
in recall@1. These gains enable high-accuracy VPR on power-constrained,
memory-limited robotic platforms, making TeTRA an appealing solution for
real-world deployment.