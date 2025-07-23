---
layout: publication
title: Deep Relational Metric Learning
authors: Zheng Wenzhao, Zhang Borui, Lu Jiwen, Zhou Jie
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: zheng2021deep
citations: 36
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.10026'}]
tags: ["Distance Metric Learning", "ICCV"]
short_authors: Zheng et al.
---
This paper presents a deep relational metric learning (DRML) framework for
image clustering and retrieval. Most existing deep metric learning methods
learn an embedding space with a general objective of increasing interclass
distances and decreasing intraclass distances. However, the conventional losses
of metric learning usually suppress intraclass variations which might be
helpful to identify samples of unseen classes. To address this problem, we
propose to adaptively learn an ensemble of features that characterizes an image
from different aspects to model both interclass and intraclass distributions.
We further employ a relational module to capture the correlations among each
feature in the ensemble and construct a graph to represent an image. We then
perform relational inference on the graph to integrate the ensemble and obtain
a relation-aware embedding to measure the similarities. Extensive experiments
on the widely-used CUB-200-2011, Cars196, and Stanford Online Products datasets
demonstrate that our framework improves existing deep metric learning methods
and achieves very competitive results.