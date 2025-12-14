---
layout: publication
title: 'Few-shot Metric Learning: Online Adaptation Of Embedding For Retrieval'
authors: Deunsol Jung, Dahyun Kang, Suha Kwak, Minsu Cho
conference: Arxiv
year: 2022
bibkey: jung2022few
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.07116'}]
tags: [Distance Metric Learning, Image Retrieval, Few-shot & Zero-shot, Datasets]
short_authors: Jung et al.
---
Metric learning aims to build a distance metric typically by learning an
effective embedding function that maps similar objects into nearby points in
its embedding space. Despite recent advances in deep metric learning, it
remains challenging for the learned metric to generalize to unseen classes with
a substantial domain gap. To tackle the issue, we explore a new problem of
few-shot metric learning that aims to adapt the embedding function to the
target domain with only a few annotated data. We introduce three few-shot
metric learning baselines and propose the Channel-Rectifier Meta-Learning
(CRML), which effectively adapts the metric space online by adjusting channels
of intermediate layers. Experimental analyses on miniImageNet, CUB-200-2011,
MPII, as well as a new dataset, miniDeepFashion, demonstrate that our method
consistently improves the learned metric by adapting it to target classes and
achieves a greater gain in image retrieval when the domain gap from the source
classes is larger.