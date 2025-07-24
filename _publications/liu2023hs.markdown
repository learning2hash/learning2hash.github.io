---
layout: publication
title: 'HS-GCN: Hamming Spatial Graph Convolutional Networks For Recommendation'
authors: Han Liu, Yinwei Wei, Jianhua Yin, Liqiang Nie
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2022
bibkey: liu2023hs
citations: 34
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.05430'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Hashing Methods", "Recommender Systems", "Scalability"]
short_authors: Liu et al.
---
An efficient solution to the large-scale recommender system is to represent
users and items as binary hash codes in the Hamming space. Towards this end,
existing methods tend to code users by modeling their Hamming similarities with
the items they historically interact with, which are termed as the first-order
similarities in this work. Despite their efficiency, these methods suffer from
the suboptimal representative capacity, since they forgo the correlation
established by connecting multiple first-order similarities, i.e., the relation
among the indirect instances, which could be defined as the high-order
similarity. To tackle this drawback, we propose to model both the first- and
the high-order similarities in the Hamming space through the user-item
bipartite graph. Therefore, we develop a novel learning to hash framework,
namely Hamming Spatial Graph Convolutional Networks (HS-GCN), which explicitly
models the Hamming similarity and embeds it into the codes of users and items.
Extensive experiments on three public benchmark datasets demonstrate that our
proposed model significantly outperforms several state-of-the-art hashing
models, and obtains performance comparable with the real-valued recommendation
models.