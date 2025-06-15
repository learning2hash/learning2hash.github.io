---
layout: publication
title: Hashing As Tie-aware Learning To Rank
authors: He K., Cakir, Bargal, Sclaroff
conference: "Arxiv"
year: 2024
citations: 51
bibkey: he2024hashing
additional_links:
  - {name: "Paper", url: "http://openaccess.thecvf.com/content_cvpr_2018/html/He_Hashing_as_Tie-Aware_CVPR_2018_paper.html"}
tags: ['ARXIV', 'Image Retrieval', 'Supervised']
---
Hashing, or learning binary embeddings of data, is frequently used in nearest neighbor retrieval. In this paper, we develop learning to rank formulations for hashing, aimed at directly optimizing ranking-based evaluation metrics such as Average Precision (AP) and Normalized Discounted Cumulative Gain (NDCG). We first observe that the integer-valued Hamming distance often leads to tied rankings, and propose to use tie-aware versions of AP and NDCG to evaluate hashing for retrieval. Then, to optimize tie-aware ranking metrics, we derive their continuous relaxations, and perform gradient-based optimization with deep neural networks. Our results establish the new state-of-the-art for image retrieval by Hamming ranking in common benchmarks.
