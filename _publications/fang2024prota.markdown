---
layout: publication
title: 'Prota: Probabilistic Token Aggregation For Text-video Retrieval'
authors: Han Fang, Xianghao Zang, Chao Ban, Zerun Feng, Lanxiang Zhou, Zhongjiang
  He, Yongxiang Li, Hao Sun
conference: 2024 IEEE International Conference on Multimedia and Expo (ICME)
year: 2024
bibkey: fang2024prota
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.12216'}]
tags: ["Distance Metric Learning", "Video Retrieval"]
short_authors: Fang et al.
---
Text-video retrieval aims to find the most relevant cross-modal samples for a
given query. Recent methods focus on modeling the whole spatial-temporal
relations. However, since video clips contain more diverse content than
captions, the model aligning these asymmetric video-text pairs has a high risk
of retrieving many false positive results. In this paper, we propose
Probabilistic Token Aggregation (ProTA) to handle cross-modal interaction with
content asymmetry. Specifically, we propose dual partial-related aggregation to
disentangle and re-aggregate token representations in both low-dimension and
high-dimension spaces. We propose token-based probabilistic alignment to
generate token-level probabilistic representation and maintain the feature
representation diversity. In addition, an adaptive contrastive loss is proposed
to learn compact cross-modal distribution space. Based on extensive
experiments, ProTA achieves significant improvements on MSR-VTT (50.9%), LSMDC
(25.8%), and DiDeMo (47.2%).