---
layout: publication
title: Unifying Deep Local And Global Features For Image Search
authors: Bingyi Cao, Andre Araujo, Jack Sim
conference: Arxiv
year: 2020
citations: 226
bibkey: cao2020unifying
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2001.05027'}, {name: Code,
    url: 'https://github.com/tensorflow/models/tree/master/research/delf'}]
tags: [Applications, Has Code]
---
Image retrieval is the problem of searching an image database for items that
are similar to a query image. To address this task, two main types of image
representations have been studied: global and local image features. In this
work, our key contribution is to unify global and local features into a single
deep model, enabling accurate retrieval with efficient feature extraction. We
refer to the new model as DELG, standing for DEep Local and Global features. We
leverage lessons from recent feature learning work and propose a model that
combines generalized mean pooling for global features and attentive selection
for local features. The entire network can be learned end-to-end by carefully
balancing the gradient flow between two heads -- requiring only image-level
labels. We also introduce an autoencoder-based dimensionality reduction
technique for local features, which is integrated into the model, improving
training efficiency and matching performance. Comprehensive experiments show
that our model achieves state-of-the-art image retrieval on the Revisited
Oxford and Paris datasets, and state-of-the-art single-model instance-level
recognition on the Google Landmarks dataset v2. Code and models are available
at https://github.com/tensorflow/models/tree/master/research/delf .