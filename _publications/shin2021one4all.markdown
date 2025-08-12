---
layout: publication
title: One4all User Representation For Recommender Systems In E-commerce
authors: Kyuyong Shin, Hanock Kwak, Kyung-Min Kim, Minkyu Kim, Young-Jin Park, Jisu
  Jeong, Seungjae Jung
conference: Arxiv
year: 2021
bibkey: shin2021one4all
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.00573'}]
tags: ["Recommender Systems"]
short_authors: Shin et al.
---
General-purpose representation learning through large-scale pre-training has
shown promising results in the various machine learning fields. For an
e-commerce domain, the objective of general-purpose, i.e., one for all,
representations would be efficient applications for extensive downstream tasks
such as user profiling, targeting, and recommendation tasks. In this paper, we
systematically compare the generalizability of two learning strategies, i.e.,
transfer learning through the proposed model, ShopperBERT, vs. learning from
scratch. ShopperBERT learns nine pretext tasks with 79.2M parameters from 0.8B
user behaviors collected over two years to produce user embeddings. As a
result, the MLPs that employ our embedding method outperform more complex
models trained from scratch for five out of six tasks. Specifically, the
pre-trained embeddings have superiority over the task-specific supervised
features and the strong baselines, which learn the auxiliary dataset for the
cold-start problem. We also show the computational efficiency and embedding
visualization of the pre-trained features.