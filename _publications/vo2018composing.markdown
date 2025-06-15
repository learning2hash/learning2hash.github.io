---
layout: publication
title: 'Composing Text And Image For Image Retrieval - An Empirical Odyssey'
authors: Nam Vo et al.
conference: "Arxiv"
year: 2018
citations: 239
bibkey: vo2018composing
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1812.07119'}
tags: ['Tools and Libraries', 'Applications']
---
In this paper, we study the task of image retrieval, where the input query is
specified in the form of an image plus some text that describes desired
modifications to the input image. For example, we may present an image of the
Eiffel tower, and ask the system to find images which are visually similar but
are modified in small ways, such as being taken at nighttime instead of during
the day. To tackle this task, we learn a similarity metric between a target
image and a source image plus source text, an embedding and composing function
such that target image feature is close to the source image plus text
composition feature. We propose a new way to combine image and text using such
function that is designed for the retrieval task. We show this outperforms
existing approaches on 3 different datasets, namely Fashion-200k, MIT-States
and a new synthetic dataset we create based on CLEVR. We also show that our
approach can be used to classify input queries, in addition to image retrieval.
