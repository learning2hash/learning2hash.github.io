---
layout: publication
title: Cross-batch Negative Sampling For Training Two-tower Recommenders
authors: Jinpeng Wang, Jieming Zhu, Xiuqiang He
conference: Proceedings of the 44th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2021
bibkey: wang2021cross
citations: 31
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.15154'}]
tags: ["Efficiency", "Recommender Systems", "SIGIR", "Scalability"]
short_authors: Jinpeng Wang, Jieming Zhu, Xiuqiang He
---
The two-tower architecture has been widely applied for learning item and user
representations, which is important for large-scale recommender systems. Many
two-tower models are trained using various in-batch negative sampling
strategies, where the effects of such strategies inherently rely on the size of
mini-batches. However, training two-tower models with a large batch size is
inefficient, as it demands a large volume of memory for item and user contents
and consumes a lot of time for feature encoding. Interestingly, we find that
neural encoders can output relatively stable features for the same input after
warming up in the training process. Based on such facts, we propose a simple
yet effective sampling strategy called Cross-Batch Negative Sampling (CBNS),
which takes advantage of the encoded item embeddings from recent mini-batches
to boost the model training. Both theoretical analysis and empirical
evaluations demonstrate the effectiveness and the efficiency of CBNS.