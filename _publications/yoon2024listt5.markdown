---
layout: publication
title: 'Listt5: Listwise Reranking With Fusion-in-decoder Improves Zero-shot Retrieval'
authors: Soyoung Yoon, Eunbi Choi, Jiyeon Kim, Hyeongu Yun, Yireun Kim, Seung-Won
  Hwang
conference: 'Proceedings of the 62nd Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2024
bibkey: yoon2024listt5
citations: 5
additional_links: [{name: Code, url: 'https://github.com/soyoung97/ListT5'}, {name: Paper,
    url: 'https://arxiv.org/abs/2402.15838'}]
tags: [Evaluation, Re-ranking, Few-shot & Zero-shot, Efficiency, Tools & Libraries,
  Hybrid ANN Methods, ACL]
short_authors: Yoon et al.
---
We propose ListT5, a novel reranking approach based on Fusion-in-Decoder
(FiD) that handles multiple candidate passages at both train and inference
time. We also introduce an efficient inference framework for listwise ranking
based on m-ary tournament sort with output caching. We evaluate and compare our
model on the BEIR benchmark for zero-shot retrieval task, demonstrating that
ListT5 (1) outperforms the state-of-the-art RankT5 baseline with a notable +1.3
gain in the average NDCG@10 score, (2) has an efficiency comparable to
pointwise ranking models and surpasses the efficiency of previous listwise
ranking models, and (3) overcomes the lost-in-the-middle problem of previous
listwise rerankers. Our code, model checkpoints, and the evaluation framework
are fully open-sourced at https://github.com/soyoung97/ListT5.