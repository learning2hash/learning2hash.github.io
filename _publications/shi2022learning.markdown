---
layout: publication
title: Learning Similarity Preserving Binary Codes For Recommender Systems
authors: Yang Shi, Young-joo Chung
conference: Arxiv
year: 2022
bibkey: shi2022learning
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2204.08569'}]
tags: ["Compact Codes", "Efficiency", "Evaluation", "Hashing Methods", "Recommender Systems"]
short_authors: Yang Shi, Young-joo Chung
---
Hashing-based Recommender Systems (RSs) are widely studied to provide
scalable services. The existing methods for the systems combine three modules
to achieve efficiency: feature extraction, interaction modeling, and
binarization. In this paper, we study an unexplored module combination for the
hashing-based recommender systems, namely Compact Cross-Similarity Recommender
(CCSR). Inspired by cross-modal retrieval, CCSR utilizes Maximum a Posteriori
similarity instead of matrix factorization and rating reconstruction to model
interactions between users and items. We conducted experiments on MovieLens1M,
Amazon product review, Ichiba purchase dataset and confirmed CCSR outperformed
the existing matrix factorization-based methods. On the Movielens1M dataset,
the absolute performance improvements are up to 15.69% in NDCG and 4.29% in
Recall. In addition, we extensively studied three binarization modules: \\(sign\\),
scaled tanh, and sign-scaled tanh. The result demonstrated that although
differentiable scaled tanh is popular in recent discrete feature learning
literature, a huge performance drop occurs when outputs of scaled \\(tanh\\) are
forced to be binary.