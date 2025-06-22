---
layout: publication
title: Towards Effective Top-n Hamming Search Via Bipartite Graph Contrastive Hashing
authors: Yankai Chen et al.
conference: Arxiv
year: 2024
citations: 0
bibkey: chen2024towards
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.09239'}]
tags: [Hashing Methods, Applications, RecSys, Evaluation Metrics, Supervised]
---
Searching on bipartite graphs serves as a fundamental task for various
real-world applications, such as recommendation systems, database retrieval,
and document querying. Conventional approaches rely on similarity matching in
continuous Euclidean space of vectorized node embeddings. To handle intensive
similarity computation efficiently, hashing techniques for graph-structured
data have emerged as a prominent research direction. However, despite the
retrieval efficiency in Hamming space, previous studies have encountered
catastrophic performance decay. To address this challenge, we investigate the
problem of hashing with Graph Convolutional Network for effective Top-N search.
Our findings indicate the learning effectiveness of incorporating hashing
techniques within the exploration of bipartite graph reception fields, as
opposed to simply treating hashing as post-processing to output embeddings. To
further enhance the model performance, we advance upon these findings and
propose Bipartite Graph Contrastive Hashing (BGCH+). BGCH+ introduces a novel
dual augmentation approach to both intermediate information and hash code
outputs in the latent feature spaces, thereby producing more expressive and
robust hash codes within a dual self-supervised learning paradigm.
Comprehensive empirical analyses on six real-world benchmarks validate the
effectiveness of our dual feature contrastive learning in boosting the
performance of BGCH+ compared to existing approaches.