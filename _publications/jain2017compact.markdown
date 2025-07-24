---
layout: publication
title: Compact Environment-invariant Codes For Robust Visual Place Recognition
authors: Unnat Jain, Vinay P. Namboodiri, Gaurav Pandey
conference: 2017 14th Conference on Computer and Robot Vision (CRV)
year: 2017
bibkey: jain2017compact
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1709.08103'}]
tags: ["Compact Codes", "Hashing Methods", "Neural Hashing", "Robustness"]
short_authors: Unnat Jain, Vinay P. Namboodiri, Gaurav Pandey
---
Robust visual place recognition (VPR) requires scene representations that are
invariant to various environmental challenges such as seasonal changes and
variations due to ambient lighting conditions during day and night. Moreover, a
practical VPR system necessitates compact representations of environmental
features. To satisfy these requirements, in this paper we suggest a
modification to the existing pipeline of VPR systems to incorporate supervised
hashing. The modified system learns (in a supervised setting) compact binary
codes from image feature descriptors. These binary codes imbibe robustness to
the visual variations exposed to it during the training phase, thereby, making
the system adaptive to severe environmental changes. Also, incorporating
supervised hashing makes VPR computationally more efficient and easy to
implement on simple hardware. This is because binary embeddings can be learned
over simple-to-compute features and the distance computation is also in the
low-dimensional hamming space of binary codes. We have performed experiments on
several challenging data sets covering seasonal, illumination and viewpoint
variations. We also compare two widely used supervised hashing methods of
CCAITQ and MLH and show that this new pipeline out-performs or closely matches
the state-of-the-art deep learning VPR methods that are based on
high-dimensional features extracted from pre-trained deep convolutional neural
networks.