---
layout: publication
title: Locality-sensitive Experience Replay For Online Recommendation
authors: Xiaocong Chen, Lina Yao, Xianzhi Wang, Julian McAuley
conference: Arxiv
year: 2021
bibkey: chen2021locality
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.10850'}]
tags: ["Evaluation", "Hashing Methods", "Locality-Sensitive-Hashing", "Recommender Systems"]
short_authors: Chen et al.
---
Online recommendation requires handling rapidly changing user preferences.
Deep reinforcement learning (DRL) is gaining interest as an effective means of
capturing users' dynamic interest during interactions with recommender systems.
However, it is challenging to train a DRL agent, due to large state space
(e.g., user-item rating matrix and user profiles), action space (e.g.,
candidate items), and sparse rewards. Existing studies encourage the agent to
learn from past experience via experience replay (ER). They adapt poorly to the
complex environment of online recommender systems and are inefficient in
determining an optimal strategy from past experience. To address these issues,
we design a novel state-aware experience replay model, which uses
locality-sensitive hashing to map high dimensional data into low-dimensional
representations and a prioritized reward-driven strategy to replay more
valuable experience at a higher chance. Our model can selectively pick the most
relevant and salient experiences and recommend the agent with the optimal
policy. Experiments on three online simulation platforms demonstrate our model'
feasibility and superiority toseveral existing experience replay methods.