---
layout: publication
title: 'Bivrec: Bidirectional View-based Multimodal Sequential Recommendation'
authors: Jiaxi Hu, Jingtong Gao, Xiangyu Zhao, Yuehong Hu, Yuxuan Liang, Yiqi Wang,
  Ming He, Zitao Liu, Hongzhi Yin
conference: Arxiv
year: 2024
bibkey: hu2024bivrec
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.17334'}]
tags: ["Recommender Systems"]
short_authors: Hu et al.
---
The integration of multimodal information into sequential recommender systems
has attracted significant attention in recent research. In the initial stages
of multimodal sequential recommendation models, the mainstream paradigm was
ID-dominant recommendations, wherein multimodal information was fused as side
information. However, due to their limitations in terms of transferability and
information intrusion, another paradigm emerged, wherein multimodal features
were employed directly for recommendation, enabling recommendation across
datasets. Nonetheless, it overlooked user ID information, resulting in low
information utilization and high training costs. To this end, we propose an
innovative framework, BivRec, that jointly trains the recommendation tasks in
both ID and multimodal views, leveraging their synergistic relationship to
enhance recommendation performance bidirectionally. To tackle the information
heterogeneity issue, we first construct structured user interest
representations and then learn the synergistic relationship between them.
Specifically, BivRec comprises three modules: Multi-scale Interest Embedding,
comprehensively modeling user interests by expanding user interaction sequences
with multi-scale patching; Intra-View Interest Decomposition, constructing
highly structured interest representations using carefully designed Gaussian
attention and Cluster attention; and Cross-View Interest Learning, learning the
synergistic relationship between the two recommendation views through
coarse-grained overall semantic similarity and fine-grained interest allocation
similarity BiVRec achieves state-of-the-art performance on five datasets and
showcases various practical advantages.