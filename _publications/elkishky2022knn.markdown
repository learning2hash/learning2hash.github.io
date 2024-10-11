---
layout: publication
title: Knn-embed Locally Smoothed Embedding Mixtures For Multi-interest Candidate Retrieval
authors: El-kishky Ahmed, Markovich Thomas, Leung Kenny, Portman Frank, Haghighi Aria, Xiao Ying
conference: "Arxiv"
year: 2022
bibkey: elkishky2022knn
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2205.06205"}
tags: ['ARXIV', 'Graph', 'Text Retrieval']
---
Candidate retrieval is the first stage in recommendation systems, where a light-weight system is used to retrieve potentially relevant items for an input user. These candidate items are then ranked and pruned in later stages of recommender systems using a more complex ranking model. As the top of the recommendation funnel, it is important to retrieve a high-recall candidate set to feed into downstream ranking models. A common approach is to leverage approximate nearest neighbor (ANN) search from a single dense query embedding; however, this approach this can yield a low-diversity result set with many near duplicates. As users often have multiple interests, candidate retrieval should ideally return a diverse set of candidates reflective of the user's multiple interests. To this end, we introduce kNN-Embed, a general approach to improving diversity in dense ANN-based retrieval. kNN-Embed represents each user as a smoothed mixture over learned item clusters that represent distinct interests of the user. By querying each of a user's mixture component in proportion to their mixture weights, we retrieve a high-diversity set of candidates reflecting elements from each of a user's interests. We experimentally compare kNN-Embed to standard ANN candidate retrieval, and show significant improvements in overall recall and improved diversity across three datasets. Accompanying this work, we open source a large Twitter follow-graph dataset (https://huggingface.co/datasets/Twitter/TwitterFollowGraph), to spur further research in graph-mining and representation learning for recommender systems.
