---
layout: publication
title: IDEA An Invariant Perspective For Efficient Domain Adaptive Image Retrieval
authors: Wang Haixin, Wu, Sun, Zhang, Chen, Hua, Luo
conference: "Arxiv"
year: 2024
bibkey: wang2024idea
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/wang2023idea"}
tags: ['ARXIV', 'Cross Modal', 'Image Retrieval', 'Unsupervised']
---
In this paper we investigate the problem of unsupervised domain adaptive hashing which leverage knowledge from a label-rich source domain to expedite learning to hash on a label-scarce target domain. Although numerous existing approaches attempt to incorporate transfer learning techniques into deep hashing frameworks they often neglect the essential invariance for adequate alignment between these two domains. Worse yet these methods fail to distinguish between causal and non-causal effects embedded in images rendering cross-domain retrieval ineffective. To address these challenges we propose an Invariance-acquired Domain AdaptivE HAshing (IDEA) model. Our IDEA first decomposes each image into a causal feature representing label information and a non-causal feature indicating domain information. Subsequently we generate discriminative hash codes using causal features with consistency learning on both source and target domains. More importantly we employ a generative model for synthetic samples to simulate the intervention of various non-causal effects ultimately minimizing their impact on hash codes for domain invariance. Comprehensive experiments conducted on benchmark datasets validate the superior performance of our IDEA compared to a variety of competitive baselines.
