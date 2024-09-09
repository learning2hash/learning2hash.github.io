---
layout: publication
title: "Prototype-Based Layered Federated Cross-Modal Hashing"
authors: Liu Jiale, Zhan Yu-Wei, Luo Xin, Chen Zhen-Duo, Wang Yongxin, Xu Xin-Shun
conference: Arxiv
year: 2022
bibkey: liu2022prototype
additional_links:
- {name: "Paper", url: "https://arxiv.org/abs/2210.15678"}
tags: ['ARXIV', 'Cross Modal']
---
Recently, deep cross-modal hashing has gained increasing attention. However, in many practical cases, data are distributed and cannot be collected due to privacy concerns, which greatly reduces the cross-modal hashing performance on each client. And due to the problems of statistical heterogeneity, model heterogeneity, and forcing each client to accept the same parameters, applying federated learning to cross-modal hash learning becomes very tricky. In this paper, we propose a novel method called prototype-based layered federated cross-modal hashing. Specifically, the prototype is introduced to learn the similarity between instances and classes on server, reducing the impact of statistical heterogeneity (non-IID) on different clients. And we monitor the distance between local and global prototypes to further improve the performance. To realize personalized federated learning, a hypernetwork is deployed on server to dynamically update different layers' weights of local model. Experimental results on benchmark datasets show that our method outperforms state-of-the-art methods.