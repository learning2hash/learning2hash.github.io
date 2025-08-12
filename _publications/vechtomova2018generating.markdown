---
layout: publication
title: Generating Lyrics With Variational Autoencoder And Multi-modal Artist Embeddings
authors: Olga Vechtomova, Hareesh Bahuleyan, Amirpasha Ghabussi, Vineet John
conference: Arxiv
year: 2018
bibkey: vechtomova2018generating
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.08318'}]
tags: ["Multimodal Retrieval", "Unsupervised"]
short_authors: Vechtomova et al.
---
We present a system for generating song lyrics lines conditioned on the style
of a specified artist. The system uses a variational autoencoder with artist
embeddings. We propose the pre-training of artist embeddings with the
representations learned by a CNN classifier, which is trained to predict
artists based on MEL spectrograms of their song clips. This work is the first
step towards combining audio and text modalities of songs for generating lyrics
conditioned on the artist's style. Our preliminary results suggest that there
is a benefit in initializing artists' embeddings with the representations
learned by a spectrogram classifier.