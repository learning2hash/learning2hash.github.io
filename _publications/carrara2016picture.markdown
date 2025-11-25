---
layout: publication
title: 'Picture It In Your Mind: Generating High Level Visual Representations From
  Textual Descriptions'
authors: "Fabio Carrara, Andrea Esuli, Tiziano Fagni, Fabrizio Falchi, Alejandro Moreo\
  \ Fern\xE1ndez"
conference: Information Retrieval Journal
year: 2016
bibkey: carrara2016picture
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1606.07287'}]
tags: ["Image Retrieval", "Similarity Search"]
short_authors: Carrara et al.
---
In this paper we tackle the problem of image search when the query is a short
textual description of the image the user is looking for. We choose to
implement the actual search process as a similarity search in a visual feature
space, by learning to translate a textual query into a visual representation.
Searching in the visual feature space has the advantage that any update to the
translation model does not require to reprocess the, typically huge, image
collection on which the search is performed. We propose Text2Vis, a neural
network that generates a visual representation, in the visual feature space of
the fc6-fc7 layers of ImageNet, from a short descriptive text. Text2Vis
optimizes two loss functions, using a stochastic loss-selection method. A
visual-focused loss is aimed at learning the actual text-to-visual feature
mapping, while a text-focused loss is aimed at modeling the higher-level
semantic concepts expressed in language and countering the overfit on
non-relevant visual components of the visual loss. We report preliminary
results on the MS-COCO dataset.