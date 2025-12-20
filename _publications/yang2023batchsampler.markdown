---
layout: publication
title: 'Batchsampler: Sampling Mini-batches For Contrastive Learning In Vision, Language,
  And Graphs'
authors: Zhen Yang, Tinglin Huang, Ming Ding, Yuxiao Dong, Rex Ying, Yukuo Cen, Yangliao
  Geng, Jie Tang
conference: 'KDD ''23: The 29th ACM SIGKDD Conference on Knowledge Discovery and Data
  Mining'
year: 2023
bibkey: yang2023batchsampler
citations: 8
additional_links: [{name: Code, url: 'https://github.com/THUDM/BatchSampler\'}, {
    name: Paper, url: 'https://arxiv.org/abs/2306.03355'}]
tags: ["Datasets", "Evaluation", "Graph Based ANN", "Self-Supervised", "Supervised"]
short_authors: Yang et al.
---
In-Batch contrastive learning is a state-of-the-art self-supervised method
that brings semantically-similar instances close while pushing dissimilar
instances apart within a mini-batch. Its key to success is the negative sharing
strategy, in which every instance serves as a negative for the others within
the mini-batch. Recent studies aim to improve performance by sampling hard
negatives \textit\{within the current mini-batch\}, whose quality is bounded by
the mini-batch itself. In this work, we propose to improve contrastive learning
by sampling mini-batches from the input data. We present
BatchSampler\footnote\{The code is available at
https://github.com/THUDM/BatchSampler\} to sample mini-batches of
hard-to-distinguish (i.e., hard and true negatives to each other) instances. To
make each mini-batch have fewer false negatives, we design the proximity graph
of randomly-selected instances. To form the mini-batch, we leverage random walk
with restart on the proximity graph to help sample hard-to-distinguish
instances. BatchSampler is a simple and general technique that can be directly
plugged into existing contrastive learning models in vision, language, and
graphs. Extensive experiments on datasets of three modalities show that
BatchSampler can consistently improve the performance of powerful contrastive
models, as shown by significant improvements of SimCLR on ImageNet-100, SimCSE
on STS (language), and GraphCL and MVGRL on graph datasets.