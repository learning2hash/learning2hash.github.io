---
layout: publication
title: A Dual-way Enhanced Framework From Text Matching Point Of View For Multimodal
  Entity Linking
authors: Shezheng Song, Shan Zhao, Chengyu Wang, Tianwei Yan, Shasha Li, Xiaoguang
  Mao, Meng Wang
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2024
bibkey: song2023dual
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.11816'}]
tags: ["AAAI"]
short_authors: Song et al.
---
Multimodal Entity Linking (MEL) aims at linking ambiguous mentions with
multimodal information to entity in Knowledge Graph (KG) such as Wikipedia,
which plays a key role in many applications. However, existing methods suffer
from shortcomings, including modality impurity such as noise in raw image and
ambiguous textual entity representation, which puts obstacles to MEL. We
formulate multimodal entity linking as a neural text matching problem where
each multimodal information (text and image) is treated as a query, and the
model learns the mapping from each query to the relevant entity from candidate
entities. This paper introduces a dual-way enhanced (DWE) framework for MEL:
(1) our model refines queries with multimodal data and addresses semantic gaps
using cross-modal enhancers between text and image information. Besides, DWE
innovatively leverages fine-grained image attributes, including facial
characteristic and scene feature, to enhance and refine visual features. (2)By
using Wikipedia descriptions, DWE enriches entity semantics and obtains more
comprehensive textual representation, which reduces between textual
representation and the entities in KG. Extensive experiments on three public
benchmarks demonstrate that our method achieves state-of-the-art (SOTA)
performance, indicating the superiority of our model. The code is released on
https://github.com/season1blue/DWE