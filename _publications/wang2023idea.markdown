---
layout: publication
title: "IDEA: An Invariant Perspective for Efficient Domain Adaptive Image Retrieval"
authors: Haixin Wang, Hao Wu, Jinan Sun, Shikun Zhang, Chong Chen, Xian-Sheng Hua, Xiao Luo
conference: NeurIPS
year: 2023
bibkey: wang2023idea
additional_links:
   - {name: "PDF", url: "https://proceedings.neurips.cc/paper_files/paper/2023/file/b33ad9d46ab2a23b6783d954121d26e3-Paper-Conference.pdf"}
tags: ["TOMM", "Unsupervised", "Deep Learning"]
---
In this paper, we investigate the problem of unsupervised domain adaptive hashing, which leverage knowledge from a label-rich source domain to expedite learning to hash on a label-scarce target domain. Although numerous existing approaches attempt to incorporate transfer learning techniques into deep hashing frameworks, they often neglect the essential invariance for adequate alignment between these two domains. Worse yet, these methods fail to distinguish between causal and non-causal effects embedded in images, rendering cross-domain retrieval ineffective. To address these challenges, we propose an Invariance-acquired Domain AdaptivE HAshing (IDEA) model. Our IDEA first decomposes each image into a causal feature representing label information, and a non-causal feature indicating domain information. Subsequently, we generate discriminative hash codes using causal features with consistency learning on both source and target domains. More importantly, we employ a generative model for synthetic samples to simulate the intervention of various non-causal effects, ultimately minimizing their impact on hash codes for domain invariance. Comprehensive experiments conducted on benchmark datasets validate the superior performance of our IDEA compared to a variety of competitive baselines.
