---
layout: publication
title: A Task-aware Dual Similarity Network For Fine-grained Few-shot Learning
authors: Yan Qi, Han Sun, Ningzhong Liu, Huiyu Zhou
conference: Lecture Notes in Computer Science
year: 2022
bibkey: qi2022task
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.12348'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Qi et al.
---
The goal of fine-grained few-shot learning is to recognize sub-categories
under the same super-category by learning few labeled samples. Most of the
recent approaches adopt a single similarity measure, that is, global or local
measure alone. However, for fine-grained images with high intra-class variance
and low inter-class variance, exploring global invariant features and
discriminative local details is quite essential. In this paper, we propose a
Task-aware Dual Similarity Network(TDSNet), which applies global features and
local patches to achieve better performance. Specifically, a local feature
enhancement module is adopted to activate the features with strong
discriminability. Besides, task-aware attention exploits the important patches
among the entire task. Finally, both the class prototypes obtained by global
features and discriminative local patches are employed for prediction.
Extensive experiments on three fine-grained datasets demonstrate that the
proposed TDSNet achieves competitive performance by comparing with other
state-of-the-art algorithms.