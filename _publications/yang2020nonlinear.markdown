---
layout: publication
title: Nonlinear Robust Discrete Hashing for Cross-Modal Retrieval
authors: Yang Zhan, Long, Zhu, Huang
conference: Proceedings of the 43rd International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2020
bibkey: yang2020nonlinear
citations: 22
additional_links: [{name: Paper, url: 'https://dl.acm.org/doi/abs/10.1145/3397271.3401152'}]
tags: ["Distance-Metric-Learning", "Datasets", "Multimodal-Retrieval", "SIGIR", "Similarity-Search", "Hashing-Methods", "Evaluation"]
short_authors: Yang et al.
---
Hashing techniques have recently been successfully applied to solve similarity search problems in the information retrieval field because of their significantly reduced storage and high-speed search capabilities. However, the hash codes learned from most recent cross-modal hashing methods lack the ability to comprehensively preserve adequate information, resulting in a less than desirable performance. To solve this limitation, we propose a novel method termed Nonlinear Robust Discrete Hashing (NRDH), for cross-modal retrieval. The main idea behind NRDH is motivated by the success of neural networks, i.e., nonlinear descriptors, in the field of representation learning, and the use of nonlinear descriptors instead of simple linear transformations is more in line with the complex relationships that exist between common latent representation and heterogeneous multimedia data in the real world. In NRDH, we first learn a common latent representation through nonlinear descriptors to encode complementary and consistent information from the features of the heterogeneous multimedia data. Moreover, an asymmetric learning scheme is proposed to correlate the learned hash codes with the common latent representation. Empirically, we demonstrate that NRDH is able to successfully generate a comprehensive common latent representation that significantly improves the quality of the learned hash codes. Then, NRDH adopts a linear learning strategy to fast learn the hash function with the learned hash codes. Extensive experiments performed on two benchmark datasets highlight the superiority of NRDH over several state-of-the-art methods.