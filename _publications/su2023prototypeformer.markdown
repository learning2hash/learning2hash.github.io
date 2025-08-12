---
layout: publication
title: 'Prototypeformer: Learning To Explore Prototype Relationships For Few-shot
  Image Classification'
authors: Meijuan Su, Feihong He, Fanzhang Li
conference: Neurocomputing
year: 2025
bibkey: su2023prototypeformer
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.03517'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Meijuan Su, Feihong He, Fanzhang Li
---
Few-shot image classification has received considerable attention for
overcoming the challenge of limited classification performance with limited
samples in novel classes. Most existing works employ sophisticated learning
strategies and feature learning modules to alleviate this challenge. In this
paper, we propose a novel method called PrototypeFormer, exploring the
relationships among category prototypes in the few-shot scenario. Specifically,
we utilize a transformer architecture to build a prototype extraction module,
aiming to extract class representations that are more discriminative for
few-shot classification. Besides, during the model training process, we propose
a contrastive learning-based optimization approach to optimize prototype
features in few-shot learning scenarios. Despite its simplicity, our method
performs remarkably well, with no bells and whistles. We have experimented with
our approach on several popular few-shot image classification benchmark
datasets, which shows that our method outperforms all current state-of-the-art
methods. In particular, our method achieves 97.07% and 90.88% on 5-way 5-shot
and 5-way 1-shot tasks of miniImageNet, which surpasses the state-of-the-art
results with accuracy of 0.57% and 6.84%, respectively. The code will be
released later.