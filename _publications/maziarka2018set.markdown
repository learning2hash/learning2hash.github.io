---
layout: publication
title: Set Aggregation Network As A Trainable Pooling Layer
authors: "\u0141ukasz Maziarka, Marek \u015Amieja, Aleksandra Nowak, Jacek Tabor,\
  \ \u0141ukasz Struski, Przemys\u0142aw Spurek"
conference: Lecture Notes in Computer Science
year: 2019
bibkey: maziarka2018set
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1810.01868'}]
tags: []
short_authors: Maziarka et al.
---
Global pooling, such as max- or sum-pooling, is one of the key ingredients in
deep neural networks used for processing images, texts, graphs and other types
of structured data. Based on the recent DeepSets architecture proposed by
Zaheer et al. (NIPS 2017), we introduce a Set Aggregation Network (SAN) as an
alternative global pooling layer. In contrast to typical pooling operators, SAN
allows to embed a given set of features to a vector representation of arbitrary
size. We show that by adjusting the size of embedding, SAN is capable of
preserving the whole information from the input. In experiments, we demonstrate
that replacing global pooling layer by SAN leads to the improvement of
classification accuracy. Moreover, it is less prone to overfitting and can be
used as a regularizer.