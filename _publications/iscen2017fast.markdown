---
layout: publication
title: Fast Spectral Ranking For Similarity Search
authors: Iscen Ahmet, Avrithis Yannis, Tolias Giorgos, Furon Teddy, Chum Ondrej
conference: "Arxiv"
year: 2017
bibkey: iscen2017fast
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1703.06935"}
tags: ['ARXIV', 'Deep Learning', 'Graph']
---
Despite the success of deep learning on representing images for particular object retrieval recent studies show that the learned representations still lie on manifolds in a high dimensional space. This makes the Euclidean nearest neighbor search biased for this task. Exploring the manifolds online remains expensive even if a nearest neighbor graph has been computed offline. This work introduces an explicit embedding reducing manifold search to Euclidean search followed by dot product similarity search. This is equivalent to linear graph filtering of a sparse signal in the frequency domain. To speed up online search we compute an approximate Fourier basis of the graph offline. We improve the state of art on particular object retrieval datasets including the challenging Instre dataset containing small objects. At a scale of 10^5 images the offline cost is only a few hours while query time is comparable to standard similarity search.
