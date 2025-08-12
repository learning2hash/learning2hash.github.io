---
layout: publication
title: 'Object2scene: Putting Objects In Context For Open-vocabulary 3D Detection'
authors: Chenming Zhu, Wenwei Zhang, Tai Wang, Xihui Liu, Kai Chen
conference: Arxiv
year: 2023
bibkey: zhu2023object2scene
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.09456'}]
tags: []
short_authors: Zhu et al.
---
Point cloud-based open-vocabulary 3D object detection aims to detect 3D
categories that do not have ground-truth annotations in the training set. It is
extremely challenging because of the limited data and annotations (bounding
boxes with class labels or text descriptions) of 3D scenes. Previous approaches
leverage large-scale richly-annotated image datasets as a bridge between 3D and
category semantics but require an extra alignment process between 2D images and
3D points, limiting the open-vocabulary ability of 3D detectors. Instead of
leveraging 2D images, we propose Object2Scene, the first approach that
leverages large-scale large-vocabulary 3D object datasets to augment existing
3D scene datasets for open-vocabulary 3D object detection. Object2Scene inserts
objects from different sources into 3D scenes to enrich the vocabulary of 3D
scene datasets and generates text descriptions for the newly inserted objects.
We further introduce a framework that unifies 3D detection and visual
grounding, named L3Det, and propose a cross-domain category-level contrastive
learning approach to mitigate the domain gap between 3D objects from different
datasets. Extensive experiments on existing open-vocabulary 3D object detection
benchmarks show that Object2Scene obtains superior performance over existing
methods. We further verify the effectiveness of Object2Scene on a new benchmark
OV-ScanNet-200, by holding out all rare categories as novel categories not seen
during training.