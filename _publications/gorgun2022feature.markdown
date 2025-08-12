---
layout: publication
title: Feature Embedding By Template Matching As A Resnet Block
authors: Ada Gorgun, Yeti Z. Gurbuz, A. Aydin Alatan
conference: Arxiv
year: 2022
bibkey: gorgun2022feature
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.00992'}]
tags: []
short_authors: Ada Gorgun, Yeti Z. Gurbuz, A. Aydin Alatan
---
Convolution blocks serve as local feature extractors and are the key to
success of the neural networks. To make local semantic feature embedding rather
explicit, we reformulate convolution blocks as feature selection according to
the best matching kernel. In this manner, we show that typical ResNet blocks
indeed perform local feature embedding via template matching once batch
normalization (BN) followed by a rectified linear unit (ReLU) is interpreted as
arg-max optimizer. Following this perspective, we tailor a residual block that
explicitly forces semantically meaningful local feature embedding through using
label information. Specifically, we assign a feature vector to each local
region according to the classes that the corresponding region matches. We
evaluate our method on three popular benchmark datasets with several
architectures for image classification and consistently show that our approach
substantially improves the performance of the baseline architectures.