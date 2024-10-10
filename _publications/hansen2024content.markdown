---
layout: publication
title: Content-aware Neural Hashing For Cold-start Recommendation
authors: Hansen Casper, Hansen, Simonsen, Alstrup, Lioma
conference: "Arxiv"
year: 2024
bibkey: hansen2024content
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/hansen2020content"}
tags: ['ARXIV', 'Unsupervised']
---
Content-aware recommendation approaches are essential for providing meaningful recommendations for new (i.e. cold-start) items in a recommender system. We present a content-aware neural hashing-based collaborative filtering approach (NeuHash-CF) which generates binary hash codes for users and items such that the highly efficient Hamming distance can be used for estimating user-item relevance. NeuHash-CF is modelled as an autoencoder architecture consisting of two joint hashing components for generating user and item hash codes. Inspired from semantic hashing the item hashing component generates a hash code directly from an items content information (i.e. it generates cold-start and seen item hash codes in the same manner). This contrasts existing state-of-the-art models which treat the two item cases separately. The user hash codes are generated directly based on user id through learning a user embedding matrix. We show experimentally that NeuHash-CF significantly outperforms state-of-the-art baselines by up to 1237; NDCG and 1337; MRR in cold-start recommendation settings and up to 437; in both NDCG and MRR in standard settings where all items are present while training. Our approach uses 2-4x shorter hash codes while obtaining the same or better performance compared to the state of the art thus consequently also enabling a notable storage reduction.
