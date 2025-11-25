---
layout: publication
title: Progressively Optimized Bi-granular Document Representation For Scalable Embedding
  Based Retrieval
authors: Shitao Xiao, Zheng Liu, Weihao Han, Jianjin Zhang, Yingxia Shao, Defu Lian,
  Chaozhuo Li, Hao Sun, Denvy Deng, Liangjie Zhang, Qi Zhang, Xing Xie
conference: Proceedings of the ACM Web Conference 2022
year: 2022
bibkey: xiao2022progressively
citations: 16
additional_links: [{name: Code, url: 'https://github.com/microsoft/BiDR'}, {name: Paper,
    url: 'https://arxiv.org/abs/2201.05409'}]
tags: ["Large Scale Search", "Quantization", "Scalability", "Similarity Search"]
short_authors: Xiao et al.
---
Ad-hoc search calls for the selection of appropriate answers from a
massive-scale corpus. Nowadays, the embedding-based retrieval (EBR) becomes a
promising solution, where deep learning based document representation and ANN
search techniques are allied to handle this task. However, a major challenge is
that the ANN index can be too large to fit into memory, given the considerable
size of answer corpus. In this work, we tackle this problem with Bi-Granular
Document Representation, where the lightweight sparse embeddings are indexed
and standby in memory for coarse-grained candidate search, and the heavyweight
dense embeddings are hosted in disk for fine-grained post verification. For the
best of retrieval accuracy, a Progressive Optimization framework is designed.
The sparse embeddings are learned ahead for high-quality search of candidates.
Conditioned on the candidate distribution induced by the sparse embeddings, the
dense embeddings are continuously learned to optimize the discrimination of
ground-truth from the shortlisted candidates. Besides, two techniques: the
contrastive quantization and the locality-centric sampling are introduced for
the learning of sparse and dense embeddings, which substantially contribute to
their performances. Thanks to the above features, our method effectively
handles massive-scale EBR with strong advantages in accuracy: with up to +4.3%
recall gain on million-scale corpus, and up to +17.5% recall gain on
billion-scale corpus. Besides, Our method is applied to a major sponsored
search platform with substantial gains on revenue (+1.95%), Recall (+1.01%) and
CTR (+0.49%). Our code is available at https://github.com/microsoft/BiDR.