---
layout: publication
title: Learning Dense Convolutional Embeddings For Semantic Segmentation
authors: Adam W. Harley, Konstantinos G. Derpanis, Iasonas Kokkinos
conference: Arxiv
year: 2015
bibkey: harley2015learning
citations: 22
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.04377'}]
tags: []
short_authors: Adam W. Harley, Konstantinos G. Derpanis, Iasonas Kokkinos
---
This paper proposes a new deep convolutional neural network (DCNN)
architecture that learns pixel embeddings, such that pairwise distances between
the embeddings can be used to infer whether or not the pixels lie on the same
region. That is, for any two pixels on the same object, the embeddings are
trained to be similar; for any pair that straddles an object boundary, the
embeddings are trained to be dissimilar. Experimental results show that when
this embedding network is used in conjunction with a DCNN trained on semantic
segmentation, there is a systematic improvement in per-pixel classification
accuracy. Our contributions are integrated in the popular Caffe deep learning
framework, and consist in straightforward modifications to convolution
routines. As such, they can be exploited for any task involving convolution
layers.