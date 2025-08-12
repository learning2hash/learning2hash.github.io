---
layout: publication
title: Simple And Effective Few-shot Named Entity Recognition With Structured Nearest
  Neighbor Learning
authors: Yi Yang, Arzoo Katiyar
conference: Proceedings of the 2020 Conference on Empirical Methods in Natural Language
  Processing (EMNLP)
year: 2020
bibkey: yang2020simple
citations: 162
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.02405'}]
tags: ["EMNLP", "Few Shot & Zero Shot"]
short_authors: Yi Yang, Arzoo Katiyar
---
We present a simple few-shot named entity recognition (NER) system based on
nearest neighbor learning and structured inference. Our system uses a
supervised NER model trained on the source domain, as a feature extractor.
Across several test domains, we show that a nearest neighbor classifier in this
feature-space is far more effective than the standard meta-learning approaches.
We further propose a cheap but effective method to capture the label
dependencies between entity tags without expensive CRF training. We show that
our method of combining structured decoding with nearest neighbor learning
achieves state-of-the-art performance on standard few-shot NER evaluation
tasks, improving F1 scores by \(6%\) to \(16%\) absolute points over prior
meta-learning based systems.