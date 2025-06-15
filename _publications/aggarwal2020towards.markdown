---
layout: publication
title: 'Towards Zero-shot Cross-lingual Image Retrieval'
authors: Pranav Aggarwal, Ajinkya Kale
conference: "Arxiv"
year: 2020
citations: 16
bibkey: aggarwal2020towards
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2012.05107'}
  - {name: "Code", url: 'https://github.com/adobe-research/Cross-lingual-Test-Dataset-XTD10'}
tags: ['Tools and Libraries', 'Has Code', 'Applications']
---
There has been a recent spike in interest in multi-modal Language and Vision
problems. On the language side, most of these models primarily focus on English
since most multi-modal datasets are monolingual. We try to bridge this gap with
a zero-shot approach for learning multi-modal representations using
cross-lingual pre-training on the text side. We present a simple yet practical
approach for building a cross-lingual image retrieval model which trains on a
monolingual training dataset but can be used in a zero-shot cross-lingual
fashion during inference. We also introduce a new objective function which
tightens the text embedding clusters by pushing dissimilar texts from each
other. Finally, we introduce a new 1K multi-lingual MSCOCO2014 caption test
dataset (XTD10) in 7 languages that we collected using a crowdsourcing
platform. We use this as the test set for evaluating zero-shot model
performance across languages. XTD10 dataset is made publicly available here:
https://github.com/adobe-research/Cross-lingual-Test-Dataset-XTD10
