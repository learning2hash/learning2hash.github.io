---
layout: publication
title: Collapse-aware Triplet Decoupling For Adversarially Robust Image Retrieval
authors: Qiwei Tian, Chenhao Lin, Zhengyu Zhao, Qian Li, Chao Shen
conference: Arxiv
year: 2023
bibkey: tian2023collapse
citations: 0
additional_links: [{name: Code, url: 'https://github.com/michaeltian108/CA-TRIDE'},
  {name: Paper, url: 'https://arxiv.org/abs/2312.07364'}]
tags: ["Distance Metric Learning", "Image Retrieval", "Robustness"]
short_authors: Tian et al.
---
Adversarial training has achieved substantial performance in defending image
retrieval against adversarial examples. However, existing studies in deep
metric learning (DML) still suffer from two major limitations: weak adversary
and model collapse. In this paper, we address these two limitations by
proposing Collapse-Aware TRIplet DEcoupling (CA-TRIDE). Specifically, TRIDE
yields a stronger adversary by spatially decoupling the perturbation targets
into the anchor and the other candidates. Furthermore, CA prevents the
consequential model collapse, based on a novel metric, collapseness, which is
incorporated into the optimization of perturbation. We also identify two
drawbacks of the existing robustness metric in image retrieval and propose a
new metric for a more reasonable robustness evaluation. Extensive experiments
on three datasets demonstrate that CA-TRIDE outperforms existing defense
methods in both conventional and new metrics. Codes are available at
https://github.com/michaeltian108/CA-TRIDE.