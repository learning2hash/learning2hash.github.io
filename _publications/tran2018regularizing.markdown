---
layout: publication
title: Regularizing Matrix Factorization With User And Item Embeddings For Recommendation
authors: Thanh Tran, Kyumin Lee, Yiming Liao, Dongwon Lee
conference: Proceedings of the 27th ACM International Conference on Information and
  Knowledge Management
year: 2018
bibkey: tran2018regularizing
citations: 63
additional_links: [{name: Code, url: 'https://github.com/thanhdtran/RME.git'}, {name: Paper,
    url: 'https://arxiv.org/abs/1809.00979'}]
tags: ["CIKM", "Recommender Systems"]
short_authors: Tran et al.
---
Following recent successes in exploiting both latent factor and word
embedding models in recommendation, we propose a novel Regularized
Multi-Embedding (RME) based recommendation model that simultaneously
encapsulates the following ideas via decomposition: (1) which items a user
likes, (2) which two users co-like the same items, (3) which two items users
often co-liked, and (4) which two items users often co-disliked. In
experimental validation, the RME outperforms competing state-of-the-art models
in both explicit and implicit feedback datasets, significantly improving
Recall@5 by 5.9~7.0%, NDCG@20 by 4.3~5.6%, and MAP@10 by 7.9~8.9%. In addition,
under the cold-start scenario for users with the lowest number of interactions,
against the competing models, the RME outperforms NDCG@5 by 20.2% and 29.4% in
MovieLens-10M and MovieLens-20M datasets, respectively. Our datasets and source
code are available at: https://github.com/thanhdtran/RME.git.