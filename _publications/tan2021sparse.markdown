---
layout: publication
title: Sparse-interest Network For Sequential Recommendation
authors: Qiaoyu Tan, Jianwei Zhang, Jiangchao Yao, Ninghao Liu, Jingren Zhou, Hongxia
  Yang, Xia Hu
conference: Proceedings of the 14th ACM International Conference on Web Search and
  Data Mining
year: 2021
bibkey: tan2021sparse
citations: 103
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.09267'}]
tags: [Recommender Systems, Evaluation, Datasets, Scalability]
short_authors: Tan et al.
---
Recent methods in sequential recommendation focus on learning an overall
embedding vector from a user's behavior sequence for the next-item
recommendation. However, from empirical analysis, we discovered that a user's
behavior sequence often contains multiple conceptually distinct items, while a
unified embedding vector is primarily affected by one's most recent frequent
actions. Thus, it may fail to infer the next preferred item if conceptually
similar items are not dominant in recent interactions. To this end, an
alternative solution is to represent each user with multiple embedding vectors
encoding different aspects of the user's intentions. Nevertheless, recent work
on multi-interest embedding usually considers a small number of concepts
discovered via clustering, which may not be comparable to the large pool of
item categories in real systems. It is a non-trivial task to effectively model
a large number of diverse conceptual prototypes, as items are often not
conceptually well clustered in fine granularity. Besides, an individual usually
interacts with only a sparse set of concepts. In light of this, we propose a
novel \textbf\{S\}parse \textbf\{I\}nterest \textbf\{NE\}twork (SINE) for sequential
recommendation. Our sparse-interest module can adaptively infer a sparse set of
concepts for each user from the large concept pool and output multiple
embeddings accordingly. Given multiple interest embeddings, we develop an
interest aggregation module to actively predict the user's current intention
and then use it to explicitly model multiple interests for next-item
prediction. Empirical results on several public benchmark datasets and one
large-scale industrial dataset demonstrate that SINE can achieve substantial
improvement over state-of-the-art methods.