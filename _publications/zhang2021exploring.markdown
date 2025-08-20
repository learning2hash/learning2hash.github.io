---
layout: publication
title: Exploring Instance Relations For Unsupervised Feature Embedding
authors: Yifei Zhang, Yu Zhou, Weiping Wang
conference: Arxiv
year: 2021
bibkey: zhang2021exploring
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.03341'}]
tags: [Self-Supervised, Unsupervised, Evaluation]
short_authors: Yifei Zhang, Yu Zhou, Weiping Wang
---
Despite the great progress achieved in unsupervised feature embedding,
existing contrastive learning methods typically pursue view-invariant
representations through attracting positive sample pairs and repelling negative
sample pairs in the embedding space, while neglecting to systematically explore
instance relations. In this paper, we explore instance relations including
intra-instance multi-view relation and inter-instance interpolation relation
for unsupervised feature embedding. Specifically, we embed intra-instance
multi-view relation by aligning the distribution of the distance between an
instance's different augmented samples and negative samples. We explore
inter-instance interpolation relation by transferring the ratio of information
for image sample interpolation from pixel space to feature embedding space. The
proposed approach, referred to as EIR, is simple-yet-effective and can be
easily inserted into existing view-invariant contrastive learning based
methods. Experiments conducted on public benchmarks for image classification
and retrieval report state-of-the-art or comparable performance.