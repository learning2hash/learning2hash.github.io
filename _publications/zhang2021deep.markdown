---
layout: publication
title: Deep Center-based Dual-constrained Hashing For Discriminative Face Image Retrieval
authors: Ming Zhang, Zhe, Yan
conference: Pattern Recognition
year: 2021
bibkey: zhang2021deep
citations: 21
additional_links: [{name: Paper, url: 'https://www.sciencedirect.com/science/article/abs/pii/S0031320321001631'}]
tags: ["Compact Codes", "Datasets", "Efficiency", "Evaluation", "Hashing Methods", "Image Retrieval", "Neural Hashing"]
short_authors: Ming Zhang, Zhe, Yan
---
With the advantages of low storage cost and extremely fast retrieval speed, deep hashing methods have attracted much attention for image retrieval recently. However, large-scale face image retrieval with significant intra-class variations is still challenging. Neither existing pairwise/triplet labels-based nor softmax classification loss-based deep hashing works can generate compact and discriminative binary codes. Considering these issues, we propose a center-based framework integrating end-to-end hashing learning and class centers learning simultaneously. The framework minimizes the intra-class variance by clustering intra-class samples into a learnable class center. To strengthen inter-class separability, it additionally imposes a novel regularization term to enlarge the Hamming distance between pairwise class centers. Moreover, a simple yet effective regression matrix is introduced to encourage intra-class samples to generate the same binary codes, which further enhances the hashing codes compactness. Experiments on four large-scale datasets show the proposed method outperforms state-of-the-art baselines under various code lengths and commonly-used evaluation metrics.