---
layout: publication
title: Ordered And Binary Speaker Embedding
authors: Jiaying Wang, Xianglong Wang, Namin Wang, Lantian Li, Dong Wang
conference: Arxiv
year: 2023
bibkey: wang2023ordered
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.16043'}]
tags: [Compact Codes, Efficiency, Datasets, Memory Efficiency, Hashing Methods]
short_authors: Wang et al.
---
Modern speaker recognition systems represent utterances by embedding vectors.
Conventional embedding vectors are dense and non-structural. In this paper, we
propose an ordered binary embedding approach that sorts the dimensions of the
embedding vector via a nested dropout and converts the sorted vectors to binary
codes via Bernoulli sampling. The resultant ordered binary codes offer some
important merits such as hierarchical clustering, reduced memory usage, and
fast retrieval. These merits were empirically verified by comprehensive
experiments on a speaker identification task with the VoxCeleb and CN-Celeb
datasets.