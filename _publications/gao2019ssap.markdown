---
layout: publication
title: 'SSAP: Single-shot Instance Segmentation With Affinity Pyramid'
authors: Naiyu Gao, Yanhu Shan, Yupei Wang, Xin Zhao, Yinan Yu, Ming Yang, Kaiqi Huang
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: gao2019ssap
citations: 213
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.01616'}]
tags: ["ICCV"]
short_authors: Gao et al.
---
Recently, proposal-free instance segmentation has received increasing
attention due to its concise and efficient pipeline. Generally, proposal-free
methods generate instance-agnostic semantic segmentation labels and
instance-aware features to group pixels into different object instances.
However, previous methods mostly employ separate modules for these two
sub-tasks and require multiple passes for inference. We argue that treating
these two sub-tasks separately is suboptimal. In fact, employing multiple
separate modules significantly reduces the potential for application. The
mutual benefits between the two complementary sub-tasks are also unexplored. To
this end, this work proposes a single-shot proposal-free instance segmentation
method that requires only one single pass for prediction. Our method is based
on a pixel-pair affinity pyramid, which computes the probability that two
pixels belong to the same instance in a hierarchical manner. The affinity
pyramid can also be jointly learned with the semantic class labeling and
achieve mutual benefits. Moreover, incorporating with the learned affinity
pyramid, a novel cascaded graph partition module is presented to sequentially
generate instances from coarse to fine. Unlike previous time-consuming graph
partition methods, this module achieves \(5\times\) speedup and 9% relative
improvement on Average-Precision (AP). Our approach achieves state-of-the-art
results on the challenging Cityscapes dataset.