---
layout: publication
title: Learning A Predictable And Generative Vector Representation For Objects
authors: Rohit Girdhar, David F. Fouhey, Mikel Rodriguez, Abhinav Gupta
conference: Lecture Notes in Computer Science
year: 2016
bibkey: girdhar2016learning
citations: 140
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1603.08637'}]
tags: ["Image Retrieval", "Unsupervised", "Vector Indexing"]
short_authors: Girdhar et al.
---
What is a good vector representation of an object? We believe that it should
be generative in 3D, in the sense that it can produce new 3D objects; as well
as be predictable from 2D, in the sense that it can be perceived from 2D
images. We propose a novel architecture, called the TL-embedding network, to
learn an embedding space with these properties. The network consists of two
components: (a) an autoencoder that ensures the representation is generative;
and (b) a convolutional network that ensures the representation is predictable.
This enables tackling a number of tasks including voxel prediction from 2D
images and 3D model retrieval. Extensive experimental analysis demonstrates the
usefulness and versatility of this embedding.