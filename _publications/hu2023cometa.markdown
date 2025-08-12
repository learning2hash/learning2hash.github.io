---
layout: publication
title: 'Cometa: Enhancing Meta Embeddings With Collaborative Information In Cold-start
  Problem Of Recommendation'
authors: Haonan Hu, Dazhong Rong, Jianhai Chen, Qinming He, Zhenguang Liu
conference: Lecture Notes in Computer Science
year: 2023
bibkey: hu2023cometa
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.07607'}]
tags: ["Recommender Systems"]
short_authors: Hu et al.
---
The cold-start problem is quite challenging for existing recommendation
models. Specifically, for the new items with only a few interactions, their ID
embeddings are trained inadequately, leading to poor recommendation
performance. Some recent studies introduce meta learning to solve the
cold-start problem by generating meta embeddings for new items as their initial
ID embeddings. However, we argue that the capability of these methods is
limited, because they mainly utilize item attribute features which only contain
little information, but ignore the useful collaborative information contained
in the ID embeddings of users and old items. To tackle this issue, we propose
CoMeta to enhance the meta embeddings with the collaborative information.
CoMeta consists of two submodules: B-EG and S-EG. Specifically, for a new item:
B-EG calculates the similarity-based weighted sum of the ID embeddings of old
items as its base embedding; S-EG generates its shift embedding not only with
its attribute features but also with the average ID embedding of the users who
interacted with it. The final meta embedding is obtained by adding up the base
embedding and the shift embedding. We conduct extensive experiments on two
public datasets. The experimental results demonstrate both the effectiveness
and the compatibility of CoMeta.