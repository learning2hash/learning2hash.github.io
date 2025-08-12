---
layout: publication
title: Producing Augmentation-invariant Embeddings From Real-life Imagery
authors: Sergio Manuel Papadakis, Sanjay Addicam
conference: Arxiv
year: 2021
bibkey: papadakis2021producing
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.03415'}]
tags: []
short_authors: Sergio Manuel Papadakis, Sanjay Addicam
---
This article presents an efficient way to produce feature-rich,
high-dimensionality embedding spaces from real-life images. The features
produced are designed to be independent from augmentations used in real-life
cases which appear on social media. Our approach uses convolutional neural
networks (CNN) to produce an embedding space. An ArcFace head was used to train
the model by employing automatically produced augmentations. Additionally, we
present a way to make an ensemble out of different embeddings containing the
same semantic information, a way to normalize the resulting embedding using an
external dataset, and a novel way to perform quick training of these models
with a high number of classes in the ArcFace head. Using this approach we
achieved the 2nd place in the 2021 Facebook AI Image Similarity Challenge:
Descriptor Track.