---
layout: publication
title: 'See More And Know More: Zero-shot Point Cloud Segmentation Via Multi-modal
  Visual Data'
authors: Yuhang Lu, Qi Jiang, Runnan Chen, Yuenan Hou, Xinge Zhu, Yuexin Ma
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: lu2023see
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.10782'}]
tags: ["ICCV"]
short_authors: Lu et al.
---
Zero-shot point cloud segmentation aims to make deep models capable of
recognizing novel objects in point cloud that are unseen in the training phase.
Recent trends favor the pipeline which transfers knowledge from seen classes
with labels to unseen classes without labels. They typically align visual
features with semantic features obtained from word embedding by the supervision
of seen classes' annotations. However, point cloud contains limited information
to fully match with semantic features. In fact, the rich appearance information
of images is a natural complement to the textureless point cloud, which is not
well explored in previous literature. Motivated by this, we propose a novel
multi-modal zero-shot learning method to better utilize the complementary
information of point clouds and images for more accurate visual-semantic
alignment. Extensive experiments are performed in two popular benchmarks, i.e.,
SemanticKITTI and nuScenes, and our method outperforms current SOTA methods
with 52% and 49% improvement on average for unseen class mIoU, respectively.