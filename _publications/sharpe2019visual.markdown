---
layout: publication
title: Visual Natural Language Query Auto-completion For Estimating Instance Probabilities
authors: Samuel Sharpe, Jin Yan, Fan Wu, Iddo Drori
conference: CVPR Language and Vision Workshop 2019
year: 2019
bibkey: sharpe2019visual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.04887'}]
tags: ["CVPR"]
short_authors: Sharpe et al.
---
We present a new task of query auto-completion for estimating instance
probabilities. We complete a user query prefix conditioned upon an image. Given
the complete query, we fine tune a BERT embedding for estimating probabilities
of a broad set of instances. The resulting instance probabilities are used for
selection while being agnostic to the segmentation or attention mechanism. Our
results demonstrate that auto-completion using both language and vision
performs better than using only language, and that fine tuning a BERT embedding
allows to efficiently rank instances in the image. In the spirit of
reproducible research we make our data, models, and code available.