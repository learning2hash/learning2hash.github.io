---
layout: publication
title: 'Wolfies At Semeval-2022 Task 8: Feature Extraction Pipeline With Transformers
  For Multi-lingual News Article Similarity'
authors: Nikhil Goel, Ranjith Reddy
conference: Proceedings of the 16th International Workshop on Semantic Evaluation
  (SemEval-2022)
year: 2022
bibkey: goel2022wolfies
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.09715'}]
tags: ["Datasets", "Distance Metric Learning", "Evaluation"]
short_authors: Nikhil Goel, Ranjith Reddy
---
This work is about finding the similarity between a pair of news articles.
There are seven different objective similarity metrics provided in the dataset
for each pair and the news articles are in multiple different languages. On top
of the pre-trained embedding model, we calculated cosine similarity for
baseline results and feed-forward neural network was then trained on top of it
to improve the results. We also built separate pipelines for each similarity
metric for feature extraction. We could see significant improvement from
baseline results using feature extraction and feed-forward neural network.