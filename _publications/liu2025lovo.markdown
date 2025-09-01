---
layout: publication
title: 'LOVO: Efficient Complex Object Query In Large-scale Video Datasets'
authors: Yuxin Liu, Yuezhang Peng, Hefeng Zhou, Hongze Liu, Xinyu Lu, Jiong Lou, Chentao
  Wu, Wei Zhao, Jie Li
conference: 2025 IEEE 41st International Conference on Data Engineering (ICDE)
year: 2025
bibkey: liu2025lovo
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2507.14301'}]
tags: ["Datasets", "Evaluation", "Re-Ranking", "Scalability", "Vector Indexing"]
short_authors: Liu et al.
---
The widespread deployment of cameras has led to an exponential increase in video data, creating vast opportunities for applications such as traffic management and crime surveillance. However, querying specific objects from large-scale video datasets presents challenges, including (1) processing massive and continuously growing data volumes, (2) supporting complex query requirements, and (3) ensuring low-latency execution. Existing video analysis methods struggle with either limited adaptability to unseen object classes or suffer from high query latency. In this paper, we present LOVO, a novel system designed to efficiently handle comp\(\underline\{L\}\)ex \(\underline\{O\}\)bject queries in large-scale \(\underline\{V\}\)ide\(\underline\{O\}\) datasets. Agnostic to user queries, LOVO performs one-time feature extraction using pre-trained visual encoders, generating compact visual embeddings for key frames to build an efficient index. These visual embeddings, along with associated bounding boxes, are organized in an inverted multi-index structure within a vector database, which supports queries for any objects. During the query phase, LOVO transforms object queries to query embeddings and conducts fast approximate nearest-neighbor searches on the visual embeddings. Finally, a cross-modal rerank is performed to refine the results by fusing visual features with detailed textual features. Evaluation on real-world video datasets demonstrates that LOVO outperforms existing methods in handling complex queries, with near-optimal query accuracy and up to 85x lower search latency, while significantly reducing index construction costs. This system redefines the state-of-the-art object query approaches in video analysis, setting a new benchmark for complex object queries with a novel, scalable, and efficient approach that excels in dynamic environments.