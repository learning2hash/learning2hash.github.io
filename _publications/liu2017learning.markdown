---
layout: publication
title: Learning Spatiotemporal-aware Representation For POI Recommendation
authors: Bei Liu, Tieyun Qian, Bing Liu, Liang Hong, Zhenni You, Yuxiang Li
conference: Arxiv
year: 2017
bibkey: liu2017learning
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.08853'}]
tags: ["Datasets", "Evaluation", "Recommender Systems", "Robustness"]
short_authors: Liu et al.
---
The wide spread of location-based social networks brings about a huge volume
of user check-in data, which facilitates the recommendation of points of
interest (POIs). Recent advances on distributed representation shed light on
learning low dimensional dense vectors to alleviate the data sparsity problem.
Current studies on representation learning for POI recommendation embed both
users and POIs in a common latent space, and users' preference is inferred
based on the distance/similarity between a user and a POI. Such an approach is
not in accordance with the semantics of users and POIs as they are inherently
different objects. In this paper, we present a novel spatiotemporal aware (STA)
representation, which models the spatial and temporal information as *a
relationship connecting users and POIs*. Our model generalizes the recent
advances in knowledge graph embedding. The basic idea is that the embedding of
a \(<\)time, location\(>\) pair corresponds to a translation from embeddings of
users to POIs. Since the POI embedding should be close to the user embedding
plus the relationship vector, the recommendation can be performed by selecting
the top-*k* POIs similar to the translated POI, which are all of the same
type of objects. We conduct extensive experiments on two real-world datasets.
The results demonstrate that our STA model achieves the state-of-the-art
performance in terms of high recommendation accuracy, robustness to data
sparsity and effectiveness in handling cold start problem.