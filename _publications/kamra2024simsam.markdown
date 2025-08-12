---
layout: publication
title: 'Simsam: Simple Siamese Representations Based Semantic Affinity Matrix For
  Unsupervised Image Segmentation'
authors: Chanda Grover Kamra, Indra Deep Mastan, Nitin Kumar, Debayan Gupta
conference: 2024 IEEE International Conference on Image Processing (ICIP)
year: 2024
bibkey: kamra2024simsam
citations: 2
additional_links: [{name: Code, url: 'https://github.com/chandagrover/SimSAM'}, {
    name: Paper, url: 'https://arxiv.org/abs/2406.07986'}]
tags: []
short_authors: Kamra et al.
---
Recent developments in self-supervised learning (SSL) have made it possible
to learn data representations without the need for annotations. Inspired by the
non-contrastive SSL approach (SimSiam), we introduce a novel framework SIMSAM
to compute the Semantic Affinity Matrix, which is significant for unsupervised
image segmentation. Given an image, SIMSAM first extracts features using
pre-trained DINO-ViT, then projects the features to predict the correlations of
dense features in a non-contrastive way. We show applications of the Semantic
Affinity Matrix in object segmentation and semantic segmentation tasks. Our
code is available at https://github.com/chandagrover/SimSAM.