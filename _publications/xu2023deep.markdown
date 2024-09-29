---
layout: publication
title: Deep Lifelong Cross45;modal Hashing
authors: Xu Liming, Li Hanqi, Zheng Bochuan, Li Weisheng, Lv Jiancheng
conference: "Arxiv"
year: 2023
bibkey: xu2023deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2304.13357"}
tags: ['ARXIV', 'Cross Modal', 'Deep Learning', 'Supervised']
---
Hashing methods have made significant progress in cross45;modal retrieval tasks with fast query speed and low storage cost. Among them deep learning45;based hashing achieves better performance on large45;scale data due to its excellent extraction and representation ability for nonlinear heterogeneous features. However there are still two main challenges in catastrophic forgetting when data with new categories arrive continuously and time45;consuming for non45;continuous hashing retrieval to retrain for updating. To this end we in this paper propose a novel deep lifelong cross45;modal hashing to achieve lifelong hashing retrieval instead of re45;training hash function repeatedly when new data arrive. Specifically we design lifelong learning strategy to update hash functions by directly training the incremental data instead of retraining new hash functions using all the accumulated data which significantly reduce training time. Then we propose lifelong hashing loss to enable original hash codes participate in lifelong learning but remain invariant and further preserve the similarity and dis45;similarity among original and incremental hash codes to maintain performance. Additionally considering distribution heterogeneity when new data arriving continuously we introduce multi45;label semantic similarity to supervise hash learning and it has been proven that the similarity improves performance with detailed analysis. Experimental results on benchmark datasets show that the proposed methods achieves comparative performance comparing with recent state45;of45;the45;art cross45;modal hashing methods and it yields substantial average increments over 2037; in retrieval accuracy and almost reduces over 8037; training time when new data arrives continuously.
