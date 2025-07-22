---
layout: publication
title: Joint Wasserstein Autoencoders For Aligning Multimodal Embeddings
authors: Mahajan Shweta, Botschen Teresa, Gurevych Iryna, Roth Stefan
conference: 2019 IEEE/CVF International Conference on Computer Vision Workshop (ICCVW)
year: 2019
bibkey: mahajan2019joint
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.06635'}]
tags: ["Supervised", "ICCV", "Multimodal-Retrieval", "Datasets"]
short_authors: Mahajan et al.
---
One of the key challenges in learning joint embeddings of multiple
modalities, e.g. of images and text, is to ensure coherent cross-modal
semantics that generalize across datasets. We propose to address this through
joint Gaussian regularization of the latent representations. Building on
Wasserstein autoencoders (WAEs) to encode the input in each domain, we enforce
the latent embeddings to be similar to a Gaussian prior that is shared across
the two domains, ensuring compatible continuity of the encoded semantic
representations of images and texts. Semantic alignment is achieved through
supervision from matching image-text pairs. To show the benefits of our
semi-supervised representation, we apply it to cross-modal retrieval and phrase
localization. We not only achieve state-of-the-art accuracy, but significantly
better generalization across datasets, owing to the semantic continuity of the
latent space.