---
layout: publication
title: A Simple Task-aware Contrastive Local Descriptor Selection Strategy For Few-shot
  Learning Between Inter Class And Intra Class
authors: Qian Qiao, Yu Xie, Shaoyao Huang, Fanzhang Li
conference: Lecture Notes in Computer Science
year: 2024
bibkey: qiao2024simple
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.05953'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Qiao et al.
---
Few-shot image classification aims to classify novel classes with few labeled
samples. Recent research indicates that deep local descriptors have better
representational capabilities. These studies recognize the impact of background
noise on classification performance. They typically filter query descriptors
using all local descriptors in the support classes or engage in bidirectional
selection between local descriptors in support and query sets. However, they
ignore the fact that background features may be useful for the classification
performance of specific tasks. This paper proposes a novel task-aware
contrastive local descriptor selection network (TCDSNet). First, we calculate
the contrastive discriminative score for each local descriptor in the support
class, and select discriminative local descriptors to form a support descriptor
subset. Finally, we leverage support descriptor subsets to adaptively select
discriminative query descriptors for specific tasks. Extensive experiments
demonstrate that our method outperforms state-of-the-art methods on both
general and fine-grained datasets.