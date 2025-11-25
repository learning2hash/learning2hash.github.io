---
layout: publication
title: Lexicon-enhanced Self-supervised Training For Multilingual Dense Retrieval
authors: Houxing Ren, Linjun Shou, Jian Pei, Ning Wu, Ming Gong, Daxin Jiang
conference: Arxiv
year: 2023
bibkey: ren2023lexicon
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.14979'}]
tags: ["Datasets", "Evaluation", "Self-Supervised"]
short_authors: Ren et al.
---
Recent multilingual pre-trained models have shown better performance in
various multilingual tasks. However, these models perform poorly on
multilingual retrieval tasks due to lacking multilingual training data. In this
paper, we propose to mine and generate self-supervised training data based on a
large-scale unlabeled corpus. We carefully design a mining method which
combines the sparse and dense models to mine the relevance of unlabeled queries
and passages. And we introduce a query generator to generate more queries in
target languages for unlabeled passages. Through extensive experiments on Mr.
TYDI dataset and an industrial dataset from a commercial search engine, we
demonstrate that our method performs better than baselines based on various
pre-trained multilingual models. Our method even achieves on-par performance
with the supervised method on the latter dataset.