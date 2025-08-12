---
layout: publication
title: Zero-shot Point Cloud Segmentation By Transferring Geometric Primitives
authors: Runnan Chen, Xinge Zhu, Nenglun Chen, Wei Li, Yuexin Ma, Ruigang Yang, Wenping
  Wang
conference: Arxiv
year: 2022
bibkey: chen2022zero
citations: 6
additional_links: [{name: Code, url: 'https://github.com/runnanchen/Zero-Shot-Point-Cloud-Segmentation)'},
  {name: Paper, url: 'https://arxiv.org/abs/2210.09923'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Chen et al.
---
We investigate transductive zero-shot point cloud semantic segmentation,
where the network is trained on seen objects and able to segment unseen
objects. The 3D geometric elements are essential cues to imply a novel 3D
object type. However, previous methods neglect the fine-grained relationship
between the language and the 3D geometric elements. To this end, we propose a
novel framework to learn the geometric primitives shared in seen and unseen
categories' objects and employ a fine-grained alignment between language and
the learned geometric primitives. Therefore, guided by language, the network
recognizes the novel objects represented with geometric primitives.
Specifically, we formulate a novel point visual representation, the similarity
vector of the point's feature to the learnable prototypes, where the prototypes
automatically encode geometric primitives via back-propagation. Besides, we
propose a novel Unknown-aware InfoNCE Loss to fine-grained align the visual
representation with language. Extensive experiments show that our method
significantly outperforms other state-of-the-art methods in the harmonic
mean-intersection-over-union (hIoU), with the improvement of 17.8%, 30.4%,
9.2% and 7.9% on S3DIS, ScanNet, SemanticKITTI and nuScenes datasets,
respectively. Codes are available
(https://github.com/runnanchen/Zero-Shot-Point-Cloud-Segmentation)