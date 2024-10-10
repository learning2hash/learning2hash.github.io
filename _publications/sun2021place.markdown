---
layout: publication
title: 3rd Place A Global And Local Dual Retrieval Solution To Facebook AI Image Similarity Challenge
authors: Sun Xinlong, Qin Yangyang, Xu Xuyuan, Gong Guoping, Fang Yang, Wang Yexin
conference: "Arxiv"
year: 2021
bibkey: sun2021place
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2112.02373"}
tags: ['ARXIV', 'Supervised']
---
As a basic task of computer vision image similarity retrieval is facing the challenge of large-scale data and image copy attacks. This paper presents our 3rd place solution to the matching track of Image Similarity Challenge (ISC) 2021 organized by Facebook AI. We propose a multi-branch retrieval method of combining global descriptors and local descriptors to cover all attack cases. Specifically we attempt many strategies to optimize global descriptors including abundant data augmentations self-supervised learning with a single Transformer model overlay detection preprocessing. Moreover we introduce the robust SIFT feature and GPU Faiss for local retrieval which makes up for the shortcomings of the global retrieval. Finally KNN-matching algorithm is used to judge the match and merge scores. We show some ablation experiments of our method which reveals the complementary advantages of global and local features.
