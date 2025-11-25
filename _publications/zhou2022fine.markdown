---
layout: publication
title: Fine-grained Distillation For Long Document Retrieval
authors: Yucheng Zhou, Tao Shen, Xiubo Geng, Chongyang Tao, Guodong Long, Can Xu,
  Daxin Jiang
conference: Arxiv
year: 2022
bibkey: zhou2022fine
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.10423'}]
tags: ["Evaluation", "Scalability", "Text Retrieval"]
short_authors: Zhou et al.
---
Long document retrieval aims to fetch query-relevant documents from a
large-scale collection, where knowledge distillation has become de facto to
improve a retriever by mimicking a heterogeneous yet powerful cross-encoder.
However, in contrast to passages or sentences, retrieval on long documents
suffers from the scope hypothesis that a long document may cover multiple
topics. This maximizes their structure heterogeneity and poses a
granular-mismatch issue, leading to an inferior distillation efficacy. In this
work, we propose a new learning framework, fine-grained distillation (FGD), for
long-document retrievers. While preserving the conventional dense retrieval
paradigm, it first produces global-consistent representations crossing
different fine granularity and then applies multi-granular aligned distillation
merely during training. In experiments, we evaluate our framework on two
long-document retrieval benchmarks, which show state-of-the-art performance.