---
layout: publication
title: 'Random Offset Block Embedding Array (ROBE) For Criteotb Benchmark Mlperf DLRM
  Model : 1000\(\times\) Compression And 3.1\(\times\) Faster Inference'
authors: Aditya Desai, Li Chou, Anshumali Shrivastava
conference: Arxiv
year: 2021
bibkey: desai2021random
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.02191'}]
tags: ["Hashing Methods", "Memory Efficiency", "Recommender Systems"]
short_authors: Aditya Desai, Li Chou, Anshumali Shrivastava
---
Deep learning for recommendation data is one of the most pervasive and
challenging AI workload in recent times. State-of-the-art recommendation models
are one of the largest models matching the likes of GPT-3 and Switch
Transformer. Challenges in deep learning recommendation models (DLRM) stem from
learning dense embeddings for each of the categorical tokens. These embedding
tables in industrial scale models can be as large as hundreds of terabytes.
Such large models lead to a plethora of engineering challenges, not to mention
prohibitive communication overheads, and slower training and inference times.
Of these, slower inference time directly impacts user experience. Model
compression for DLRM is gaining traction and the community has recently shown
impressive compression results. In this paper, we present Random Offset Block
Embedding Array (ROBE) as a low memory alternative to embedding tables which
provide orders of magnitude reduction in memory usage while maintaining
accuracy and boosting execution speed. ROBE is a simple fundamental approach in
improving both cache performance and the variance of randomized hashing, which
could be of independent interest in itself. We demonstrate that we can
successfully train DLRM models with same accuracy while using \(1000 \times\)
less memory. A \(1000\times\) compressed model directly results in faster
inference without any engineering effort. In particular, we show that we can
train DLRM model using ROBE array of size 100MB on a single GPU to achieve AUC
of 0.8025 or higher as required by official MLPerf CriteoTB benchmark DLRM
model of 100GB while achieving about \(3.1\times\) (209%) improvement in
inference throughput.