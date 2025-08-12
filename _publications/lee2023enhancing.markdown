---
layout: publication
title: Enhancing Low-resource Fine-grained Named Entity Recognition By Leveraging
  Coarse-grained Datasets
authors: Su Ah Lee, Seokjin Oh, Woohwan Jung
conference: Proceedings of the 2023 Conference on Empirical Methods in Natural Language
  Processing
year: 2023
bibkey: lee2023enhancing
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2310.11715'}]
tags: ["EMNLP"]
short_authors: Su Ah Lee, Seokjin Oh, Woohwan Jung
---
Named Entity Recognition (NER) frequently suffers from the problem of
insufficient labeled data, particularly in fine-grained NER scenarios. Although
\(K\)-shot learning techniques can be applied, their performance tends to
saturate when the number of annotations exceeds several tens of labels. To
overcome this problem, we utilize existing coarse-grained datasets that offer a
large number of annotations. A straightforward approach to address this problem
is pre-finetuning, which employs coarse-grained data for representation
learning. However, it cannot directly utilize the relationships between
fine-grained and coarse-grained entities, although a fine-grained entity type
is likely to be a subcategory of a coarse-grained entity type. We propose a
fine-grained NER model with a Fine-to-Coarse(F2C) mapping matrix to leverage
the hierarchical structure explicitly. In addition, we present an inconsistency
filtering method to eliminate coarse-grained entities that are inconsistent
with fine-grained entity types to avoid performance degradation. Our
experimental results show that our method outperforms both \(K\)-shot learning
and supervised learning methods when dealing with a small number of
fine-grained annotations.