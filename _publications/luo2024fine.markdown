---
layout: publication
title: Fine-grained Embedding Dimension Optimization During Training For Recommender Systems
authors: Luo Qinyi, Wang Penghan, Zhang Wei, Lai Fan, Mao Jiachen, Wei Xiaohan, Song Jun, Tsai Wei-yu, Yang Shuai, Hu Yuxi, Qian Xuehai
conference: "Arxiv"
year: 2024
bibkey: luo2024fine
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2401.04408"}
tags: ['ARXIV', 'Deep Learning']
---
Huge embedding tables in modern Deep Learning Recommender Models (DLRM) require prohibitively large memory during training and inference. Aiming to reduce the memory footprint of training this paper proposes FIne-grained In-Training Embedding Dimension optimization (FIITED). Given the observation that embedding vectors are not equally important FIITED adjusts the dimension of each individual embedding vector continuously during training assigning longer dimensions to more important embeddings while adapting to dynamic changes in data. A novel embedding storage system based on virtually-hashed physically-indexed hash tables is designed to efficiently implement the embedding dimension adjustment and effectively enable memory saving. Experiments on two industry models show that FIITED is able to reduce the size of embeddings by more than 6537; while maintaining the trained models quality saving significantly more memory than a state-of-the-art in-training embedding pruning method. On public click-through rate prediction datasets FIITED is able to prune up to 93.7537;-99.7537; embeddings without significant accuracy loss.
