---
layout: publication
title: Distilling Vision45;language Pretraining For Efficient Cross45;modal Retrieval
authors: Jang Young Kyun, Kim Donghyun, Lim Ser-nam
conference: "Arxiv"
year: 2024
bibkey: jang2024distilling
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2405.14726"}
tags: ['ARXIV', 'Quantisation', 'Supervised']
---
Learning to hash is a practical solution for efficient retrieval offering fast search speed and low storage cost. It is widely applied in various applications such as image45;text cross45;modal search. In this paper we explore the potential of enhancing the performance of learning to hash with the proliferation of powerful large pre45;trained models such as Vision45;Language Pre45;training (VLP) models. We introduce a novel method named Distillation for Cross45;Modal Quantization (DCMQ) which leverages the rich semantic knowledge of VLP models to improve hash representation learning. Specifically we use the VLP as a teacher to distill knowledge into a student hashing model equipped with codebooks. This process involves the replacement of supervised labels which are composed of multi45;hot vectors and lack semantics with the rich semantics of VLP. In the end we apply a transformation termed Normalization with Paired Consistency (NPC) to achieve a discriminative target for distillation. Further we introduce a new quantization method Product Quantization with Gumbel (PQG) that promotes balanced codebook learning thereby improving the retrieval performance. Extensive benchmark testing demonstrates that DCMQ consistently outperforms existing supervised cross45;modal hashing approaches showcasing its significant potential.
