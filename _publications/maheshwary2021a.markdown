---
layout: publication
title: A Strong Baseline For Query Efficient Attacks In A Black Box Setting
authors: Rishabh Maheshwary, Saket Maheshwary, Vikram Pudi
conference: Proceedings of the 2021 Conference on Empirical Methods in Natural Language
  Processing
year: 2021
bibkey: maheshwary2021a
citations: 35
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.04775'}]
tags: ["EMNLP", "Evaluation", "Locality-Sensitive-Hashing", "Robustness"]
short_authors: Rishabh Maheshwary, Saket Maheshwary, Vikram Pudi
---
Existing black box search methods have achieved high success rate in
generating adversarial attacks against NLP models. However, such search methods
are inefficient as they do not consider the amount of queries required to
generate adversarial attacks. Also, prior attacks do not maintain a consistent
search space while comparing different search methods. In this paper, we
propose a query efficient attack strategy to generate plausible adversarial
examples on text classification and entailment tasks. Our attack jointly
leverages attention mechanism and locality sensitive hashing (LSH) to reduce
the query count. We demonstrate the efficacy of our approach by comparing our
attack with four baselines across three different search spaces. Further, we
benchmark our results across the same search space used in prior attacks. In
comparison to attacks proposed, on an average, we are able to reduce the query
count by 75% across all datasets and target models. We also demonstrate that
our attack achieves a higher success rate when compared to prior attacks in a
limited query setting.