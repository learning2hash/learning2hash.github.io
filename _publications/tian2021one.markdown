---
layout: publication
title: One Loss For All Deep Hashing With A Single Cosine Similarity Based Learning Objective
authors: Jiun Tian Hoe, Kam Woh Ng, Tianyu Zhang, Chee Seng Chan, Yi-zhe Song, Tao Xiang
conference: "Neural Information Processing Systems"
year: 2021
bibkey: tian2021one
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2021/hash/cbcb58ac2e496207586df2854b17995f-Abstract.html"}
tags: ['NEURIPS', 'Quantisation', 'Supervised']
---
A deep hashing model typically has two main learning objectives to make the learned binary hash codes discriminative and to minimize a quantization error. With further constraints such as bit balance and code orthogonality it is not uncommon for existing models to employ a large number (4) of losses. This leads to difficulties in model training and subsequently impedes their effectiveness. In this work we propose a novel deep hashing model with only textit123;a single learning objective125;. Specifically we show that maximizing the cosine similarity between the continuous codes and their corresponding textit123;binary orthogonal codes125; can ensure both hash code discriminativeness and quantization error minimization. Further with this learning objective code balancing can be achieved by simply using a Batch Normalization (BN) layer and multi45;label classification is also straightforward with label smoothing. The result is a one45;loss deep hashing model that removes all the hassles of tuning the weights of various losses. Importantly extensive experiments show that our model is highly effective outperforming the state45;of45;the45;art multi45;loss hashing models on three large45;scale instance retrieval benchmarks often by significant margins.
