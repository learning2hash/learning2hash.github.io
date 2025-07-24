---
layout: publication
title: Partial Scene Text Retrieval
authors: Hao Wang, Minghui Liao, Zhouyi Xie, Wenyu Liu, Xiang Bai
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2024
bibkey: wang2024partial
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2411.10261'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Text Retrieval"]
short_authors: Wang et al.
---
The task of partial scene text retrieval involves localizing and searching
for text instances that are the same or similar to a given query text from an
image gallery. However, existing methods can only handle text-line instances,
leaving the problem of searching for partial patches within these text-line
instances unsolved due to a lack of patch annotations in the training data. To
address this issue, we propose a network that can simultaneously retrieve both
text-line instances and their partial patches. Our method embeds the two types
of data (query text and scene text instances) into a shared feature space and
measures their cross-modal similarities. To handle partial patches, our
proposed approach adopts a Multiple Instance Learning (MIL) approach to learn
their similarities with query text, without requiring extra annotations.
However, constructing bags, which is a standard step of conventional MIL
approaches, can introduce numerous noisy samples for training, and lower
inference speed. To address this issue, we propose a Ranking MIL (RankMIL)
approach to adaptively filter those noisy samples. Additionally, we present a
Dynamic Partial Match Algorithm (DPMA) that can directly search for the target
partial patch from a text-line instance during the inference stage, without
requiring bags. This greatly improves the search efficiency and the performance
of retrieving partial patches. The source code and dataset are available at
https://github.com/lanfeng4659/PSTR.