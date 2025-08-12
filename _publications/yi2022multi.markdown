---
layout: publication
title: Multi-auxiliary Augmented Collaborative Variational Auto-encoder For Tag Recommendation
authors: Jing Yi, Xubin Ren, Zhenzhong Chen
conference: ACM Transactions on Information Systems
year: 2023
bibkey: yi2022multi
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.09422'}]
tags: ["Recommender Systems"]
short_authors: Jing Yi, Xubin Ren, Zhenzhong Chen
---
Recommending appropriate tags to items can facilitate content organization,
retrieval, consumption and other applications, where hybrid tag recommender
systems have been utilized to integrate collaborative information and content
information for better recommendations. In this paper, we propose a
multi-auxiliary augmented collaborative variational auto-encoder (MA-CVAE) for
tag recommendation, which couples item collaborative information and item
multi-auxiliary information, i.e., content and social graph, by defining a
generative process. Specifically, the model learns deep latent embeddings from
different item auxiliary information using variational auto-encoders (VAE),
which could form a generative distribution over each auxiliary information by
introducing a latent variable parameterized by deep neural network. Moreover,
to recommend tags for new items, item multi-auxiliary latent embeddings are
utilized as a surrogate through the item decoder for predicting recommendation
probabilities of each tag, where reconstruction losses are added in the
training phase to constrict the generation for feedback predictions via
different auxiliary embeddings. In addition, an inductive variational graph
auto-encoder is designed where new item nodes could be inferred in the test
phase, such that item social embeddings could be exploited for new items.
Extensive experiments on MovieLens and citeulike datasets demonstrate the
effectiveness of our method.