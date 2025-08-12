---
layout: publication
title: Leveraging Member-group Relations Via Multi-view Graph Filtering For Effective
  Group Recommendation
authors: Chae-Hyun Kim, Yoon-Ryung Choi, Jin-Duk Park, Won-Yong Shin
conference: Companion Proceedings of the ACM on Web Conference 2025
year: 2025
bibkey: kim2025leveraging
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.09050'}]
tags: ["Recommender Systems"]
short_authors: Kim et al.
---
Group recommendation aims at providing optimized recommendations tailored to
diverse groups, enabling groups to enjoy appropriate items. On the other hand,
most existing group recommendation methods are built upon deep neural network
(DNN) architectures designed to capture the intricate relationships between
member-level and group-level interactions. While these DNN-based approaches
have proven their effectiveness, they require complex and expensive training
procedures to incorporate group-level interactions in addition to member-level
interactions. To overcome such limitations, we introduce Group-GF, a new
approach for extremely fast recommendations of items to each group via
multi-view graph filtering (GF) that offers a holistic view of complex
member-group dynamics, without the need for costly model training.
Specifically, in Group-GF, we first construct three item similarity graphs
manifesting different viewpoints for GF. Then, we discover a distinct
polynomial graph filter for each similarity graph and judiciously aggregate the
three graph filters. Extensive experiments demonstrate the effectiveness of
Group-GF in terms of significantly reducing runtime and achieving
state-of-the-art recommendation accuracy.