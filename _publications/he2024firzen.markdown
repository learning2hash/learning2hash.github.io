---
layout: publication
title: 'Firzen: Firing Strict Cold-start Items With Frozen Heterogeneous And Homogeneous
  Graphs For Recommendation'
authors: Hulingxiao He, Xiangteng He, Yuxin Peng, Zifei Shan, Xin Su
conference: 2024 IEEE 40th International Conference on Data Engineering (ICDE)
year: 2024
bibkey: he2024firzen
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.07654'}]
tags: ["Recommender Systems"]
short_authors: He et al.
---
Recommendation models utilizing unique identities (IDs) to represent distinct
users and items have dominated the recommender systems literature for over a
decade. Since multi-modal content of items (e.g., texts and images) and
knowledge graphs (KGs) may reflect the interaction-related users' preferences
and items' characteristics, they have been utilized as useful side information
to further improve the recommendation quality. However, the success of such
methods often limits to either warm-start or strict cold-start item
recommendation in which some items neither appear in the training data nor have
any interactions in the test stage: (1) Some fail to learn the embedding of a
strict cold-start item since side information is only utilized to enhance the
warm-start ID representations; (2) The others deteriorate the performance of
warm-start recommendation since unrelated multi-modal content or entities in
KGs may blur the final representations. In this paper, we propose a unified
framework incorporating multi-modal content of items and KGs to effectively
solve both strict cold-start and warm-start recommendation termed Firzen, which
extracts the user-item collaborative information over frozen heterogeneous
graph (collaborative knowledge graph), and exploits the item-item semantic
structures and user-user behavioral association over frozen homogeneous graphs
(item-item relation graph and user-user co-occurrence graph). Furthermore, we
build four unified strict cold-start evaluation benchmarks based on publicly
available Amazon datasets and a real-world industrial dataset from Weixin
Channels via rearranging the interaction data and constructing KGs. Extensive
empirical results demonstrate that our model yields significant improvements
for strict cold-start recommendation and outperforms or matches the
state-of-the-art performance in the warm-start scenario.