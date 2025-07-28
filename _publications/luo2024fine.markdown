---
layout: publication
title: Fine-grained Embedding Dimension Optimization During Training For Recommender
  Systems
authors: Qinyi Luo, Penghan Wang, Wei Zhang, Fan Lai, Jiachen Mao, Xiaohan Wei, Jun
  Song, Wei-yu Tsai, Shuai Yang, Yuxi Hu, Xuehai Qian
conference: Arxiv
year: 2024
bibkey: luo2024fine
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.04408'}]
tags: ["Recommender Systems"]
short_authors: Luo et al.
---
Huge embedding tables in modern deep learning recommender models (DLRM)
require prohibitively large memory during training and inference. This paper
proposes FIITED, a system to automatically reduce the memory footprint via
FIne-grained In-Training Embedding Dimension pruning. By leveraging the key
insight that embedding vectors are not equally important, FIITED adaptively
adjusts the dimension of each individual embedding vector during model
training, assigning larger dimensions to more important embeddings while
adapting to dynamic changes in data. We prioritize embedding dimensions with
higher frequencies and gradients as more important. To enable efficient pruning
of embeddings and their dimensions during model training, we propose an
embedding storage system based on virtually-hashed physically-indexed hash
tables. Experiments on two industry models and months of realistic datasets
show that FIITED can reduce DLRM embedding size by more than 65% while
preserving model quality, outperforming state-of-the-art in-training embedding
pruning methods. On public datasets, FIITED can reduce the size of embedding
tables by 2.1x to 800x with negligible accuracy drop, while improving model
throughput.