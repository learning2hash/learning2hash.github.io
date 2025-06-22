---
layout: publication
title: Tile Compression And Embeddings For Multi-label Classification In Geolifeclef
  2024
authors: Anthony Miyaguchi, Patcharapong Aphiwetsa, Mark Mcduffie
conference: Arxiv
year: 2024
citations: 0
bibkey: miyaguchi2024tile
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.06326'}, {name: Code,
    url: 'https://github.com/dsgt-kaggle-clef/geolifeclef-2024'}]
tags: [Hashing Methods, Has Code, Supervised]
---
We explore methods to solve the multi-label classification task posed by the
GeoLifeCLEF 2024 competition with the DS@GT team, which aims to predict the
presence and absence of plant species at specific locations using spatial and
temporal remote sensing data. Our approach uses frequency-domain coefficients
via the Discrete Cosine Transform (DCT) to compress and pre-compute the raw
input data for convolutional neural networks. We also investigate nearest
neighborhood models via locality-sensitive hashing (LSH) for prediction and to
aid in the self-supervised contrastive learning of embeddings through tile2vec.
Our best competition model utilized geolocation features with a leaderboard
score of 0.152 and a best post-competition score of 0.161. Source code and
models are available at https://github.com/dsgt-kaggle-clef/geolifeclef-2024.