---
layout: publication
title: Leveraging Swin Transformer For Local-to-global Weakly Supervised Semantic
  Segmentation
authors: Rozhan Ahmadi, Shohreh Kasaei
conference: 2024 13th Iranian/3rd International Machine Vision and Image Processing
  Conference (MVIP)
year: 2024
bibkey: ahmadi2024leveraging
citations: 0
additional_links: [{name: Code, url: 'https://github.com/RozhanAhmadi/SWTformer'},
  {name: Paper, url: 'https://arxiv.org/abs/2401.17828'}]
tags: ["Supervised"]
short_authors: Rozhan Ahmadi, Shohreh Kasaei
---
In recent years, weakly supervised semantic segmentation using image-level
labels as supervision has received significant attention in the field of
computer vision. Most existing methods have addressed the challenges arising
from the lack of spatial information in these labels by focusing on
facilitating supervised learning through the generation of pseudo-labels from
class activation maps (CAMs). Due to the localized pattern detection of CNNs,
CAMs often emphasize only the most discriminative parts of an object, making it
challenging to accurately distinguish foreground objects from each other and
the background. Recent studies have shown that Vision Transformer (ViT)
features, due to their global view, are more effective in capturing the scene
layout than CNNs. However, the use of hierarchical ViTs has not been
extensively explored in this field. This work explores the use of Swin
Transformer by proposing "SWTformer" to enhance the accuracy of the initial
seed CAMs by bringing local and global views together. SWTformer-V1 generates
class probabilities and CAMs using only the patch tokens as features.
SWTformer-V2 incorporates a multi-scale feature fusion mechanism to extract
additional information and utilizes a background-aware mechanism to generate
more accurate localization maps with improved cross-object discrimination.
Based on experiments on the PascalVOC 2012 dataset, SWTformer-V1 achieves a
0.98% mAP higher localization accuracy, outperforming state-of-the-art models.
It also yields comparable performance by 0.82% mIoU on average higher than
other methods in generating initial localization maps, depending only on the
classification network. SWTformer-V2 further improves the accuracy of the
generated seed CAMs by 5.32% mIoU, further proving the effectiveness of the
local-to-global view provided by the Swin transformer. Code available at:
https://github.com/RozhanAhmadi/SWTformer