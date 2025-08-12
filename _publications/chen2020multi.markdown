---
layout: publication
title: Multi-scale Adaptive Task Attention Network For Few-shot Learning
authors: Haoxing Chen, Huaxiong Li, Yaohui Li, Chunlin Chen
conference: 2022 26th International Conference on Pattern Recognition (ICPR)
year: 2022
bibkey: chen2020multi
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.14479'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Chen et al.
---
The goal of few-shot learning is to classify unseen categories with few
labeled samples. Recently, the low-level information metric-learning based
methods have achieved satisfying performance, since local representations (LRs)
are more consistent between seen and unseen classes. However, most of these
methods deal with each category in the support set independently, which is not
sufficient to measure the relation between features, especially in a certain
task. Moreover, the low-level information-based metric learning method suffers
when dominant objects of different scales exist in a complex background. To
address these issues, this paper proposes a novel Multi-scale Adaptive Task
Attention Network (MATANet) for few-shot learning. Specifically, we first use a
multi-scale feature generator to generate multiple features at different
scales. Then, an adaptive task attention module is proposed to select the most
important LRs among the entire task. Afterwards, a similarity-to-class module
and a fusion layer are utilized to calculate a joint multi-scale similarity
between the query image and the support set. Extensive experiments on popular
benchmarks clearly show the effectiveness of the proposed MATANet compared with
state-of-the-art methods.