---
layout: publication
title: A Multi-task Semantic Decomposition Framework With Task-specific Pre-training
  For Few-shot NER
authors: Guanting Dong, Zechen Wang, Jinxu Zhao, Gang Zhao, Daichi Guo, Dayuan Fu,
  Tingfeng Hui, Chen Zeng, Keqing He, Xuefeng Li, Liwen Wang, Xinyue Cui, Weiran Xu
conference: Proceedings of the 32nd ACM International Conference on Information and
  Knowledge Management
year: 2023
bibkey: dong2023multi
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.14533'}]
tags: ["CIKM", "Few Shot & Zero Shot", "Self-Supervised"]
short_authors: Dong et al.
---
The objective of few-shot named entity recognition is to identify named
entities with limited labeled instances. Previous works have primarily focused
on optimizing the traditional token-wise classification framework, while
neglecting the exploration of information based on NER data characteristics. To
address this issue, we propose a Multi-Task Semantic Decomposition Framework
via Joint Task-specific Pre-training (MSDP) for few-shot NER. Drawing
inspiration from demonstration-based and contrastive learning, we introduce two
novel pre-training tasks: Demonstration-based Masked Language Modeling (MLM)
and Class Contrastive Discrimination. These tasks effectively incorporate
entity boundary information and enhance entity representation in Pre-trained
Language Models (PLMs). In the downstream main task, we introduce a multi-task
joint optimization framework with the semantic decomposing method, which
facilitates the model to integrate two different semantic information for
entity classification. Experimental results of two few-shot NER benchmarks
demonstrate that MSDP consistently outperforms strong baselines by a large
margin. Extensive analyses validate the effectiveness and generalization of
MSDP.