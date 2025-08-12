---
layout: publication
title: Hyperbolic Contrastive Learning For Visual Representations Beyond Objects
authors: Songwei Ge, Shlok Mishra, Simon Kornblith, Chun-liang Li, David Jacobs
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: ge2022hyperbolic
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.00653'}]
tags: ["CVPR", "Self-Supervised"]
short_authors: Ge et al.
---
Although self-/un-supervised methods have led to rapid progress in visual
representation learning, these methods generally treat objects and scenes using
the same lens. In this paper, we focus on learning representations for objects
and scenes that preserve the structure among them.
  Motivated by the observation that visually similar objects are close in the
representation space, we argue that the scenes and objects should instead
follow a hierarchical structure based on their compositionality. To exploit
such a structure, we propose a contrastive learning framework where a Euclidean
loss is used to learn object representations and a hyperbolic loss is used to
encourage representations of scenes to lie close to representations of their
constituent objects in a hyperbolic space. This novel hyperbolic objective
encourages the scene-object hypernymy among the representations by optimizing
the magnitude of their norms. We show that when pretraining on the COCO and
OpenImages datasets, the hyperbolic loss improves downstream performance of
several baselines across multiple datasets and tasks, including image
classification, object detection, and semantic segmentation. We also show that
the properties of the learned representations allow us to solve various vision
tasks that involve the interaction between scenes and objects in a zero-shot
fashion. Our code can be found at
https://github.com/shlokk/HCL/tree/main/HCL.