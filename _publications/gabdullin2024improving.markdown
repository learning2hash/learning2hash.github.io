---
layout: publication
title: Improving Analytical Color And Texture Similarity Estimation Methods For Dataset-agnostic
  Person Reidentification
authors: Nikita Gabdullin
conference: Arxiv
year: 2024
bibkey: gabdullin2024improving
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.05076'}]
tags: ["Datasets"]
short_authors: Nikita Gabdullin
---
This paper studies a combined person reidentification (re-id) method that
uses human parsing, analytical feature extraction and similarity estimation
schemes. One of its prominent features is its low computational requirements so
it can be implemented on edge devices. The method allows direct comparison of
specific image regions using interpretable features which consist of color and
texture channels. It is proposed to analyze and compare colors in CIE-Lab color
space using histogram smoothing for noise reduction. A novel pre-configured
latent space (LS) supervised autoencoder (SAE) is proposed for texture analysis
which encodes input textures as LS points. This allows to obtain more accurate
similarity measures compared to simplistic label comparison. The proposed
method also does not rely upon photos or other re-id data for training, which
makes it completely re-id dataset-agnostic. The viability of the proposed
method is verified by computing rank-1, rank-10, and mAP re-id metrics on
Market1501 dataset. The results are comparable to those of conventional deep
learning methods and the potential ways to further improve the method are
discussed.