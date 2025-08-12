---
layout: publication
title: Hypernymization Of Named Entity-rich Captions For Grounding-based Multi-modal
  Pretraining
authors: Giacomo Nebbia, Adriana Kovashka
conference: Proceedings of the 2023 ACM International Conference on Multimedia Retrieval
year: 2023
bibkey: nebbia2023hypernymization
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.13130'}]
tags: ["Text Retrieval"]
short_authors: Giacomo Nebbia, Adriana Kovashka
---
Named entities are ubiquitous in text that naturally accompanies images,
especially in domains such as news or Wikipedia articles. In previous work,
named entities have been identified as a likely reason for low performance of
image-text retrieval models pretrained on Wikipedia and evaluated on named
entities-free benchmark datasets. Because they are rarely mentioned, named
entities could be challenging to model. They also represent missed learning
opportunities for self-supervised models: the link between named entity and
object in the image may be missed by the model, but it would not be if the
object were mentioned using a more common term. In this work, we investigate
hypernymization as a way to deal with named entities for pretraining
grounding-based multi-modal models and for fine-tuning on open-vocabulary
detection. We propose two ways to perform hypernymization: (1) a ``manual''
pipeline relying on a comprehensive ontology of concepts, and (2) a ``learned''
approach where we train a language model to learn to perform hypernymization.
We run experiments on data from Wikipedia and from The New York Times. We
report improved pretraining performance on objects of interest following
hypernymization, and we show the promise of hypernymization on open-vocabulary
detection, specifically on classes not seen during training.