---
layout: publication
title: 'Semantics-oriented Multitask Learning For Deepfake Detection: A Joint Embedding
  Approach'
authors: Mian Zou, Baosheng Yu, Yibing Zhan, Siwei Lyu, Kede Ma
conference: Arxiv
year: 2024
bibkey: zou2024semantics
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.16305'}]
tags: []
short_authors: Zou et al.
---
In recent years, the multimedia forensics and security community has seen remarkable progress in multitask learning for DeepFake (i.e., face forgery) detection. The prevailing approach has been to frame DeepFake detection as a binary classification problem augmented by manipulation-oriented auxiliary tasks. This scheme focuses on learning features specific to face manipulations with limited generalizability. In this paper, we delve deeper into semantics-oriented multitask learning for DeepFake detection, capturing the relationships among face semantics via joint embedding. We first propose an automated dataset expansion technique that broadens current face forgery datasets to support semantics-oriented DeepFake detection tasks at both the global face attribute and local face region levels. Furthermore, we resort to the joint embedding of face images and labels (depicted by text descriptions) for prediction. This approach eliminates the need for manually setting task-agnostic and task-specific parameters, which is typically required when predicting multiple labels directly from images. In addition, we employ bi-level optimization to dynamically balance the fidelity loss weightings of various tasks, making the training process fully automated. Extensive experiments on six DeepFake datasets show that our method improves the generalizability of DeepFake detection and renders some degree of model interpretation by providing human-understandable explanations.