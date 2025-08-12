---
layout: publication
title: Self-supervised Graph Learning For Occasional Group Recommendation
authors: Bowen Hao, Hongzhi Yin, Cuiping Li, Hong Chen
conference: International Journal of Intelligent Systems
year: 2022
bibkey: hao2021self
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.02274'}]
tags: ["Recommender Systems", "Self-Supervised"]
short_authors: Hao et al.
---
As an important branch in Recommender System, occasional group recommendation
has received more and more attention. In this scenario, each occasional group
(cold-start group) has no or few historical interacted items. As each
occasional group has extremely sparse interactions with items, traditional
group recommendation methods can not learn high-quality group representations.
The recent proposed Graph Neural Networks (GNNs), which incorporate the
high-order neighbors of the target occasional group, can alleviate the above
problem in some extent. However, these GNNs still can not explicitly strengthen
the embedding quality of the high-order neighbors with few interactions.
Motivated by the Self-supervised Learning technique, which is able to find the
correlations within the data itself, we propose a self-supervised graph
learning framework, which takes the user/item/group embedding reconstruction as
the pretext task to enhance the embeddings of the cold-start
users/items/groups. In order to explicitly enhance the high-order cold-start
neighbors' embedding quality, we further introduce an embedding enhancer, which
leverages the self-attention mechanism to improve the embedding quality for
them. Comprehensive experiments show the advantages of our proposed framework
than the state-of-the-art methods.