---
layout: publication
title: Entity-aware Image Caption Generation
authors: di Lu, Spencer Whitehead, Lifu Huang, Heng Ji, Shih-Fu Chang
conference: Proceedings of the 2018 Conference on Empirical Methods in Natural Language
  Processing
year: 2018
bibkey: lu2018entity
citations: 66
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.07889'}]
tags: ["Datasets", "EMNLP", "Evaluation"]
short_authors: Lu et al.
---
Current image captioning approaches generate descriptions which lack specific
information, such as named entities that are involved in the images. In this
paper we propose a new task which aims to generate informative image captions,
given images and hashtags as input. We propose a simple but effective approach
to tackle this problem. We first train a convolutional neural networks - long
short term memory networks (CNN-LSTM) model to generate a template caption
based on the input image. Then we use a knowledge graph based collective
inference algorithm to fill in the template with specific named entities
retrieved via the hashtags. Experiments on a new benchmark dataset collected
from Flickr show that our model generates news-style image descriptions with
much richer information. Our model outperforms unimodal baselines significantly
with various evaluation metrics.