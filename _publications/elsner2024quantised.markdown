---
layout: publication
title: 'Quantised Global Autoencoder: A Holistic Approach To Representing Visual Data'
authors: Tim Elsner, Paula Usinger, Victor Czech, Gregor Kobsik, Yanjiang He, Isaak
  Lim, Leif Kobbelt
conference: Arxiv
year: 2024
bibkey: elsner2024quantised
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.11913'}]
tags: []
short_authors: Elsner et al.
---
In quantised autoencoders, images are usually split into local patches, each
encoded by one token. This representation is redundant in the sense that the
same number of tokens is spend per region, regardless of the visual information
content in that region. Adaptive discretisation schemes like quadtrees are
applied to allocate tokens for patches with varying sizes, but this just varies
the region of influence for a token which nevertheless remains a local
descriptor. Modern architectures add an attention mechanism to the autoencoder
which infuses some degree of global information into the local tokens. Despite
the global context, tokens are still associated with a local image region. In
contrast, our method is inspired by spectral decompositions which transform an
input signal into a superposition of global frequencies. Taking the data-driven
perspective, we learn custom basis functions corresponding to the codebook
entries in our VQ-VAE setup. Furthermore, a decoder combines these basis
functions in a non-linear fashion, going beyond the simple linear superposition
of spectral decompositions. We can achieve this global description with an
efficient transpose operation between features and channels and demonstrate our
performance on compression.