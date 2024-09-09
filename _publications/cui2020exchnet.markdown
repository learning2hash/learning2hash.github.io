---
layout: publication
title: ExchNet A Unified Hashing Network for Large-Scale Fine-Grained Image Retrieval
authors: Cui Quan, Jiang Qing-Yuan, Wei Xiu-Shen, Li Wu-Jun, Yoshie Osamu
conference: "Arxiv"
year: 2020
bibkey: cui2020exchnet
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2008.01369"}
tags: ['ARXIV', 'Image Retrieval']
---
Retrieving content relevant images from a large-scale fine-grained dataset could suffer from intolerably slow query speed and highly redundant storage cost due to high-dimensional real-valued embeddings which aim to distinguish subtle visual differences of fine-grained objects. In this paper we study the novel fine-grained hashing topic to generate compact binary codes for fine-grained images leveraging the search and storage efficiency of hash learning to alleviate the aforementioned problems. Specifically we propose a unified end-to-end trainable network termed as ExchNet. Based on attention mechanisms and proposed attention constraints it can firstly obtain both local and global features to represent object parts and whole fine-grained objects respectively. Furthermore to ensure the discriminative ability and semantic meanings consistency of these part-level features across images we design a local feature alignment approach by performing a feature exchanging operation. Later an alternative learning algorithm is employed to optimize the whole ExchNet and then generate the final binary hash codes. Validated by extensive experiments our proposal consistently outperforms state-of-the-art generic hashing methods on five fine-grained datasets which shows our effectiveness. Moreover compared with other approximate nearest neighbor methods ExchNet achieves the best speed-up and storage reduction revealing its efficiency and practicality.
