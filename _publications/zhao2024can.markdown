---
layout: publication
title: Can One Embedding Fit All? A Multi-interest Learning Paradigm Towards Improving
  User Interest Diversity Fairness
authors: Yuying Zhao, Minghua Xu, Huiyuan Chen, Yuzhong Chen, Yiwei Cai, Rashidul
  Islam, Yu Wang, Tyler Derr
conference: Proceedings of the ACM Web Conference 2024
year: 2024
bibkey: zhao2024can
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.13495'}]
tags: []
short_authors: Zhao et al.
---
Recommender systems (RSs) have gained widespread applications across various
domains owing to the superior ability to capture users' interests. However, the
complexity and nuanced nature of users' interests, which span a wide range of
diversity, pose a significant challenge in delivering fair recommendations. In
practice, user preferences vary significantly; some users show a clear
preference toward certain item categories, while others have a broad interest
in diverse ones. Even though it is expected that all users should receive
high-quality recommendations, the effectiveness of RSs in catering to this
disparate interest diversity remains under-explored.
  In this work, we investigate whether users with varied levels of interest
diversity are treated fairly. Our empirical experiments reveal an inherent
disparity: users with broader interests often receive lower-quality
recommendations. To mitigate this, we propose a multi-interest framework that
uses multiple (virtual) interest embeddings rather than single ones to
represent users. Specifically, the framework consists of stacked multi-interest
representation layers, which include an interest embedding generator that
derives virtual interests from shared parameters, and a center embedding
aggregator that facilitates multi-hop aggregation. Experiments demonstrate the
effectiveness of the framework in achieving better trade-off between fairness
and utility across various datasets and backbones.