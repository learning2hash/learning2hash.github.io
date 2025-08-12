---
layout: publication
title: Decomposed Meta-learning For Few-shot Named Entity Recognition
authors: Tingting Ma, Huiqiang Jiang, Qianhui Wu, Tiejun Zhao, Chin-Yew Lin
conference: 'Findings of the Association for Computational Linguistics: ACL 2022'
year: 2022
bibkey: ma2022decomposed
citations: 59
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.05751'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Ma et al.
---
Few-shot named entity recognition (NER) systems aim at recognizing
novel-class named entities based on only a few labeled examples. In this paper,
we present a decomposed meta-learning approach which addresses the problem of
few-shot NER by sequentially tackling few-shot span detection and few-shot
entity typing using meta-learning. In particular, we take the few-shot span
detection as a sequence labeling problem and train the span detector by
introducing the model-agnostic meta-learning (MAML) algorithm to find a good
model parameter initialization that could fast adapt to new entity classes. For
few-shot entity typing, we propose MAML-ProtoNet, i.e., MAML-enhanced
prototypical networks to find a good embedding space that can better
distinguish text span representations from different entity classes. Extensive
experiments on various benchmarks show that our approach achieves superior
performance over prior methods.