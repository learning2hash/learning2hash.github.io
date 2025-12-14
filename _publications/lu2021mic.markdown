---
layout: publication
title: 'MIC: Model-agnostic Integrated Cross-channel Recommenders'
authors: Yujie Lu, Ping Nie, Shengyu Zhang, Ming Zhao, Ruobing Xie, William Yang Wang,
  Yi Ren
conference: Arxiv
year: 2021
bibkey: lu2021mic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.11570'}]
tags: [Scalability, Evaluation, Recommender Systems]
short_authors: Lu et al.
---
Semantically connecting users and items is a fundamental problem for the
matching stage of an industrial recommender system. Recent advances in this
topic are based on multi-channel retrieval to efficiently measure users'
interest on items from the massive candidate pool. However, existing work are
primarily built upon pre-defined retrieval channels, including User-CF (U2U),
Item-CF (I2I), and Embedding-based Retrieval (U2I), thus access to the limited
correlation between users and items which solely entail from partial
information of latent interactions. In this paper, we propose a model-agnostic
integrated cross-channel (MIC) approach for the large-scale recommendation,
which maximally leverages the inherent multi-channel mutual information to
enhance the matching performance. Specifically, MIC robustly models correlation
within user-item, user-user, and item-item from latent interactions in a
universal schema. For each channel, MIC naturally aligns pairs with semantic
similarity and distinguishes them otherwise with more uniform anisotropic
representation space. While state-of-the-art methods require specific
architectural design, MIC intuitively considers them as a whole by enabling the
complete information flow among users and items. Thus MIC can be easily plugged
into other retrieval recommender systems. Extensive experiments show that our
MIC helps several state-of-the-art models boost their performance on two
real-world benchmarks. The satisfactory deployment of the proposed MIC on
industrial online services empirically proves its scalability and flexibility.