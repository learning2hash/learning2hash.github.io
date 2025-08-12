---
layout: publication
title: Inferring Offensiveness In Images From Natural Language Supervision
authors: Patrick Schramowski, Kristian Kersting
conference: Arxiv
year: 2021
bibkey: schramowski2021inferring
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.04222'}]
tags: ["Datasets", "Evaluation"]
short_authors: Patrick Schramowski, Kristian Kersting
---
Probing or fine-tuning (large-scale) pre-trained models results in
state-of-the-art performance for many NLP tasks and, more recently, even for
computer vision tasks when combined with image data. Unfortunately, these
approaches also entail severe risks. In particular, large image datasets
automatically scraped from the web may contain derogatory terms as categories
and offensive images, and may also underrepresent specific classes.
Consequently, there is an urgent need to carefully document datasets and curate
their content. Unfortunately, this process is tedious and error-prone. We show
that pre-trained transformers themselves provide a methodology for the
automated curation of large-scale vision datasets. Based on human-annotated
examples and the implicit knowledge of a CLIP based model, we demonstrate that
one can select relevant prompts for rating the offensiveness of an image. In
addition to e.g. privacy violation and pornographic content previously
identified in ImageNet, we demonstrate that our approach identifies further
inappropriate and potentially offensive content.