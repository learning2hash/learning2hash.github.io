---
layout: publication
title: Efficient Deep Feature Calibration For Cross-modal Joint Embedding Learning
authors: Xie Zhongwei, Liu Ling, Li Lin, Zhong Luo
conference: Proceedings of the 2021 International Conference on Multimodal Interaction
year: 2021
bibkey: xie2021efficient
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.00705'}]
tags: ["Tools-&-Libraries", "Distance-Metric-Learning", "Datasets"]
short_authors: Xie et al.
---
This paper introduces a two-phase deep feature calibration framework for
efficient learning of semantics enhanced text-image cross-modal joint
embedding, which clearly separates the deep feature calibration in data
preprocessing from training the joint embedding model. We use the Recipe1M
dataset for the technical description and empirical validation. In
preprocessing, we perform deep feature calibration by combining deep feature
engineering with semantic context features derived from raw text-image input
data. We leverage LSTM to identify key terms, NLP methods to produce ranking
scores for key terms before generating the key term feature. We leverage
wideResNet50 to extract and encode the image category semantics to help
semantic alignment of the learned recipe and image embeddings in the joint
latent space. In joint embedding learning, we perform deep feature calibration
by optimizing the batch-hard triplet loss function with soft-margin and double
negative sampling, also utilizing the category-based alignment loss and
discriminator-based alignment loss. Extensive experiments demonstrate that our
SEJE approach with the deep feature calibration significantly outperforms the
state-of-the-art approaches.