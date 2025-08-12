---
layout: publication
title: Learning Representations For Clustering Via Partial Information Discrimination
  And Cross-level Interaction
authors: Hai-Xin Zhang, Dong Huang, Hua-Bao Ling, Guang-Yu Zhang, Wei-Jun Sun, Zi-Hao
  Wen
conference: Arxiv
year: 2024
bibkey: zhang2024learning
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Regan-Zhang/PICI'}, {name: Paper,
    url: 'https://arxiv.org/abs/2401.13503'}]
tags: ["Self-Supervised"]
short_authors: Zhang et al.
---
In this paper, we present a novel deep image clustering approach termed PICI,
which enforces the partial information discrimination and the cross-level
interaction in a joint learning framework. In particular, we leverage a
Transformer encoder as the backbone, through which the masked image modeling
with two paralleled augmented views is formulated. After deriving the class
tokens from the masked images by the Transformer encoder, three partial
information learning modules are further incorporated, including the PISD
module for training the auto-encoder via masked image reconstruction, the PICD
module for employing two levels of contrastive learning, and the CLI module for
mutual interaction between the instance-level and cluster-level subspaces.
Extensive experiments have been conducted on six real-world image datasets,
which demononstrate the superior clustering performance of the proposed PICI
approach over the state-of-the-art deep clustering approaches. The source code
is available at https://github.com/Regan-Zhang/PICI.