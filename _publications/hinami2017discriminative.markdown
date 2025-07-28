---
layout: publication
title: Discriminative Learning Of Open-vocabulary Object Retrieval And Localization
  By Negative Phrase Augmentation
authors: Ryota Hinami, Shin'ichi Satoh
conference: Proceedings of the 2018 Conference on Empirical Methods in Natural Language
  Processing
year: 2018
bibkey: hinami2017discriminative
citations: 14
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1711.09509'}]
tags: ["EMNLP"]
short_authors: Ryota Hinami, Shin'ichi Satoh
---
Thanks to the success of object detection technology, we can retrieve objects
of the specified classes even from huge image collections. However, the current
state-of-the-art object detectors (such as Faster R-CNN) can only handle
pre-specified classes. In addition, large amounts of positive and negative
visual samples are required for training. In this paper, we address the problem
of open-vocabulary object retrieval and localization, where the target object
is specified by a textual query (e.g., a word or phrase). We first propose
Query-Adaptive R-CNN, a simple extension of Faster R-CNN adapted to
open-vocabulary queries, by transforming the text embedding vector into an
object classifier and localization regressor. Then, for discriminative
training, we then propose negative phrase augmentation (NPA) to mine hard
negative samples which are visually similar to the query and at the same time
semantically mutually exclusive of the query. The proposed method can retrieve
and localize objects specified by a textual query from one million images in
only 0.5 seconds with high precision.