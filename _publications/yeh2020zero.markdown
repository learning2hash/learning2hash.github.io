---
layout: publication
title: Zero-shot Recognition Through Image-guided Semantic Classification
authors: Mei-chen Yeh, Fang Li
conference: 2021 IEEE International Conference on Image Processing (ICIP)
year: 2021
bibkey: yeh2020zero
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.11814'}]
tags: []
short_authors: Mei-chen Yeh, Fang Li
---
We present a new embedding-based framework for zero-shot learning (ZSL). Most
embedding-based methods aim to learn the correspondence between an image
classifier (visual representation) and its class prototype (semantic
representation) for each class. Motivated by the binary relevance method for
multi-label classification, we propose to inversely learn the mapping between
an image and a semantic classifier. Given an input image, the proposed
Image-Guided Semantic Classification (IGSC) method creates a label classifier,
being applied to all label embeddings to determine whether a label belongs to
the input image. Therefore, semantic classifiers are image-adaptive and are
generated during inference. IGSC is conceptually simple and can be realized by
a slight enhancement of an existing deep architecture for classification; yet
it is effective and outperforms state-of-the-art embedding-based generalized
ZSL approaches on standard benchmarks.