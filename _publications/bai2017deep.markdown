---
layout: publication
title: 'Deep-person: Learning Discriminative Deep Features For Person Re-identification'
authors: Xiang Bai, Mingkun Yang, Tengteng Huang, Zhiyong Dou, Rui Yu, Yongchao Xu
conference: Pattern Recognition
year: 2019
bibkey: bai2017deep
citations: 220
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.10658'}]
tags: ["Datasets", "Evaluation", "Re-Ranking"]
short_authors: Bai et al.
---
Recently, many methods of person re-identification (Re-ID) rely on part-based
feature representation to learn a discriminative pedestrian descriptor.
However, the spatial context between these parts is ignored for the independent
extractor to each separate part. In this paper, we propose to apply Long
Short-Term Memory (LSTM) in an end-to-end way to model the pedestrian, seen as
a sequence of body parts from head to foot. Integrating the contextual
information strengthens the discriminative ability of local representation. We
also leverage the complementary information between local and global feature.
Furthermore, we integrate both identification task and ranking task in one
network, where a discriminative embedding and a similarity measurement are
learned concurrently. This results in a novel three-branch framework named
Deep-Person, which learns highly discriminative features for person Re-ID.
Experimental results demonstrate that Deep-Person outperforms the
state-of-the-art methods by a large margin on three challenging datasets
including Market-1501, CUHK03, and DukeMTMC-reID. Specifically, combining with
a re-ranking approach, we achieve a 90.84% mAP on Market-1501 under single
query setting.