---
layout: publication
title: 'Deepm: A Deep Part-based Model For Object Detection And Semantic Part Localization'
authors: Jun Zhu, Xianjie Chen, Alan L. Yuille
conference: Arxiv
year: 2015
bibkey: zhu2015deepm
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.07131'}]
tags: []
short_authors: Jun Zhu, Xianjie Chen, Alan L. Yuille
---
In this paper, we propose a deep part-based model (DeePM) for symbiotic
object detection and semantic part localization. For this purpose, we annotate
semantic parts for all 20 object categories on the PASCAL VOC 2012 dataset,
which provides information on object pose, occlusion, viewpoint and
functionality. DeePM is a latent graphical model based on the state-of-the-art
R-CNN framework, which learns an explicit representation of the object-part
configuration with flexible type sharing (e.g., a sideview horse head can be
shared by a fully-visible sideview horse and a highly truncated sideview horse
with head and neck only). For comparison, we also present an end-to-end
Object-Part (OP) R-CNN which learns an implicit feature representation for
jointly mapping an image ROI to the object and part bounding boxes. We evaluate
the proposed methods for both the object and part detection performance on
PASCAL VOC 2012, and show that DeePM consistently outperforms OP R-CNN in
detecting objects and parts. In addition, it obtains superior performance to
Fast and Faster R-CNNs in object detection.