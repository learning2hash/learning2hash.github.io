---
layout: publication
title: A Frequency-aware Software Cache For Large Recommendation System Embeddings
authors: Jiarui Fang, Geng Zhang, Jiatong Han, Shenggui Li, Zhengda Bian, Yongbin
  Li, Jin Liu, Yang You
conference: Arxiv
year: 2022
bibkey: fang2022a
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.05321'}]
tags: [Evaluation, Recommender Systems, Neural Hashing, Datasets]
short_authors: Fang et al.
---
Deep learning recommendation models (DLRMs) have been widely applied in
Internet companies. The embedding tables of DLRMs are too large to fit on GPU
memory entirely. We propose a GPU-based software cache approaches to
dynamically manage the embedding table in the CPU and GPU memory space by
leveraging the id's frequency statistics of the target dataset. Our proposed
software cache is efficient in training entire DLRMs on GPU in a synchronized
update manner. It is also scaled to multiple GPUs in combination with the
widely used hybrid parallel training approaches. Evaluating our prototype
system shows that we can keep only 1.5% of the embedding parameters in the GPU
to obtain a decent end-to-end training speed.