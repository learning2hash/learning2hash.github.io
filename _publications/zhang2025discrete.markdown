---
layout: publication
title: Discrete Scale-invariant Metric Learning for Efficient Collaborative Filtering
authors: Zhang et al.
conference: Information Retrieval
year: 2025
bibkey: zhang2025discrete
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.09898'}]
tags: [SIGIR, Distance Metric Learning, Recommender Systems]
---
Metric learning has attracted extensive interest for its ability to provide personalized recommendations based on the importance of observed user-item interactions. Current metric learning methods aim to push negative items away from the corresponding users and positive items by an absolute geometrical distance margin. However, items may come from imbalanced categories with different intra-class variations. Thus, the absolute distance margin may not be ideal for estimating the difference between user preferences over imbalanced items. To this end, we propose a new method, named discrete scale-invariant metric learning (DSIML), by adding binary constraints to users and items, which maps users and items into binary codes of a shared Hamming subspace to speed up the online recommendation. Specifically, we firstly propose a scale-invariant margin based on angles at the negative item points in the shared Hamming subspace. Then, we derive a scale-invariant triple hinge loss based on the margin. To capture more preference difference information, we integrate a pairwise ranking loss into the scale-invariant loss in the proposed model. Due to the difficulty of directly optimizing the mixed integer optimization problem formulated with \textit\{log-sum-exp\} functions, we seek to optimize its variational quadratic upper bound and learn hash codes with an alternating optimization strategy. Experiments on benchmark datasets clearly show that our proposed method is superior to competitive metric learning and hashing-based baselines for recommender systems. The implementation code is available at https://github.com/AnonyFeb/dsml.