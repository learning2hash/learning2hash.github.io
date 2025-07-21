---
layout: publication
title: Cross-modal Image Retrieval with Deep Mutual Information Maximization
authors: Gu et al.
conference: Neurocomputing
year: 2022
bibkey: gu2021cross
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.06032'}]
tags: ["Image-Retrieval"]
---
In this paper, we study the cross-modal image retrieval, where the inputs
contain a source image plus some text that describes certain modifications to
this image and the desired image. Prior work usually uses a three-stage
strategy to tackle this task: 1) extract the features of the inputs; 2) fuse
the feature of the source image and its modified text to obtain fusion feature;
3) learn a similarity metric between the desired image and the source image +
modified text by using deep metric learning. Since classical image/text
encoders can learn the useful representation and common pair-based loss
functions of distance metric learning are enough for cross-modal retrieval,
people usually improve retrieval accuracy by designing new fusion networks.
However, these methods do not successfully handle the modality gap caused by
the inconsistent distribution and representation of the features of different
modalities, which greatly influences the feature fusion and similarity
learning. To alleviate this problem, we adopt the contrastive self-supervised
learning method Deep InforMax (DIM) to our approach to bridge this gap by
enhancing the dependence between the text, the image, and their fusion.
Specifically, our method narrows the modality gap between the text modality and
the image modality by maximizing mutual information between their not exactly
semantically identical representation. Moreover, we seek an effective common
subspace for the semantically same fusion feature and desired image's feature
by utilizing Deep InforMax between the low-level layer of the image encoder and
the high-level layer of the fusion network. Extensive experiments on three
large-scale benchmark datasets show that we have bridged the modality gap
between different modalities and achieve state-of-the-art retrieval
performance.