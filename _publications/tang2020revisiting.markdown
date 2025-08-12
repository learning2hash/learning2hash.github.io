---
layout: publication
title: Revisiting Pose-normalization For Fine-grained Few-shot Recognition
authors: Luming Tang, Davis Wertheimer, Bharath Hariharan
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: tang2020revisiting
citations: 45
additional_links: [{name: Code, url: 'https://github.com/Tsingularity/PoseNorm_Fewshot'},
  {name: Paper, url: 'https://arxiv.org/abs/2004.00705'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Luming Tang, Davis Wertheimer, Bharath Hariharan
---
Few-shot, fine-grained classification requires a model to learn subtle,
fine-grained distinctions between different classes (e.g., birds) based on a
few images alone. This requires a remarkable degree of invariance to pose,
articulation and background. A solution is to use pose-normalized
representations: first localize semantic parts in each image, and then describe
images by characterizing the appearance of each part. While such
representations are out of favor for fully supervised classification, we show
that they are extremely effective for few-shot fine-grained classification.
With a minimal increase in model capacity, pose normalization improves accuracy
between 10 and 20 percentage points for shallow and deep architectures,
generalizes better to new domains, and is effective for multiple few-shot
algorithms and network backbones. Code is available at
https://github.com/Tsingularity/PoseNorm_Fewshot