---
layout: publication
title: Anti-aliasing Semantic Reconstruction For Few-shot Semantic Segmentation
authors: Binghao Liu, Yao Ding, Jianbin Jiao, Xiangyang Ji, Qixiang Ye
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2021
bibkey: liu2021anti
citations: 41
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.00184'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Encouraging progress in few-shot semantic segmentation has been made by
leveraging features learned upon base classes with sufficient training data to
represent novel classes with few-shot examples. However, this feature sharing
mechanism inevitably causes semantic aliasing between novel classes when they
have similar compositions of semantic concepts. In this paper, we reformulate
few-shot segmentation as a semantic reconstruction problem, and convert base
class features into a series of basis vectors which span a class-level semantic
space for novel class reconstruction. By introducing contrastive loss, we
maximize the orthogonality of basis vectors while minimizing semantic aliasing
between classes. Within the reconstructed representation space, we further
suppress interference from other classes by projecting query features to the
support vector for precise semantic activation. Our proposed approach, referred
to as anti-aliasing semantic reconstruction (ASR), provides a systematic yet
interpretable solution for few-shot learning problems. Extensive experiments on
PASCAL VOC and MS COCO datasets show that ASR achieves strong results compared
with the prior works.