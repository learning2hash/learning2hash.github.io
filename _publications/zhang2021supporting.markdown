---
layout: publication
title: Supporting Clustering With Contrastive Learning
authors: Dejiao Zhang, Feng Nan, Xiaokai Wei, Shangwen Li, Henghui Zhu, Kathleen McKeown,
  Ramesh Nallapati, Andrew Arnold, Bing Xiang
conference: 'Proceedings of the 2021 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies'
year: 2021
bibkey: zhang2021supporting
citations: 142
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.12953'}]
tags: ["Self-Supervised", "Unsupervised"]
short_authors: Zhang et al.
---
Unsupervised clustering aims at discovering the semantic categories of data
according to some distance measured in the representation space. However,
different categories often overlap with each other in the representation space
at the beginning of the learning process, which poses a significant challenge
for distance-based clustering in achieving good separation between different
categories. To this end, we propose Supporting Clustering with Contrastive
Learning (SCCL) -- a novel framework to leverage contrastive learning to
promote better separation. We assess the performance of SCCL on short text
clustering and show that SCCL significantly advances the state-of-the-art
results on most benchmark datasets with 3%-11% improvement on Accuracy and
4%-15% improvement on Normalized Mutual Information. Furthermore, our
quantitative analysis demonstrates the effectiveness of SCCL in leveraging the
strengths of both bottom-up instance discrimination and top-down clustering to
achieve better intra-cluster and inter-cluster distances when evaluated with
the ground truth cluster labels.