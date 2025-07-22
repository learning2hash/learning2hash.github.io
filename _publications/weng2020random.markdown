---
layout: publication
title: Random VLAD based Deep Hashing for Efficient Image Retrieval
authors: Weng et al.
conference: 2016 IEEE International Conference on Multimedia and Expo (ICME)
year: 2020
bibkey: weng2020random
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.02333'}]
tags: ["Neural-Hashing", "Hashing-Methods", "Image-Retrieval"]
---
Image hash algorithms generate compact binary representations that can be
quickly matched by Hamming distance, thus become an efficient solution for
large-scale image retrieval. This paper proposes RV-SSDH, a deep image hash
algorithm that incorporates the classical VLAD (vector of locally aggregated
descriptors) architecture into neural networks. Specifically, a novel neural
network component is formed by coupling a random VLAD layer with a latent hash
layer through a transform layer. This component can be combined with
convolutional layers to realize a hash algorithm. We implement RV-SSDH as a
point-wise algorithm that can be efficiently trained by minimizing
classification error and quantization loss. Comprehensive experiments show this
new architecture significantly outperforms baselines such as NetVLAD and SSDH,
and offers a cost-effective trade-off in the state-of-the-art. In addition, the
proposed random VLAD layer leads to satisfactory accuracy with low complexity,
thus shows promising potentials as an alternative to NetVLAD.