---
layout: publication
title: Fine-grained Prototypes Distillation For Few-shot Object Detection
authors: Zichen Wang, Bo Yang, Haonan Yue, Zhenghao Ma
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: wang2024fine
citations: 12
additional_links: [{name: Code, url: 'https://github.com/wangchen1801/FPD'}, {name: Paper,
    url: 'https://arxiv.org/abs/2401.07629'}]
tags: ["AAAI", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Wang et al.
---
Few-shot object detection (FSOD) aims at extending a generic detector for
novel object detection with only a few training examples. It attracts great
concerns recently due to the practical meanings. Meta-learning has been
demonstrated to be an effective paradigm for this task. In general, methods
based on meta-learning employ an additional support branch to encode novel
examples (a.k.a. support images) into class prototypes, which are then fused
with query branch to facilitate the model prediction. However, the class-level
prototypes are difficult to precisely generate, and they also lack detailed
information, leading to instability in performance.New methods are required to
capture the distinctive local context for more robust novel object detection.
To this end, we propose to distill the most representative support features
into fine-grained prototypes. These prototypes are then assigned into query
feature maps based on the matching results, modeling the detailed feature
relations between two branches. This process is realized by our Fine-Grained
Feature Aggregation (FFA) module. Moreover, in terms of high-level feature
fusion, we propose Balanced Class-Agnostic Sampling (B-CAS) strategy and
Non-Linear Fusion (NLF) module from differenct perspectives. They are
complementary to each other and depict the high-level feature relations more
effectively. Extensive experiments on PASCAL VOC and MS COCO benchmarks show
that our method sets a new state-of-the-art performance in most settings. Our
code is available at https://github.com/wangchen1801/FPD.