---
layout: publication
title: Unifying Dual-space Embedding For Entity Alignment Via Contrastive Learning
authors: Cunda Wang, Weihua Wang, Qiuyu Liang, Feilong Bao, Guanglai Gao
conference: Arxiv
year: 2024
bibkey: wang2024unifying
citations: 1
additional_links: [{name: Code, url: 'https://github.com/wonderCS1213/UniEA.'}, {
    name: Paper, url: 'https://arxiv.org/abs/2412.05028'}]
tags: [Evaluation, Datasets, Self-Supervised]
short_authors: Wang et al.
---
Entity alignment aims to match identical entities across different knowledge
graphs (KGs). Graph neural network-based entity alignment methods have achieved
promising results in Euclidean space. However, KGs often contain complex
structures, including both local and hierarchical ones, which make it
challenging to efficiently represent them within a single space. In this paper,
we proposed a novel method UniEA, which unifies dual-space embedding to
preserve the intrinsic structure of KGs. Specifically, we learn graph structure
embedding in both Euclidean and hyperbolic spaces simultaneously to maximize
the consistency between the embedding in both spaces. Moreover, we employ
contrastive learning to mitigate the misalignment issues caused by similar
entities, where embedding of similar neighboring entities within the KG become
too close in distance. Extensive experiments on benchmark datasets demonstrate
that our method achieves state-of-the-art performance in structure-based EA.
Our code is available at https://github.com/wonderCS1213/UniEA.