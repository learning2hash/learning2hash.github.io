---
layout: publication
title: 'Towards Zero-shot Cross-lingual Image Retrieval And Tagging'
authors: Pranav Aggarwal, Ritiz Tambi, Ajinkya Kale
conference: "Arxiv"
year: 2021
citations: 4
bibkey: aggarwal2021towards
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2109.07622'}
  - {name: "Code", url: 'https://github.com/adobe-research/Cross-lingual-Test-Dataset-XTD10'}
tags: ['Cross-Modal', 'Retrieval Models', 'Evaluation', 'Shallow', 'Datasets', 'Vector Indexing', 'Has Code', 'Supervised', 'Training Strategy', 'Applications']
---
There has been a recent spike in interest in multi-modal Language and Vision
problems. On the language side, most of these models primarily focus on English
since most multi-modal datasets are monolingual. We try to bridge this gap with
a zero-shot approach for learning multi-modal representations using
cross-lingual pre-training on the text side. We present a simple yet practical
approach for building a cross-lingual image retrieval model which trains on a
monolingual training dataset but can be used in a zero-shot cross-lingual
fashion during inference. We also introduce a new objective function which
tightens the text embedding clusters by pushing dissimilar texts away from each
other. For evaluation, we introduce a new 1K multi-lingual MSCOCO2014 caption
test dataset (XTD10) in 7 languages that we collected using a crowdsourcing
platform. We use this as the test set for zero-shot model performance across
languages. We also demonstrate how a cross-lingual model can be used for
downstream tasks like multi-lingual image tagging in a zero shot manner. XTD10
dataset is made publicly available here:
https://github.com/adobe-research/Cross-lingual-Test-Dataset-XTD10.
