---
layout: publication
title: BinGAN Learning Compact Binary Descriptors with a Regularized GAN
authors: Maciej Zieba, Piotr Semberecki, Tarek El-Gaaly, Tomasz Trzcinski
conference: "Neural Information Processing Systems"
year: 2018
bibkey: zieba2018bingan
tags: ['GAN', 'NEURIPS']
---
In this paper we propose a novel regularization method for Generative Adversarial Networks that allows the model to learn discriminative yet compact binary representations of image patches (image descriptors). We exploit the dimensionality reduction that takes place in the intermediate layers of the discriminator network and train the binarized penultimate layers low-dimensional representation to mimic the distribution of the higher-dimensional preceding layers. To achieve this we introduce two loss terms that aim at (i) reducing the correlation between the dimensions of the binarized penultimate layers low-dimensional representation (i.e. maximizing joint entropy) and (ii) propagating the relations between the dimensions in the high-dimensional space to the low-dimensional space. We evaluate the resulting binary image descriptors on two challenging applications image matching and retrieval where they achieve state-of-the-art results.
