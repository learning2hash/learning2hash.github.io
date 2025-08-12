---
layout: publication
title: 'MLIP: Medical Language-image Pre-training With Masked Local Representation
  Learning'
authors: Jiarun Liu, Hong-Yu Zhou, Cheng Li, Weijian Huang, Hao Yang, Yong Liang,
  Shanshan Wang
conference: 2024 IEEE International Symposium on Biomedical Imaging (ISBI)
year: 2024
bibkey: liu2024mlip
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.01591'}]
tags: ["Self-Supervised"]
short_authors: Liu et al.
---
Existing contrastive language-image pre-training aims to learn a joint
representation by matching abundant image-text pairs. However, the number of
image-text pairs in medical datasets is usually orders of magnitude smaller
than that in natural datasets. Besides, medical image-text pairs often involve
numerous complex fine-grained correspondences. This paper aims to enhance the
data efficiency by introducing multiple-to-multiple local relationship modeling
to capture denser supervisions. More specifically, we propose a Medical
Language-Image Pre-training (MLIP) framework, which exploits the limited
image-text medical data more efficiently through patch-sentence matching.
Furthermore, we introduce a masked contrastive learning strategy with semantic
integrity estimation to reduce redundancy in images while preserving the
underlying semantics. Our evaluation results show that MLIP outperforms
previous work in zero/few-shot classification and few-shot segmentation tasks
by a large margin.