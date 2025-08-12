---
layout: publication
title: 'Refined: An Efficient Zero-shot-capable Approach To End-to-end Entity Linking'
authors: Tom Ayoola, Shubhi Tyagi, Joseph Fisher, Christos Christodoulopoulos, Andrea
  Pierleoni
conference: 'Proceedings of the 2022 Conference of the North American Chapter of the
  Association for Computational Linguistics: Human Language Technologies: Industry
  Track'
year: 2022
bibkey: ayoola2022refined
citations: 43
additional_links: [{name: Code, url: 'https://github.com/alexa/ReFinED'}, {name: Paper,
    url: 'https://arxiv.org/abs/2207.04108'}]
tags: ["Few Shot & Zero Shot", "NAACL"]
short_authors: Ayoola et al.
---
We introduce ReFinED, an efficient end-to-end entity linking model which uses
fine-grained entity types and entity descriptions to perform linking. The model
performs mention detection, fine-grained entity typing, and entity
disambiguation for all mentions within a document in a single forward pass,
making it more than 60 times faster than competitive existing approaches.
ReFinED also surpasses state-of-the-art performance on standard entity linking
datasets by an average of 3.7 F1. The model is capable of generalising to
large-scale knowledge bases such as Wikidata (which has 15 times more entities
than Wikipedia) and of zero-shot entity linking. The combination of speed,
accuracy and scale makes ReFinED an effective and cost-efficient system for
extracting entities from web-scale datasets, for which the model has been
successfully deployed. Our code and pre-trained models are available at
https://github.com/alexa/ReFinED