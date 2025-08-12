---
layout: publication
title: Hierarchical Feature Embedding For Attribute Recognition
authors: Jie Yang, Jiarou Fan, Yiru Wang, Yige Wang, Weihao Gan, Lin Liu, Wei Wu
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2020
bibkey: yang2020hierarchical
citations: 48
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.11576'}]
tags: ["CVPR"]
short_authors: Yang et al.
---
Attribute recognition is a crucial but challenging task due to viewpoint
changes, illumination variations and appearance diversities, etc. Most of
previous work only consider the attribute-level feature embedding, which might
perform poorly in complicated heterogeneous conditions. To address this
problem, we propose a hierarchical feature embedding (HFE) framework, which
learns a fine-grained feature embedding by combining attribute and ID
information. In HFE, we maintain the inter-class and intra-class feature
embedding simultaneously. Not only samples with the same attribute but also
samples with the same ID are gathered more closely, which could restrict the
feature embedding of visually hard samples with regard to attributes and
improve the robustness to variant conditions. We establish this hierarchical
structure by utilizing HFE loss consisted of attribute-level and ID-level
constraints. We also introduce an absolute boundary regularization and a
dynamic loss weight as supplementary components to help build up the feature
embedding. Experiments show that our method achieves the state-of-the-art
results on two pedestrian attribute datasets and a facial attribute dataset.