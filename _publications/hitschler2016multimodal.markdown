---
layout: publication
title: Multimodal Pivots For Image Caption Translation
authors: Julian Hitschler, Shigehiko Schamoni, Stefan Riezler
conference: 'Proceedings of the 54th Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)'
year: 2016
bibkey: hitschler2016multimodal
citations: 92
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1601.03916'}]
tags: ["Image Retrieval"]
short_authors: Julian Hitschler, Shigehiko Schamoni, Stefan Riezler
---
We present an approach to improve statistical machine translation of image
descriptions by multimodal pivots defined in visual space. The key idea is to
perform image retrieval over a database of images that are captioned in the
target language, and use the captions of the most similar images for
crosslingual reranking of translation outputs. Our approach does not depend on
the availability of large amounts of in-domain parallel data, but only relies
on available large datasets of monolingually captioned images, and on
state-of-the-art convolutional neural networks to compute image similarities.
Our experimental evaluation shows improvements of 1 BLEU point over strong
baselines.