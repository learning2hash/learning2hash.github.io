---
layout: publication
title: Anno-incomplete Multi-dataset Detection
authors: Yiran Xu, Haoxiang Zhong, Kai Wu, Jialin Li, Yong Liu, Chengjie Wang, Shu-Tao
  Xia, Hongen Liao
conference: Arxiv
year: 2024
bibkey: xu2024anno
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.16247'}]
tags: ["Datasets", "Evaluation"]
short_authors: Xu et al.
---
Object detectors have shown outstanding performance on various public
datasets. However, annotating a new dataset for a new task is usually
unavoidable in real, since 1) a single existing dataset usually does not
contain all object categories needed; 2) using multiple datasets usually
suffers from annotation incompletion and heterogeneous features. We propose a
novel problem as "Annotation-incomplete Multi-dataset Detection", and develop
an end-to-end multi-task learning architecture which can accurately detect all
the object categories with multiple partially annotated datasets. Specifically,
we propose an attention feature extractor which helps to mine the relations
among different datasets. Besides, a knowledge amalgamation training strategy
is incorporated to accommodate heterogeneous features from different sources.
Extensive experiments on different object detection datasets demonstrate the
effectiveness of our methods and an improvement of 2.17%, 2.10% in mAP can be
achieved on COCO and VOC respectively.