---
layout: publication
title: Improving Visual-semantic Embeddings By Learning Semantically-enhanced Hard
  Negatives For Cross-modal Information Retrieval
authors: Yan Gong, Georgina Cosma
conference: Pattern Recognition
year: 2022
bibkey: gong2022improving
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.04754'}]
tags: ["Datasets", "Evaluation"]
short_authors: Yan Gong, Georgina Cosma
---
Visual Semantic Embedding (VSE) aims to extract the semantics of images and
their descriptions, and embed them into the same latent space for cross-modal
information retrieval. Most existing VSE networks are trained by adopting a
hard negatives loss function which learns an objective margin between the
similarity of relevant and irrelevant image-description embedding pairs.
However, the objective margin in the hard negatives loss function is set as a
fixed hyperparameter that ignores the semantic differences of the irrelevant
image-description pairs. To address the challenge of measuring the optimal
similarities between image-description pairs before obtaining the trained VSE
networks, this paper presents a novel approach that comprises two main parts:
(1) finds the underlying semantics of image descriptions; and (2) proposes a
novel semantically enhanced hard negatives loss function, where the learning
objective is dynamically determined based on the optimal similarity scores
between irrelevant image-description pairs. Extensive experiments were carried
out by integrating the proposed methods into five state-of-the-art VSE networks
that were applied to three benchmark datasets for cross-modal information
retrieval tasks. The results revealed that the proposed methods achieved the
best performance and can also be adopted by existing and future VSE networks.