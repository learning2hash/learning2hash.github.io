---
layout: publication
title: Dynamic Visual Semantic Sub-embeddings And Fast Re-ranking
authors: Wenzhang Wei, Zhipeng Gui, Changguang Wu, Anqi Zhao, Dehua Peng, Huayi Wu
conference: Arxiv
year: 2023
bibkey: wei2023dynamic
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.08154'}]
tags: ["Datasets", "Evaluation", "Re-Ranking"]
short_authors: Wei et al.
---
The core of cross-modal matching is to accurately measure the similarity
between different modalities in a unified representation space. However,
compared to textual descriptions of a certain perspective, the visual modality
has more semantic variations. So, images are usually associated with multiple
textual captions in databases. Although popular symmetric embedding methods
have explored numerous modal interaction approaches, they often learn toward
increasing the average expression probability of multiple semantic variations
within image embeddings. Consequently, information entropy in embeddings is
increased, resulting in redundancy and decreased accuracy. In this work, we
propose a Dynamic Visual Semantic Sub-Embeddings framework (DVSE) to reduce the
information entropy. Specifically, we obtain a set of heterogeneous visual
sub-embeddings through dynamic orthogonal constraint loss. To encourage the
generated candidate embeddings to capture various semantic variations, we
construct a mixed distribution and employ a variance-aware weighting loss to
assign different weights to the optimization process. In addition, we develop a
Fast Re-ranking strategy (FR) to efficiently evaluate the retrieval results and
enhance the performance. We compare the performance with existing set-based
method using four image feature encoders and two text feature encoders on three
benchmark datasets: MSCOCO, Flickr30K and CUB Captions. We also show the role
of different components by ablation studies and perform a sensitivity analysis
of the hyperparameters. The qualitative analysis of visualized bidirectional
retrieval and attention maps further demonstrates the ability of our method to
encode semantic variations.