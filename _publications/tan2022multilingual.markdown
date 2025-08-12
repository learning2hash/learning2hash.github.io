---
layout: publication
title: Multilingual Representation Distillation With Contrastive Learning
authors: Weiting Tan, Kevin Heffernan, Holger Schwenk, Philipp Koehn
conference: Proceedings of the 17th Conference of the European Chapter of the Association
  for Computational Linguistics
year: 2023
bibkey: tan2022multilingual
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.05033'}]
tags: ["Eacl", "Self-Supervised"]
short_authors: Tan et al.
---
Multilingual sentence representations from large models encode semantic
information from two or more languages and can be used for different
cross-lingual information retrieval and matching tasks. In this paper, we
integrate contrastive learning into multilingual representation distillation
and use it for quality estimation of parallel sentences (i.e., find
semantically similar sentences that can be used as translations of each other).
We validate our approach with multilingual similarity search and corpus
filtering tasks. Experiments across different low-resource languages show that
our method greatly outperforms previous sentence encoders such as LASER,
LASER3, and LaBSE.