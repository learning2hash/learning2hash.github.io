---
layout: publication
title: 'Documentnet: Bridging The Data Gap In Document Pre-training'
authors: Lijun Yu, Jin Miao, Xiaoyu Sun, Jiayi Chen, Alexander G. Hauptmann, Hanjun
  Dai, Wei Wei
conference: 'Proceedings of the 2023 Conference on Empirical Methods in Natural Language
  Processing: Industry Track'
year: 2023
bibkey: yu2023documentnet
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.08937'}]
tags: ["Datasets", "EMNLP"]
short_authors: Yu et al.
---
Document understanding tasks, in particular, Visually-rich Document Entity
Retrieval (VDER), have gained significant attention in recent years thanks to
their broad applications in enterprise AI. However, publicly available data
have been scarce for these tasks due to strict privacy constraints and high
annotation costs. To make things worse, the non-overlapping entity spaces from
different datasets hinder the knowledge transfer between document types. In
this paper, we propose a method to collect massive-scale and weakly labeled
data from the web to benefit the training of VDER models. The collected
dataset, named DocumentNet, does not depend on specific document types or
entity sets, making it universally applicable to all VDER tasks. The current
DocumentNet consists of 30M documents spanning nearly 400 document types
organized in a four-level ontology. Experiments on a set of broadly adopted
VDER tasks show significant improvements when DocumentNet is incorporated into
the pre-training for both classic and few-shot learning settings. With the
recent emergence of large language models (LLMs), DocumentNet provides a large
data source to extend their multi-modal capabilities for VDER.