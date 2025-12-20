---
layout: publication
title: Multi-task Retrieval For Knowledge-intensive Tasks
authors: "Jean Maillard, Vladimir Karpukhin, Fabio Petroni, Wen-Tau Yih, Barlas O\u011F\
  uz, Veselin Stoyanov, Gargi Ghosh"
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 1: Long Papers)'
year: 2021
bibkey: maillard2021multi
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2101.00117'}]
tags: ["Evaluation", "Few Shot & Zero Shot"]
short_authors: Maillard et al.
---
Retrieving relevant contexts from a large corpus is a crucial step for tasks
such as open-domain question answering and fact checking. Although neural
retrieval outperforms traditional methods like tf-idf and BM25, its performance
degrades considerably when applied to out-of-domain data.
  Driven by the question of whether a neural retrieval model can be universal
and perform robustly on a wide variety of problems, we propose a multi-task
trained model. Our approach not only outperforms previous methods in the
few-shot setting, but also rivals specialised neural retrievers, even when
in-domain training data is abundant. With the help of our retriever, we improve
existing models for downstream tasks and closely match or improve the state of
the art on multiple benchmarks.