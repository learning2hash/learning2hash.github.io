---
layout: publication
title: 'ARTEMIS: Using Gans With Multiple Discriminators To Generate Art'
authors: James Baker
conference: Arxiv
year: 2023
bibkey: baker2023artemis
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.08278'}]
tags: []
short_authors: James Baker
---
We propose a novel method for generating abstract art. First an autoencoder
is trained to encode and decode the style representations of images, which are
extracted from source images with a pretrained VGG network. Then, the decoder
component of the autoencoder is extracted and used as a generator in a GAN. The
generator works with an ensemble of discriminators. Each discriminator takes
different style representations of the same images, and the generator is
trained to create images that create convincing style representations in order
to deceive all of the generators. The generator is also trained to maximize a
diversity term. The resulting images had a surreal, geometric quality. We call
our approach ARTEMIS (ARTistic Encoder- Multi- Discriminators Including
Self-Attention), as it uses the self-attention layers and an encoder-decoder
architecture.