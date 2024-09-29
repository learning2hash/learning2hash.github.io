---
layout: publication
title: HS45;GCN Hamming Spatial Graph Convolutional Networks For Recommendation
authors: Liu Han, Wei Yinwei, Yin Jianhua, Nie Liqiang
conference: "Arxiv"
year: 2023
bibkey: liu2023hamming
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2301.05430"}
tags: ['ARXIV', 'Graph', 'Independent']
---
An efficient solution to the large45;scale recommender system is to represent users and items as binary hash codes in the Hamming space. Towards this end existing methods tend to code users by modeling their Hamming similarities with the items they historically interact with which are termed as the first45;order similarities in this work. Despite their efficiency these methods suffer from the suboptimal representative capacity since they forgo the correlation established by connecting multiple first45;order similarities i.e. the relation among the indirect instances which could be defined as the high45;order similarity. To tackle this drawback we propose to model both the first45; and the high45;order similarities in the Hamming space through the user45;item bipartite graph. Therefore we develop a novel learning to hash framework namely Hamming Spatial Graph Convolutional Networks (HS45;GCN) which explicitly models the Hamming similarity and embeds it into the codes of users and items. Extensive experiments on three public benchmark datasets demonstrate that our proposed model significantly outperforms several state45;of45;the45;art hashing models and obtains performance comparable with the real45;valued recommendation models.
