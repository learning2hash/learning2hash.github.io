---
layout: publication
title: Adversarial Cross-modal Retrieval Via Learning And Transferring Single-modal
  Similarities
authors: Xin Wen, Zhizhong Han, Xinyu Yin, Yu-Shen Liu
conference: 2019 IEEE International Conference on Multimedia and Expo (ICME)
year: 2019
bibkey: wen2019adversarial
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.08042'}]
tags: ["Multimodal Retrieval", "Robustness", "Supervised", "Unsupervised"]
short_authors: Wen et al.
---
Cross-modal retrieval aims to retrieve relevant data across different
modalities (e.g., texts vs. images). The common strategy is to apply
element-wise constraints between manually labeled pair-wise items to guide the
generators to learn the semantic relationships between the modalities, so that
the similar items can be projected close to each other in the common
representation subspace. However, such constraints often fail to preserve the
semantic structure between unpaired but semantically similar items (e.g. the
unpaired items with the same class label are more similar than items with
different labels). To address the above problem, we propose a novel cross-modal
similarity transferring (CMST) method to learn and preserve the semantic
relationships between unpaired items in an unsupervised way. The key idea is to
learn the quantitative similarities in single-modal representation subspace,
and then transfer them to the common representation subspace to establish the
semantic relationships between unpaired items across modalities. Experiments
show that our method outperforms the state-of-the-art approaches both in the
class-based and pair-based retrieval tasks.