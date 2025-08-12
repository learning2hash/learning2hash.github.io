---
layout: publication
title: Boosting Multi-label Image Classification With Complementary Parallel Self-distillation
authors: Jiazhi Xu, Sheng Huang, Fengtao Zhou, Luwen Huangfu, Daniel Zeng, Bo Liu
conference: Proceedings of the Thirty-First International Joint Conference on Artificial
  Intelligence
year: 2022
bibkey: xu2022boosting
citations: 9
additional_links: [{name: Code, url: 'https://github.com/Robbie-Xu/CPSD'}, {name: Paper,
    url: 'https://arxiv.org/abs/2205.10986'}]
tags: ["IJCAI"]
short_authors: Xu et al.
---
Multi-Label Image Classification (MLIC) approaches usually exploit label
correlations to achieve good performance. However, emphasizing correlation like
co-occurrence may overlook discriminative features of the target itself and
lead to model overfitting, thus undermining the performance. In this study, we
propose a generic framework named Parallel Self-Distillation (PSD) for boosting
MLIC models. PSD decomposes the original MLIC task into several simpler MLIC
sub-tasks via two elaborated complementary task decomposition strategies named
Co-occurrence Graph Partition (CGP) and Dis-occurrence Graph Partition (DGP).
Then, the MLIC models of fewer categories are trained with these sub-tasks in
parallel for respectively learning the joint patterns and the category-specific
patterns of labels. Finally, knowledge distillation is leveraged to learn a
compact global ensemble of full categories with these learned patterns for
reconciling the label correlation exploitation and model overfitting. Extensive
results on MS-COCO and NUS-WIDE datasets demonstrate that our framework can be
easily plugged into many MLIC approaches and improve performances of recent
state-of-the-art approaches. The explainable visual study also further
validates that our method is able to learn both the category-specific and
co-occurring features. The source code is released at
https://github.com/Robbie-Xu/CPSD.