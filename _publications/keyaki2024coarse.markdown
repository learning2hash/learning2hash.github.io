---
layout: publication
title: Coarse-tuning For Ad-hoc Document Retrieval Using Pre-trained Language Models
authors: Atsushi Keyaki, Ribeka Keyaki
conference: Arxiv
year: 2024
bibkey: keyaki2024coarse
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.16915'}]
tags: ["Datasets", "Evaluation", "Text Retrieval"]
short_authors: Atsushi Keyaki, Ribeka Keyaki
---
Fine-tuning in information retrieval systems using pre-trained language
models (PLM-based IR) requires learning query representations and
query-document relations, in addition to downstream task-specific learning.
This study introduces coarse-tuning as an intermediate learning stage that
bridges pre-training and fine-tuning. By learning query representations and
query-document relations in coarse-tuning, we aim to reduce the load of
fine-tuning and improve the learning effect of downstream IR tasks. We propose
Query-Document Pair Prediction (QDPP) for coarse-tuning, which predicts the
appropriateness of query-document pairs. Evaluation experiments show that the
proposed method significantly improves MRR and/or nDCG@5 in four ad-hoc
document retrieval datasets. Furthermore, the results of the query prediction
task suggested that coarse-tuning facilitated learning of query representation
and query-document relations.