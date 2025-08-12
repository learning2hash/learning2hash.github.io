---
layout: publication
title: 'Muver: Improving First-stage Entity Retrieval With Multi-view Entity Representations'
authors: Xinyin Ma, Yong Jiang, Nguyen Bach, Tao Wang, Zhongqiang Huang, Fei Huang,
  Weiming Lu
conference: Proceedings of the 2021 Conference on Empirical Methods in Natural Language
  Processing
year: 2021
bibkey: ma2021muver
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.05716'}]
tags: ["EMNLP", "Tools & Libraries"]
short_authors: Ma et al.
---
Entity retrieval, which aims at disambiguating mentions to canonical entities
from massive KBs, is essential for many tasks in natural language processing.
Recent progress in entity retrieval shows that the dual-encoder structure is a
powerful and efficient framework to nominate candidates if entities are only
identified by descriptions. However, they ignore the property that meanings of
entity mentions diverge in different contexts and are related to various
portions of descriptions, which are treated equally in previous works. In this
work, we propose Multi-View Entity Representations (MuVER), a novel approach
for entity retrieval that constructs multi-view representations for entity
descriptions and approximates the optimal view for mentions via a heuristic
searching method. Our method achieves the state-of-the-art performance on
ZESHEL and improves the quality of candidates on three standard Entity Linking
datasets