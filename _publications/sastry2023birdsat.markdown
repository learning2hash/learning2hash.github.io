---
layout: publication
title: 'Birdsat: Cross-view Contrastive Masked Autoencoders For Bird Species Classification
  And Mapping'
authors: Srikumar Sastry, Subash Khanal, Aayush Dhakal, di Huang, Nathan Jacobs
conference: Arxiv
year: 2023
bibkey: sastry2023birdsat
citations: 0
additional_links: [{name: Code, url: 'https://github.com/mvrl/BirdSAT\'}, {name: Paper,
    url: 'https://arxiv.org/abs/2310.19168'}]
tags: ["Datasets", "Multimodal Retrieval", "Self-Supervised"]
short_authors: Sastry et al.
---
We propose a metadata-aware self-supervised learning~(SSL)~framework useful
for fine-grained classification and ecological mapping of bird species around
the world. Our framework unifies two SSL strategies: Contrastive Learning~(CL)
and Masked Image Modeling~(MIM), while also enriching the embedding space with
metadata available with ground-level imagery of birds. We separately train
uni-modal and cross-modal ViT on a novel cross-view global bird species dataset
containing ground-level imagery, metadata (location, time), and corresponding
satellite imagery. We demonstrate that our models learn fine-grained and
geographically conditioned features of birds, by evaluating on two downstream
tasks: fine-grained visual classification~(FGVC) and cross-modal retrieval.
Pre-trained models learned using our framework achieve SotA performance on FGVC
of iNAT-2021 birds and in transfer learning settings for CUB-200-2011 and
NABirds datasets. Moreover, the impressive cross-modal retrieval performance of
our model enables the creation of species distribution maps across any
geographic region. The dataset and source code will be released at
https://github.com/mvrl/BirdSAT\}.