---
layout: publication
title: On Measuring The Intrinsic Few-shot Hardness Of Datasets
authors: Xinran Zhao, Shikhar Murty, Christopher D. Manning
conference: Proceedings of the 2022 Conference on Empirical Methods in Natural Language
  Processing
year: 2022
bibkey: zhao2022measuring
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.09113'}]
tags: ["Datasets", "EMNLP", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Xinran Zhao, Shikhar Murty, Christopher D. Manning
---
While advances in pre-training have led to dramatic improvements in few-shot
learning of NLP tasks, there is limited understanding of what drives successful
few-shot adaptation in datasets. In particular, given a new dataset and a
pre-trained model, what properties of the dataset make it *few-shot
learnable* and are these properties independent of the specific adaptation
techniques used? We consider an extensive set of recent few-shot learning
methods, and show that their performance across a large number of datasets is
highly correlated, showing that few-shot hardness may be intrinsic to datasets,
for a given pre-trained model. To estimate intrinsic few-shot hardness, we then
propose a simple and lightweight metric called "Spread" that captures the
intuition that few-shot learning is made possible by exploiting feature-space
invariances between training and test samples. Our metric better accounts for
few-shot hardness compared to existing notions of hardness, and is ~8-100x
faster to compute.