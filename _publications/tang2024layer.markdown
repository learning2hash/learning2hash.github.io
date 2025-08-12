---
layout: publication
title: Layer-wise Feature Metric Of Semantic-pixel Matching For Few-shot Learning
authors: Hao Tang, Junhao Lu, Guoheng Huang, Ming Li, Xuhang Chen, Guo Zhong, Zhengguang
  Tan, Zinuo Li
conference: Arxiv
year: 2024
bibkey: tang2024layer
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Halo2Tang/Code-for-LWFM-SPM'},
  {name: Paper, url: 'https://arxiv.org/abs/2411.06363'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Tang et al.
---
In Few-Shot Learning (FSL), traditional metric-based approaches often rely on
global metrics to compute similarity. However, in natural scenes, the spatial
arrangement of key instances is often inconsistent across images. This spatial
misalignment can result in mismatched semantic pixels, leading to inaccurate
similarity measurements. To address this issue, we propose a novel method
called the Layer-Wise Features Metric of Semantic-Pixel Matching (LWFM-SPM) to
make finer comparisons. Our method enhances model performance through two key
modules: (1) the Layer-Wise Embedding (LWE) Module, which refines the
cross-correlation of image pairs to generate well-focused feature maps for each
layer; (2)the Semantic-Pixel Matching (SPM) Module, which aligns critical
pixels based on semantic embeddings using an assignment algorithm. We conducted
extensive experiments to evaluate our method on four widely used few-shot
classification benchmarks: miniImageNet, tieredImageNet, CUB-200-2011, and
CIFAR-FS. The results indicate that LWFM-SPM achieves competitive performance
across these benchmarks. Our code will be publicly available on
https://github.com/Halo2Tang/Code-for-LWFM-SPM.