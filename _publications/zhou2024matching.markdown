---
layout: publication
title: Matching Query Image Against Selected Nerf Feature For Efficient And Scalable
  Localization
authors: Huaiji Zhou, Bing Wang, Changhao Chen
conference: Arxiv
year: 2024
bibkey: zhou2024matching
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.11766'}]
tags: ["Efficiency", "Scalability"]
short_authors: Huaiji Zhou, Bing Wang, Changhao Chen
---
Neural implicit representations such as NeRF have revolutionized 3D scene
representation with photo-realistic quality. However, existing methods for
visual localization within NeRF representations suffer from inefficiency and
scalability issues, particularly in large-scale environments. This work
proposes MatLoc-NeRF, a novel matching-based localization framework using
selected NeRF features. It addresses efficiency by employing a learnable
feature selection mechanism that identifies informative NeRF features for
matching with query images. This eliminates the need for all NeRF features or
additional descriptors, leading to faster and more accurate pose estimation. To
tackle large-scale scenes, MatLoc-NeRF utilizes a pose-aware scene partitioning
strategy. It ensures that only the most relevant NeRF sub-block generates key
features for a specific pose. Additionally, scene segmentation and a place
predictor provide fast coarse initial pose estimation. Evaluations on public
large-scale datasets demonstrate that MatLoc-NeRF achieves superior efficiency
and accuracy compared to existing NeRF-based localization methods.