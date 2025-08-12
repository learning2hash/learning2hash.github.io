---
layout: publication
title: Multimodal Metadata Assignment For Cultural Heritage Artifacts
authors: "Luis Rei, Dunja Mladeni\u0107, Mareike Dorozynski, Franz Rottensteiner,\
  \ Thomas Schleider, Rapha\xEBl Troncy, Jorge Sebasti\xE1n Lozano, Mar Gait\xE1n\
  \ Salvatella"
conference: Multimedia Systems
year: 2022
bibkey: rei2022multimodal
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2406.00423'}]
tags: ["Datasets"]
short_authors: Rei et al.
---
We develop a multimodal classifier for the cultural heritage domain using a
late fusion approach and introduce a novel dataset. The three modalities are
Image, Text, and Tabular data. We based the image classifier on a ResNet
convolutional neural network architecture and the text classifier on a
multilingual transformer architecture (XML-Roberta). Both are trained as
multitask classifiers and use the focal loss to handle class imbalance. Tabular
data and late fusion are handled by Gradient Tree Boosting. We also show how we
leveraged specific data models and taxonomy in a Knowledge Graph to create the
dataset and to store classification results. All individual classifiers
accurately predict missing properties in the digitized silk artifacts, with the
multimodal approach providing the best results.