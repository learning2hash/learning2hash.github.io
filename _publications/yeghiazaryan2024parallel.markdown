---
layout: publication
title: 'Parallel Watershed Partitioning: Gpu-based Hierarchical Image Segmentation'
authors: Varduhi Yeghiazaryan, Yeva Gabrielyan, Irina Voiculescu
conference: Arxiv
year: 2024
bibkey: yeghiazaryan2024parallel
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.08946'}]
tags: ["Efficiency", "Image Retrieval", "Scalability"]
short_authors: Varduhi Yeghiazaryan, Yeva Gabrielyan, Irina Voiculescu
---
Many image processing applications rely on partitioning an image into
disjoint regions whose pixels are 'similar.' The watershed and waterfall
transforms are established mathematical morphology pixel clustering techniques.
They are both relevant to modern applications where groups of pixels are to be
decided upon in one go, or where adjacency information is relevant. We
introduce three new parallel partitioning algorithms for GPUs. By repeatedly
applying watershed algorithms, we produce waterfall results which form a
hierarchy of partition regions over an input image. Our watershed algorithms
attain competitive execution times in both 2D and 3D, processing an 800
megavoxel image in less than 1.4 sec. We also show how to use this fully
deterministic image partitioning as a pre-processing step to machine learning
based semantic segmentation. This replaces the role of superpixel algorithms,
and results in comparable accuracy and faster training times.