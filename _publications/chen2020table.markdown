---
layout: publication
title: Table Search Using A Deep Contextualized Language Model
authors: Zhiyu Chen, Mohamed Trabelsi, Jeff Heflin, Yinan Xu, Brian D. Davison
conference: 'SIGIR ''20: The 43rd International ACM SIGIR conference on research and
  development in Information Retrieval'
year: 2020
bibkey: chen2020table
citations: 44
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2005.09207'}]
tags: ["Datasets", "Evaluation", "SIGIR"]
short_authors: Chen et al.
---
Pretrained contextualized language models such as BERT have achieved
impressive results on various natural language processing benchmarks.
Benefiting from multiple pretraining tasks and large scale training corpora,
pretrained models can capture complex syntactic word relations. In this paper,
we use the deep contextualized language model BERT for the task of ad hoc table
retrieval. We investigate how to encode table content considering the table
structure and input length limit of BERT. We also propose an approach that
incorporates features from prior literature on table retrieval and jointly
trains them with BERT. In experiments on public datasets, we show that our best
approach can outperform the previous state-of-the-art method and BERT baselines
with a large margin under different evaluation metrics.