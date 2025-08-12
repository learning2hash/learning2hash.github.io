---
layout: publication
title: 'Swift Cross-dataset Pruning: Enhancing Fine-tuning Efficiency In Natural Language
  Understanding'
authors: Binh-Nguyen Nguyen, Yang He
conference: Arxiv
year: 2025
bibkey: nguyen2025swift
citations: 0
additional_links: [{name: Code, url: 'https://github.com/he-y/NLP-Dataset-Pruning'},
  {name: Paper, url: 'https://arxiv.org/abs/2501.02432'}]
tags: ["Datasets", "Efficiency"]
short_authors: Binh-Nguyen Nguyen, Yang He
---
Dataset pruning aims to select a subset of a dataset for efficient model
training. While data efficiency in natural language processing has primarily
focused on within-corpus scenarios during model pre-training, efficient dataset
pruning for task-specific fine-tuning across diverse datasets remains
challenging due to variability in dataset sizes, data distributions, class
imbalance and label spaces. Current cross-dataset pruning techniques for
fine-tuning often rely on computationally expensive sample ranking processes,
typically requiring full dataset training or reference models. We address this
gap by proposing Swift Cross-Dataset Pruning (SCDP). Specifically, our approach
uses TF-IDF embeddings with geometric median to rapidly evaluate sample
importance. We then apply dataset size-adaptive pruning to ensure diversity:
for smaller datasets, we retain samples far from the geometric median, while
for larger ones, we employ distance-based stratified pruning. Experimental
results on six diverse datasets demonstrate the effectiveness of our method,
spanning various tasks and scales while significantly reducing computational
resources. Source code is available at:
https://github.com/he-y/NLP-Dataset-Pruning