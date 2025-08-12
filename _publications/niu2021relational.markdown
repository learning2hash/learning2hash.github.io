---
layout: publication
title: Relational Learning With Gated And Attentive Neighbor Aggregator For Few-shot
  Knowledge Graph Completion
authors: Guanglin Niu, Yang Li, Chengguang Tang, Ruiying Geng, Jian Dai, Qiao Liu,
  Hao Wang, Jian Sun, Fei Huang, Luo Si
conference: Proceedings of the 44th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2021
bibkey: niu2021relational
citations: 58
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.13095'}]
tags: ["Few Shot & Zero Shot", "SIGIR"]
short_authors: Niu et al.
---
Aiming at expanding few-shot relations' coverage in knowledge graphs (KGs),
few-shot knowledge graph completion (FKGC) has recently gained more research
interests. Some existing models employ a few-shot relation's multi-hop neighbor
information to enhance its semantic representation. However, noise neighbor
information might be amplified when the neighborhood is excessively sparse and
no neighbor is available to represent the few-shot relation. Moreover, modeling
and inferring complex relations of one-to-many (1-N), many-to-one (N-1), and
many-to-many (N-N) by previous knowledge graph completion approaches requires
high model complexity and a large amount of training instances. Thus, inferring
complex relations in the few-shot scenario is difficult for FKGC models due to
limited training instances. In this paper, we propose a few-shot relational
learning with global-local framework to address the above issues. At the global
stage, a novel gated and attentive neighbor aggregator is built for accurately
integrating the semantics of a few-shot relation's neighborhood, which helps
filtering the noise neighbors even if a KG contains extremely sparse
neighborhoods. For the local stage, a meta-learning based TransH (MTransH)
method is designed to model complex relations and train our model in a few-shot
learning fashion. Extensive experiments show that our model outperforms the
state-of-the-art FKGC approaches on the frequently-used benchmark datasets
NELL-One and Wiki-One. Compared with the strong baseline model MetaR, our model
achieves 5-shot FKGC performance improvements of 8.0% on NELL-One and 2.8% on
Wiki-One by the metric Hits@10.