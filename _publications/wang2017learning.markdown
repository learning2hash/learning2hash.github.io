---
layout: publication
title: Learning Two-Branch Neural Networks for Image-Text Matching Tasks
authors: Wang et al.
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2018
bibkey: wang2017learning
citations: 529
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1704.03470'}]
tags: []
---
Image-language matching tasks have recently attracted a lot of attention in
the computer vision field. These tasks include image-sentence matching, i.e.,
given an image query, retrieving relevant sentences and vice versa, and
region-phrase matching or visual grounding, i.e., matching a phrase to relevant
regions. This paper investigates two-branch neural networks for learning the
similarity between these two data modalities. We propose two network structures
that produce different output representations. The first one, referred to as an
embedding network, learns an explicit shared latent embedding space with a
maximum-margin ranking loss and novel neighborhood constraints. Compared to
standard triplet sampling, we perform improved neighborhood sampling that takes
neighborhood information into consideration while constructing mini-batches.
The second network structure, referred to as a similarity network, fuses the
two branches via element-wise product and is trained with regression loss to
directly predict a similarity score. Extensive experiments show that our
networks achieve high accuracies for phrase localization on the Flickr30K
Entities dataset and for bi-directional image-sentence retrieval on Flickr30K
and MSCOCO datasets.