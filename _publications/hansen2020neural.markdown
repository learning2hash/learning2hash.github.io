---
layout: publication
title: Content45;aware Neural Hashing For Cold45;start Recommendation
authors: Hansen Casper, Hansen Christian, Simonsen Jakob Grue, Alstrup Stephen, Lioma Christina
conference: "Arxiv"
year: 2020
bibkey: hansen2020neural
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2006.00617"}
tags: ['ARXIV', 'Unsupervised']
---
Content45;aware recommendation approaches are essential for providing meaningful recommendations for textit123;new125; (i.e. textit123;cold45;start125;) items in a recommender system. We present a content45;aware neural hashing45;based collaborative filtering approach (NeuHash45;CF) which generates binary hash codes for users and items such that the highly efficient Hamming distance can be used for estimating user45;item relevance. NeuHash45;CF is modelled as an autoencoder architecture consisting of two joint hashing components for generating user and item hash codes. Inspired from semantic hashing the item hashing component generates a hash code directly from an items content information (i.e. it generates cold45;start and seen item hash codes in the same manner). This contrasts existing state45;of45;the45;art models which treat the two item cases separately. The user hash codes are generated directly based on user id through learning a user embedding matrix. We show experimentally that NeuHash45;CF significantly outperforms state45;of45;the45;art baselines by up to 1237; NDCG and 1337; MRR in cold45;start recommendation settings and up to 437; in both NDCG and MRR in standard settings where all items are present while training. Our approach uses 245;4x shorter hash codes while obtaining the same or better performance compared to the state of the art thus consequently also enabling a notable storage reduction.
