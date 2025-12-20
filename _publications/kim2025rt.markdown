---
layout: publication
title: 'RT-HDIST: Ray-tracing Core-based Hausdorff Distance Computation'
authors: Youngwoo Kim, Jaehong Lee, Duksu Kim
conference: Computer Graphics Forum
year: 2025
bibkey: kim2025rt
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.13436'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Scalability"]
short_authors: Youngwoo Kim, Jaehong Lee, Duksu Kim
---
The Hausdorff distance is a fundamental metric with widespread applications
across various fields. However, its computation remains computationally
expensive, especially for large-scale datasets. In this work, we present
RT-HDIST, the first Hausdorff distance algorithm accelerated by ray-tracing
cores (RT-cores). By reformulating the Hausdorff distance problem as a series
of nearest-neighbor searches and introducing a novel quantized index space,
RT-HDIST achieves significant reductions in computational overhead while
maintaining exact results. Extensive benchmarks demonstrate up to a
two-order-of-magnitude speedup over prior state-of-the-art methods,
underscoring RT-HDIST's potential for real-time and large-scale applications.