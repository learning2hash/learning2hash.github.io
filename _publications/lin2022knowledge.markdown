---
layout: publication
title: Knowledge Distillation Via The Target-aware Transformer
authors: Sihao Lin, Hongwei Xie, Bing Wang, Kaicheng Yu, Xiaojun Chang, Xiaodan Liang,
  Gang Wang
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: lin2022knowledge
citations: 82
additional_links: [{name: Code, url: 'https://github.com/sihaoevery/TaT'}, {name: Paper,
    url: 'https://arxiv.org/abs/2205.10793'}]
tags: ["CVPR"]
short_authors: Lin et al.
---
Knowledge distillation becomes a de facto standard to improve the performance
of small neural networks. Most of the previous works propose to regress the
representational features from the teacher to the student in a one-to-one
spatial matching fashion. However, people tend to overlook the fact that, due
to the architecture differences, the semantic information on the same spatial
location usually vary. This greatly undermines the underlying assumption of the
one-to-one distillation approach. To this end, we propose a novel one-to-all
spatial matching knowledge distillation approach. Specifically, we allow each
pixel of the teacher feature to be distilled to all spatial locations of the
student features given its similarity, which is generated from a target-aware
transformer. Our approach surpasses the state-of-the-art methods by a
significant margin on various computer vision benchmarks, such as ImageNet,
Pascal VOC and COCOStuff10k. Code is available at
https://github.com/sihaoevery/TaT.