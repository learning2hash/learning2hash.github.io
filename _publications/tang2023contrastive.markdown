---
layout: publication
title: Contrastive Grouping With Transformer For Referring Image Segmentation
authors: Jiajin Tang, Ge Zheng, Cheng Shi, Sibei Yang
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: tang2023contrastive
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.01017'}]
tags: ["CVPR"]
short_authors: Tang et al.
---
Referring image segmentation aims to segment the target referent in an image
conditioning on a natural language expression. Existing one-stage methods
employ per-pixel classification frameworks, which attempt straightforwardly to
align vision and language at the pixel level, thus failing to capture critical
object-level information. In this paper, we propose a mask classification
framework, Contrastive Grouping with Transformer network (CGFormer), which
explicitly captures object-level information via token-based querying and
grouping strategy. Specifically, CGFormer first introduces learnable query
tokens to represent objects and then alternately queries linguistic features
and groups visual features into the query tokens for object-aware cross-modal
reasoning. In addition, CGFormer achieves cross-level interaction by jointly
updating the query tokens and decoding masks in every two consecutive layers.
Finally, CGFormer cooperates contrastive learning to the grouping strategy to
identify the token and its mask corresponding to the referent. Experimental
results demonstrate that CGFormer outperforms state-of-the-art methods in both
segmentation and generalization settings consistently and significantly.