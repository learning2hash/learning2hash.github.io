---
layout: publication
title: CIMON Towards High-quality Hash Codes
authors: Luo Xiao, Wu Daqing, Ma Zeyu, Chen Chong, Deng Minghua, Ma Jinwen, Jin Zhongming, Huang Jianqiang, Hua Xian-sheng
conference: "Arxiv"
year: 2020
bibkey: luo2020cimon
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2010.07804"}
tags: ['ARXIV', 'Unsupervised']
---
Recently, hashing is widely used in approximate nearest neighbor search for its storage and computational efficiency. Most of the unsupervised hashing methods learn to map images into semantic similarity-preserving hash codes by constructing local semantic similarity structure from the pre-trained model as the guiding information, i.e., treating each point pair similar if their distance is small in feature space. However, due to the inefficient representation ability of the pre-trained model, many false positives and negatives in local semantic similarity will be introduced and lead to error propagation during the hash code learning. Moreover, few of the methods consider the robustness of models, which will cause instability of hash codes to disturbance. In this paper, we propose a new method named \{\textbf\\{C\\}\}omprehensive s\{\textbf\\{I\\}\}milarity \{\textbf\\{M\\}\}ining and c\{\textbf\\{O\\}\}nsistency lear\{\textbf\\{N\\}\}ing (CIMON). First, we use global refinement and similarity statistical distribution to obtain reliable and smooth guidance. Second, both semantic and contrastive consistency learning are introduced to derive both disturb-invariant and discriminative hash codes. Extensive experiments on several benchmark datasets show that the proposed method outperforms a wide range of state-of-the-art methods in both retrieval performance and robustness.
