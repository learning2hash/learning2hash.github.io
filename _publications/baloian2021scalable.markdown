---
layout: publication
title: Scalable Visual Attribute Extraction Through Hidden Layers Of A Residual Convnet
authors: Andres Baloian, Nils Murrugarra-Llerena, Jose M. Saavedra
conference: Arxiv
year: 2021
bibkey: baloian2021scalable
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.00161'}]
tags: [Evaluation]
short_authors: Andres Baloian, Nils Murrugarra-Llerena, Jose M. Saavedra
---
Visual attributes play an essential role in real applications based on image
retrieval. For instance, the extraction of attributes from images allows an
eCommerce search engine to produce retrieval results with higher precision. The
traditional manner to build an attribute extractor is by training a
convnet-based classifier with a fixed number of classes. However, this approach
does not scale for real applications where the number of attributes changes
frequently. Therefore in this work, we propose an approach for extracting
visual attributes from images, leveraging the learned capability of the hidden
layers of a general convolutional network to discriminate among different
visual features. We run experiments with a resnet-50 trained on Imagenet, on
which we evaluate the output of its different blocks to discriminate between
colors and textures. Our results show that the second block of the resnet is
appropriate for discriminating colors, while the fourth block can be used for
textures. In both cases, the achieved accuracy of attribute classification is
superior to 93%. We also show that the proposed embeddings form local
structures in the underlying feature space, which makes it possible to apply
reduction techniques like UMAP, maintaining high accuracy and widely reducing
the size of the feature space.