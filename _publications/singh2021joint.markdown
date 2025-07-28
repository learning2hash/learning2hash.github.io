---
layout: publication
title: Joint Triplet Autoencoder For Histopathological Colon Cancer Nuclei Retrieval
authors: Satya Rajendra Singh, Shiv Ram Dubey, Shruthi Ms, Sairathan Ventrapragada,
  Saivamshi Salla Dasharatha
conference: Multimedia Tools and Applications
year: 2023
bibkey: singh2021joint
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.10262'}]
tags: ["Image Retrieval"]
short_authors: Singh et al.
---
Deep learning has shown a great improvement in the performance of visual
tasks. Image retrieval is the task of extracting the visually similar images
from a database for a query image. The feature matching is performed to rank
the images. Various hand-designed features have been derived in past to
represent the images. Nowadays, the power of deep learning is being utilized
for automatic feature learning from data in the field of biomedical image
analysis. Autoencoder and Siamese networks are two deep learning models to
learn the latent space (i.e., features or embedding). Autoencoder works based
on the reconstruction of the image from latent space. Siamese network utilizes
the triplets to learn the intra-class similarity and inter-class dissimilarity.
Moreover, Autoencoder is unsupervised, whereas Siamese network is supervised.
We propose a Joint Triplet Autoencoder Network (JTANet) by facilitating the
triplet learning in autoencoder framework. A joint supervised learning for
Siamese network and unsupervised learning for Autoencoder is performed.
Moreover, the Encoder network of Autoencoder is shared with Siamese network and
referred as the Siamcoder network. The features are extracted by using the
trained Siamcoder network for retrieval purpose. The experiments are performed
over Histopathological Routine Colon Cancer dataset. We have observed the
promising performance using the proposed JTANet model against the Autoencoder
and Siamese models for colon cancer nuclei retrieval in histopathological
images.