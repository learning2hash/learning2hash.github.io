---
layout: publication
title: 'SMARAGD: Learning Smatch For Accurate And Rapid Approximate Graph Distance'
authors: Juri Opitz, Philipp Meier, Anette Frank
conference: Arxiv
year: 2022
bibkey: opitz2022smaragd
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.13226'}]
tags: ["Scalability"]
short_authors: Juri Opitz, Philipp Meier, Anette Frank
---
The similarity of graph structures, such as Meaning Representations (MRs), is
often assessed via structural matching algorithms, such as Smatch (Cai and
Knight, 2013). However, Smatch involves a combinatorial problem that suffers
from NP-completeness, making large-scale applications, e.g., graph clustering
or search, infeasible. To alleviate this issue, we learn SMARAGD: Semantic
Match for Accurate and Rapid Approximate Graph Distance. We show the potential
of neural networks to approximate Smatch scores, i) in linear time using a
machine translation framework to predict alignments, or ii) in constant time
using a Siamese CNN to directly predict Smatch scores. We show that the
approximation error can be substantially reduced through data augmentation and
graph anonymization.