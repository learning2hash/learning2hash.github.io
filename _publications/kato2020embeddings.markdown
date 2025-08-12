---
layout: publication
title: 'Embeddings Of Label Components For Sequence Labeling: A Case Study Of Fine-grained
  Named Entity Recognition'
authors: Takuma Kato, Kaori Abe, Hiroki Ouchi, Shumpei Miyawaki, Jun Suzuki, Kentaro
  Inui
conference: 'Proceedings of the 58th Annual Meeting of the Association for Computational
  Linguistics: Student Research Workshop'
year: 2020
bibkey: kato2020embeddings
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.01372'}]
tags: ["Evaluation"]
short_authors: Kato et al.
---
In general, the labels used in sequence labeling consist of different types
of elements. For example, IOB-format entity labels, such as B-Person and
I-Person, can be decomposed into span (B and I) and type information (Person).
However, while most sequence labeling models do not consider such label
components, the shared components across labels, such as Person, can be
beneficial for label prediction. In this work, we propose to integrate label
component information as embeddings into models. Through experiments on English
and Japanese fine-grained named entity recognition, we demonstrate that the
proposed method improves performance, especially for instances with
low-frequency labels.