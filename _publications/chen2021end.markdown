---
layout: publication
title: End-to-end User Behavior Retrieval In Click-through Rateprediction Model
authors: Qiwei Chen, Changhua Pei, Shanshan Lv, Chao Li, Junfeng Ge, Wenwu Ou
conference: Arxiv
year: 2021
bibkey: chen2021end
citations: 16
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.04468'}]
tags: [Evaluation, Scalability, Hashing Methods, Locality Sensitive Hashing, Recommender
    Systems]
short_authors: Chen et al.
---
Click-Through Rate (CTR) prediction is one of the core tasks in recommender
systems (RS). It predicts a personalized click probability for each user-item
pair. Recently, researchers have found that the performance of CTR model can be
improved greatly by taking user behavior sequence into consideration,
especially long-term user behavior sequence. The report on an e-commerce
website shows that 23% of users have more than 1000 clicks during the past 5
months. Though there are numerous works focus on modeling sequential user
behaviors, few works can handle long-term user behavior sequence due to the
strict inference time constraint in real world system. Two-stage methods are
proposed to push the limit for better performance. At the first stage, an
auxiliary task is designed to retrieve the top-\(k\) similar items from long-term
user behavior sequence. At the second stage, the classical attention mechanism
is conducted between the candidate item and \(k\) items selected in the first
stage. However, information gap happens between retrieval stage and the main
CTR task. This goal divergence can greatly diminishing the performance gain of
long-term user sequence. In this paper, inspired by Reformer, we propose a
locality-sensitive hashing (LSH) method called ETA (End-to-end Target
Attention) which can greatly reduce the training and inference cost and make
the end-to-end training with long-term user behavior sequence possible. Both
offline and online experiments confirm the effectiveness of our model. We
deploy ETA into a large-scale real world E-commerce system and achieve extra
3.1% improvements on GMV (Gross Merchandise Value) compared to a two-stage
long user sequence CTR model.