---
layout: publication
title: Looking At Outfit To Parse Clothing
authors: Pongsate Tangseng, Zhipeng Wu, Kota Yamaguchi
conference: Arxiv
year: 2017
bibkey: tangseng2017looking
citations: 48
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1703.01386'}]
tags: [Evaluation, Image Retrieval, Datasets]
short_authors: Pongsate Tangseng, Zhipeng Wu, Kota Yamaguchi
---
This paper extends fully-convolutional neural networks (FCN) for the clothing
parsing problem. Clothing parsing requires higher-level knowledge on clothing
semantics and contextual cues to disambiguate fine-grained categories. We
extend FCN architecture with a side-branch network which we refer outfit
encoder to predict a consistent set of clothing labels to encourage
combinatorial preference, and with conditional random field (CRF) to explicitly
consider coherent label assignment to the given image. The empirical results
using Fashionista and CFPD datasets show that our model achieves
state-of-the-art performance in clothing parsing, without additional
supervision during training. We also study the qualitative influence of
annotation on the current clothing parsing benchmarks, with our Web-based tool
for multi-scale pixel-wise annotation and manual refinement effort to the
Fashionista dataset. Finally, we show that the image representation of the
outfit encoder is useful for dress-up image retrieval application.