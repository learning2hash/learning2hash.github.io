---
layout: publication
title: 'Setbert: Enhancing Retrieval Performance For Boolean Logic And Set Operation
  Queries'
authors: Quan Mai, Susan Gauch, Douglas Adams
conference: Proceedings of the 2024 8th International Conference on Natural Language
  Processing and Information Retrieval
year: 2024
bibkey: mai2024setbert
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.17282'}]
tags: [Distance Metric Learning, Evaluation, Text Retrieval, Datasets]
short_authors: Quan Mai, Susan Gauch, Douglas Adams
---
We introduce SetBERT, a fine-tuned BERT-based model designed to enhance query
embeddings for set operations and Boolean logic queries, such as Intersection
(AND), Difference (NOT), and Union (OR). SetBERT significantly improves
retrieval performance for logic-structured queries, an area where both
traditional and neural retrieval methods typically underperform. We propose an
innovative use of inversed-contrastive loss, focusing on identifying the
negative sentence, and fine-tuning BERT with a dataset generated via prompt
GPT. Furthermore, we demonstrate that, unlike other BERT-based models,
fine-tuning with triplet loss actually degrades performance for this specific
task. Our experiments reveal that SetBERT-base not only significantly
outperforms BERT-base (up to a 63% improvement in Recall) but also achieves
performance comparable to the much larger BERT-large model, despite being only
one-third the size.