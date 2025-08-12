---
layout: publication
title: Weakly-supervised Learning Of Visual Relations In Multimodal Pretraining
authors: Emanuele Bugliarello, Aida Nematzadeh, Lisa Anne Hendricks
conference: Proceedings of the 2023 Conference on Empirical Methods in Natural Language
  Processing
year: 2023
bibkey: bugliarello2023weakly
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.14281'}]
tags: ["EMNLP"]
short_authors: Emanuele Bugliarello, Aida Nematzadeh, Lisa Anne Hendricks
---
Recent work in vision-and-language pretraining has investigated supervised
signals from object detection data to learn better, fine-grained multimodal
representations. In this work, we take a step further and explore how we can
tap into supervision from small-scale visual relation data. In particular, we
propose two pretraining approaches to contextualise visual entities in a
multimodal setup. With verbalised scene graphs, we transform visual relation
triplets into structured captions, and treat them as additional image
descriptions. With masked relation prediction, we further encourage relating
entities from image regions with visually masked contexts. When applied to
strong baselines pretrained on large amounts of Web data, zero-shot evaluations
on both coarse-grained and fine-grained tasks show the efficacy of our methods
in learning multimodal representations from weakly-supervised relations data.