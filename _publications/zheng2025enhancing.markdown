---
layout: publication
title: Enhancing Embedding Representation Stability In Recommendation Systems With
  Semantic ID
authors: Zheng Carolina, Huang Minhui, Pedchenko Dmitrii, Rangadurai Kaushik, Wang
  Siyu, Nahum Gaby, Lei Jie, Yang Yang, Liu Tao, Luo Zutian, Wei Xiaohan, Ramasamy
  Dinesh, Yang Jiyan, Han Yiping, Yang Lin, Xu Hangjun, Jin Rong, Yang Shuang
conference: Arxiv
year: 2025
bibkey: zheng2025enhancing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.02137'}]
tags: ["Evaluation", "Recommender-Systems", "Hashing-Methods"]
short_authors: Zheng et al.
---
The exponential growth of online content has posed significant challenges to
ID-based models in industrial recommendation systems, ranging from extremely
high cardinality and dynamically growing ID space, to highly skewed engagement
distributions, to prediction instability as a result of natural id life cycles
(e.g, the birth of new IDs and retirement of old IDs). To address these issues,
many systems rely on random hashing to handle the id space and control the
corresponding model parameters (i.e embedding table). However, this approach
introduces data pollution from multiple ids sharing the same embedding, leading
to degraded model performance and embedding representation instability.
  This paper examines these challenges and introduces Semantic ID prefix ngram,
a novel token parameterization technique that significantly improves the
performance of the original Semantic ID. Semantic ID prefix ngram creates
semantically meaningful collisions by hierarchically clustering items based on
their content embeddings, as opposed to random assignments. Through extensive
experimentation, we demonstrate that Semantic ID prefix ngram not only
addresses embedding instability but also significantly improves tail id
modeling, reduces overfitting, and mitigates representation shifts. We further
highlight the advantages of Semantic ID prefix ngram in attention-based models
that contextualize user histories, showing substantial performance
improvements. We also report our experience of integrating Semantic ID into
Meta production Ads Ranking system, leading to notable performance gains and
enhanced prediction stability in live deployments.