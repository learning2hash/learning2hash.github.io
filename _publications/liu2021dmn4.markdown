---
layout: publication
title: 'DMN4: Few-shot Learning Via Discriminative Mutual Nearest Neighbor Neural
  Network'
authors: Yang Liu, Tu Zheng, Jie Song, Deng Cai, Xiaofei He
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2022
bibkey: liu2021dmn4
citations: 24
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.08160'}]
tags: ["AAAI", "Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Few-shot learning (FSL) aims to classify images under low-data regimes, where
the conventional pooled global feature is likely to lose useful local
characteristics. Recent work has achieved promising performances by using deep
descriptors. They generally take all deep descriptors from neural networks into
consideration while ignoring that some of them are useless in classification
due to their limited receptive field, e.g., task-irrelevant descriptors could
be misleading and multiple aggregative descriptors from background clutter
could even overwhelm the object's presence. In this paper, we argue that a
Mutual Nearest Neighbor (MNN) relation should be established to explicitly
select the query descriptors that are most relevant to each task and discard
less relevant ones from aggregative clutters in FSL. Specifically, we propose
Discriminative Mutual Nearest Neighbor Neural Network (DMN4) for FSL. Extensive
experiments demonstrate that our method outperforms the existing
state-of-the-arts on both fine-grained and generalized datasets.