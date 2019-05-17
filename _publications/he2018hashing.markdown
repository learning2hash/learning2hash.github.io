---
layout: publication
title: "Hashing as Tie-Aware Learning to Rank"
authors: K. He, F. Cakir, S. Bargal, S. Sclaroff
conference: CVPR
year: 2018
bibkey: he2018hashing
additional_links:
   - {name: "PDF", url: "http://openaccess.thecvf.com/content_cvpr_2018/html/He_Hashing_as_Tie-Aware_CVPR_2018_paper.html"}
   - {name: "Code", url: "https://github.com/kunhe/TALR"}
---
Hashing, or learning binary embeddings of data, is frequently used in nearest neighbor retrieval. In this paper, we develop learning to rank formulations for hashing, aimed at directly optimizing ranking-based evaluation metrics such as Average Precision (AP) and Normalized Discounted Cumulative Gain (NDCG). We first observe that the integer-valued Hamming distance often leads to tied rankings, and propose to use tie-aware versions of AP and NDCG to evaluate hashing for retrieval. Then, to optimize tie-aware ranking metrics, we derive their continuous relaxations, and perform gradient-based optimization with deep neural networks. Our results establish the new state-of-the-art for image retrieval by Hamming ranking in common benchmarks.
